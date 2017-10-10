#-*- coding: utf-8 -*-

import os
import csv

__location__ = os.path.dirname(os.path.realpath(__file__))



inputFiles = "\\\\romeo\\SPE\\EspyWorkingSeries2\\jpg"

headerRow = ["filename", "used_check", "aspace", "folder_name"]
outputData = [headerRow]

for root, dirs, files in os.walk(inputFiles):
	for file in files:
		if file.endswith(".jpg"):
			print (file)
			aspace = ""
			folder = os.path.basename(root)
			aspaceFile = open(os.path.join(__location__, "aspaceS2.csv"), "r")
			aspaceIDs = csv.reader(aspaceFile, delimiter="|")
			for line in aspaceIDs:
				if line[0] == folder:
					aspace = line[1]
					folderName =  line[2]
			
			outputData.append([file, False, aspace, folderName])		
		
#write data to file
csvOut = open(os.path.join(__location__, "railsData", "reference.csv"), "w", newline='', encoding='utf-8')
writer = csv.writer(csvOut, delimiter='|')
writer.writerows(outputData)
csvOut.close()