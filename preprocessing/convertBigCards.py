import os
from subprocess import Popen, PIPE

inputPath = "\\\\romeo\\SPE\\EspyWorkingSeries1\\largeCardsTIF"
outputPath = "\\\\romeo\\SPE\\EspyWorkingSeries1\\largeCardsPNG"


for root, dirs, files in os.walk(inputPath):
	for file in files:
		if file.lower().endswith(".tif"):
			#if file == "B01_AL_000014a.tif" or file == "B01_AL_000052a.tif":
			print (file)
			
			img = os.path.join(root, file)
			
			if "B20_CA_" in file:
				file = file.replace ("B20_CA_", "B20_LA_")
			elif "B20_MILITARY" in file:
				file = file.replace ("B20_MILITARY", "B20_MIL")
			elif "B19_FEDERAL" in file:
				file = file.replace ("B19_FEDERAL", "B19_FED")
			elif "B19_GUAM" in file:
				file = file.replace ("B19_GUAM", "B19_GU")
			elif "B19_INDIAN-TRIBAL" in file:
				file = file.replace ("B19_INDIAN-TRIBAL", "B19_INDIAN")
			elif "B19_DECA" in file:
				file = file.replace ("B19_DECA", "B19_DE")

			outFile = os.path.join(outputPath, os.path.splitext(file)[0] + ".png")
			
			cmdString = "convert -density 300 \"" + img + "\" \"" + outFile + "\""
			convert = Popen(cmdString, shell=True, stdout=PIPE, stderr=PIPE)
			stdout, stderr = convert.communicate()
			if len(stdout) > 0:
				print (stdout)
			if len(stderr) > 0:
				print (stderr)