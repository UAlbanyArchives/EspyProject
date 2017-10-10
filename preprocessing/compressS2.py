import os
from subprocess import Popen, PIPE

inputTIFFs = "\\\\romeo\SPE\\EspyWorkingSeries2\\tif"
workingOutput = "\\\\romeo\SPE\\EspyWorkingSeries2\\jpg"

for root, dirs, files in os.walk(inputTIFFs):
	for file in files:
		if file.lower().endswith("tif"):
			print (file)
			itemFolder = os.path.basename(root)
			folderPath = os.path.join(workingOutput, itemFolder)
			print (itemFolder)
			if not os.path.isdir(folderPath):
				os.makedirs(folderPath)
				
			filePath = os.path.join(root, file)
			
			outPath = os.path.join(folderPath, os.path.splitext(file)[0] + ".jpg")
			print ("	" + file)
			cmdString = "convert -density 300 \"" + filePath + "\" \"" + outPath + "\""
			convert = Popen(cmdString, shell=True, stdout=PIPE, stderr=PIPE)
			stdout, stderr = convert.communicate()
			if len(stdout) > 0:
				print (stdout)
			if len(stderr) > 0:
				print (stderr)
		