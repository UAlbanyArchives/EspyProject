import os
from subprocess import Popen, PIPE

inputPath = "C:\\Projects\\icpsr\\B01"
outputPath = "C:\\Projects\\icpsr\\testFiles"


for root, dirs, files in os.walk(inputPath):
	for file in files:
		if file.lower().endswith(".tif"):
			if file == "B01_AL_000014a.tif" or file == "B01_AL_000052a.tif":
				print (file)
				img = os.path.join(root, file)
				outFile = os.path.join(outputPath, os.path.splitext(file)[0] + ".png")
				
				cmdString = "convert -density 300 \"" + img + "\" \"" + outFile + "\""
				convert = Popen(cmdString, shell=True, stdout=PIPE, stderr=PIPE)
				stdout, stderr = convert.communicate()
				if len(stdout) > 0:
					print (stdout)
				if len(stderr) > 0:
					print (stderr)