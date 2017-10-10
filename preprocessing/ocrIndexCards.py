#-*- coding: utf-8 -*-

import os
import csv
from subprocess import Popen, PIPE


__location__ = os.path.dirname(os.path.realpath(__file__))

inputDir = "\\\\romeo\\SPE\\EspyWorkingSeries1\\indexCardsPNG"
outputDir = os.path.join(__location__, "railsData")

aspaceFile = open(os.path.join(__location__, "aspaceS1.csv"), 'r')
aspaceIDs = csv.reader(aspaceFile, delimiter="|")

headerRow = ["state_abbreviation", "root_filename", "file_group", "ocr_text", "used_check", "aspace"]
outputData = [headerRow]


fileCount = 0
for file in os.listdir(inputDir):
	if file.endswith(".png"):
		fileCount = fileCount + 1
		#outputLine = [str(fileCount)]
		outputLine = []
		print (file)
		
		
		path = os.path.join(inputDir, file)
		filename = os.path.splitext(file)[0]
		if filename.lower().endswith("a"):
		
			stateAbb = file.split("_")[1]
			outputLine.append(stateAbb)
			
			box = file.split("_")[0]
			for boxLine in aspaceIDs:
				if boxLine[0] == box:
					aspaceID = boxLine[1]
			
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
						
						otherPath = os.path.join(inputDir, otherFile)
						process = Popen(['tesseract', otherPath, "stdout"], stdout=PIPE, stderr=PIPE)
						stdout, stderr = process.communicate()
						ocrText = stdout.strip()
						ocrString = ocrString + b" " + ocrText.strip()
					
			
			
			outputLine.append("; ".join(fileList))
			outputLine.append(" ".join(ocrString.decode("utf-8").splitlines()))
			outputLine.append(False)
			outputLine.append(aspaceID)
		
	outputData.append(outputLine)
		
	#write data to file
	csvOut = open(os.path.join(outputDir, "indexCards.csv"), "w", newline='', encoding='utf-8')
	writer = csv.writer(csvOut, delimiter='|')
	writer.writerows(outputData)
	csvOut.close()