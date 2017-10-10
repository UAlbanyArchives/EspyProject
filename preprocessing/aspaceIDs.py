from archives_tools import aspace as AS
import os
import csv

__location__ = os.path.dirname(os.path.realpath(__file__))

s = AS.getSession()
repo = "2"

#IndexCards
aspaceData = []

parent = AS.getArchObjID(s, repo, "9cede46816f600a9ea55232e2bcac9fb")
print (parent.title)
childCount = 0
children = AS.getChildren(s, parent)
for child in children.children:

	childObj = AS.getArchObj(s, child.record_uri)
	print (childObj.title)
	childCount += 1
	if childCount < 10:
		start = "B0"
	else:
		start = "B"
	aspaceData.append([start + str(childCount), childObj.ref_id])
	
#write data to file
csvOut = open(os.path.join(__location__, "aspaceS1.csv"), "w", newline='', encoding='utf-8')
writer = csv.writer(csvOut, delimiter='|')
writer.writerows(aspaceData)
csvOut.close()