import os
from subprocess import Popen, PIPE

inputPath = "\\\\romeo\\SPE\\EspyWorkingSeries1\\indexCardsTIF"
outputPath = "\\\\romeo\\SPE\\EspyWorkingSeries1\\indexCardsPNG"


for root, dirs, files in os.walk(inputPath):
	for file in files:
		if file.lower().endswith(".tif"):
			#if file == "B01_AL_000014a.tif" or file == "B01_AL_000052a.tif":
			print (file)
			img = os.path.join(root, file)
			
			if "B05_Indian-Tribal" in file:
				file = file.replace ("B05_Indian-Tribal", "B05_INDIAN")
			elif "B08_MILITARY" in file:
				file = file.replace ("B08_MILITARY", "B08_MIL")
			elif "B18_SPECIAL-CATEGORIES" in file:
				file = file.replace ("B18_SPECIAL-CATEGORIES", "B18_SPECIAL")
			
			outFile = os.path.join(outputPath, os.path.splitext(file)[0] + ".png")
			
			if os.path.isfile(outFile):
				pass
			else:
			
				cmdString = "convert -density 300 \"" + img + "\" \"" + outFile + "\""
				convert = Popen(cmdString, shell=True, stdout=PIPE, stderr=PIPE)
				stdout, stderr = convert.communicate()
				if len(stdout) > 0:
					print (stdout)
				if len(stderr) > 0:
					print (stderr)