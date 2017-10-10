from archives_tools import aspace as AS
import os
import csv

__location__ = os.path.dirname(os.path.realpath(__file__))

s = AS.getSession()
repo = "2"

#IndexCards
aspaceData = []

parent = AS.getArchObjID(s, repo, "28851bea92e4ac4dee5e6f03f600623b")
print (parent.title)
childCount = 0
subseries = AS.getChildren(s, parent)
for sub in subseries.children:
	print (sub.title)
	for child in sub.children:
		
		childObj = AS.getArchObj(s, child.record_uri)
		childCount += 1
		print ("	" + childObj.title)
		#B02_F001
		box = childObj.instances[0].container.indicator_1.split(" ")[0]
		folder = childObj.instances[0].container.indicator_2
	
		if len(box) == 1:
			box = "B0" + box
		else:
			box = "B" + box
			
		if len(folder) == 1:
			folder = "F00" + folder
		elif len(folder) == 2:
			folder = "F0" + folder
		else:
			folder = "F" + folder
			
		aspaceData.append([box + "_" + folder, childObj.ref_id,  childObj.title])
	
#write data to file
csvOut = open(os.path.join(__location__, "aspaceS2.csv"), "w", newline='', encoding='utf-8')
writer = csv.writer(csvOut, delimiter='|')
writer.writerows(aspaceData)
csvOut.close()