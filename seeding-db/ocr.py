#-*- coding: utf-8 -*-

import os
import csv
from subprocess import Popen, PIPE


inputDir = "C:\\Projects\\icpsr\\pngTest"
outputDir = "C:\\Projects\\icpsr"

headerRow = ["id", "state", "root_file", "file_paths", "text"]
outputData = [headerRow]


fileCount = 0
for file in os.listdir(inputDir):
	fileCount = fileCount + 1
	outputLine = [str(fileCount)]
	print (file)
	
	
	path = os.path.join(inputDir, file)
	filename = os.path.splitext(file)[0]
	if filename.lower().endswith("a"):
	
		stateAbb = file.split("_")[1]
		outputLine.append(stateAbb)
		
		outputLine.append(file)
		matchFiles = filename[:-1]
		fileList = [file]
		
		process = Popen(['tesseract', path, "stdout"], stdout=PIPE, stderr=PIPE)
		stdout, stderr = process.communicate()
		ocrText = stdout.strip()
		ocrString = ocrText.strip()
	
		for otherFile in os.listdir(inputDir):
			if otherFile.startswith(matchFiles):
				if otherFile != file:
					fileList.append(otherFile)
					
					process = Popen(['tesseract', path, "stdout"], stdout=PIPE, stderr=PIPE)
					stdout, stderr = process.communicate()
					ocrText = stdout.strip()
					ocrString = ocrString + b" " + ocrText.strip()
				
		
		
		outputLine.append("; ".join(fileList))
		outputLine.append(" ".join(ocrString.decode("utf-8").splitlines()))
	
	outputData.append(outputLine)
		
#write data to file
csvOut = open(os.path.join(outputDir, "fileTable.csv"), "w", newline='', encoding='utf-8')
writer = csv.writer(csvOut, delimiter='|')
writer.writerows(outputData)
csvOut.close()