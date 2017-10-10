#-*- coding: utf-8 -*-

import os
import csv

__location__ = os.path.dirname(os.path.realpath(__file__))


inputFiles = "\\\\romeo\\SPE\\EspyWorkingSeries1\\indexCardsPNG"

dataPath = os.path.join("\\\\romeo\\SPE\\Espy Working Files", "railsData", "indexCards.csv")

fileList = []

for root, dirs, files in os.walk(inputFiles):
	for file in files:
		fileList.append(file)

dataFile = open(dataPath, "r",  encoding='utf-8')
dataTable = csv.reader(dataFile, delimiter="|")

for record in dataTable:
	for listedFile in record[2].split("; "):
		if not listedFile in fileList:
			print ("ERROR: " + listedFile)
		else:
			fileList.remove(listedFile)
			
			
print ("ERRORS: " + "	\n".join(fileList))
	
dataFile.close()

