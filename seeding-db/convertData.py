import csv

dataPath = "C:\\Projects\\icpsr\\08451-0001-Data.tsv"
outPath = "C:\\Projects\\icpsr\\icpsrData.csv"
occupationPath = "C:\\Projects\\icpsr\\occupations.txt"

dataFile = open(dataPath, "r", newline="")
data = csv.reader(dataFile, delimiter="\t")


outData = []
headList = ["id", "name", "date_execution", "age", "race", "sex", "occupation", "crime", "execution_method", "location_execution", " jurisdiction", "state", "county_conviction", "compensation_case", "icpsr_state"]
outData.append(headList)

raceLookup = ["Unknown", "White", "Black", "Native American", "Asian-Pacific Islander", "Hispanic", "Other"]
sexLookup = ["Unknown", "Male", "Female"]
crimeLookup = ["Unknown", "Murder", "Rape", "Criminal Assault", "Housebreaking-Burglary", "Horse Stealing", "Conspiracy to Murder", "Treason", "Slave Revolt", "Witchcraft", "Robbery-Murder", "Rape-Murder", "Piracy", "Accessory to Murder", "Desertion", "Robbery", "Arson", "Guerrilla Activity", "Spying-Espionage", "Murder-Rape-Robbery", "Burglary-Attempted Rape", "Rioting", "Attempted Rape", "Murder-Burglary", "Kidnapping-Murder", "Kidnapping-Murder-Robbery", "Arson-Murder", "Rape-Robbery", "Kidnapping", "Prison Break-Kidnapping", "Sodomy-Buggery-Bestiality", "Adultery", '32', "Poisoning", "34", "Concealing Birth", "Unspecified Felony", "Aid Runaway Slave", "38", "Counterfeiting", "Attempted Murder" , "Forgery" , "42", "Theft-Stealing", "Other"]
methodLookup = ["Unknown", "Hanging", "Electrocution", "Asphyxiation-Gas", "Shot", "Injection", "Pressing", "7", "Break on Wheel", "9", "Burned", "Hung in Chains", "12", "Bludgeoned", "Gibbetted", "Other"]
locationLookup = ["Unknown", "City-Local Jurisdiction", "County-Local Jurisdiction", "State-State Prison", "Other"]
jurisdictionLookup = ["Unknown", "Local-Colonial", "State", "Federal", "Territorial", "Indian Tribunal", "Other-Military"]
stateLookup = ['Unknown','Alabama','Alaska','3','Arizona','Arkansas','California','7','Colorado','Connecticut','Delaware','Washington, D.C.','Florida','Georgia','14','Hawaii','Idaho','Illinois','Indiana','Iowa','Kansas','Kentucky','Louisiana','Maine','Maryland','Massachusetts','Michigan','Minnesota','Mississippi','Missouri','Montana','Nebraska','Nevada','New Hampshire','New Jersey','New Mexico','New York','North Carolina','North Dakota','Ohio','Oklahoma','Oregon','Pennsylvania','43','Rhode Island','South Carolina','South Dakota','Tennessee','Texas','Utah','Vermont','Virginia','','Washington','West Virginia','Wisconsin','Wyoming']

occupationFile = open(occupationPath, "r", newline="")
occupationLookup = occupationFile.read().splitlines()
occupationFile.close()

def checkData(field, count):
	if len(str(field).strip()) > 0:
		if str(field).strip() != 0:
			count = count + 1
	return count

nameCount = 0
dateCount = 0
ageCount = 0
raceCount = 0
sexCount = 0
occupationCount = 0
crimeCount = 0
methodCount = 0
locationCount = 0
jurisdictionCount = 0
stateCount = 0
countyCount = 0
compCount = 0
codeCount = 0


count = 0
for line in data:
	count = count + 1
	if count > 1:
	
		nameCount = checkData(line[6], nameCount)
		dateCount = checkData(line[13], nameCount)
		ageCount = checkData(line[5], nameCount)
		raceCount = checkData(line[4], raceCount)
		sexCount = checkData(line[18], sexCount)
		occupationCount = checkData(line[20], occupationCount)
		crimeCount = checkData(line[9], crimeCount)
		methodCount = checkData(line[10], methodCount)
		locationCount = checkData(line[7], locationCount)
		jurisdictionCount = checkData(line[8], jurisdictionCount)
		stateCount = checkData(line[15], stateCount)
		countyCount = checkData(line[16], countyCount)
		compCount = checkData(line[19], compCount)
		codeCount = checkData(line[17], codeCount)
		
		#if "stinney" in line[6].lower():
			#print (line)
		name = line[6]		
		date = str(line[13])
		if len(str(line[12]).strip()) == 1:
			date = date + "-0" + str(line[12]).strip()
		elif len(str(line[12]).strip()) == 2:
			date = date + "-" + str(line[12]).strip()
		if len(str(line[11]).strip()) == 1:
			date = date + "-0" + str(line[11]).strip()
		elif len(str(line[11]).strip()) == 2:
			date = date + "-" + str(line[11]).strip()
		if len(str(line[4]).strip()) > 0:
			race = raceLookup[int(line[4])]
		else:
			race = "Unknown"
		if len(str(line[18]).strip()) > 0:
			sex = sexLookup[int(line[18])]
		else:
			sex = "Unknown"
		if len(str(line[20]).strip()) > 0:
			occupationLine = str(occupationLookup[int(line[20])])
			#print (occupationLine)
			occupation = occupationLine.split(" ")[1]
		else:
			occupation = "Unknown"
		if len(str(line[9]).strip()) > 0:
			crime = crimeLookup[int(line[9])]
		else:
			crime = "Unknown"
		if len(str(line[10]).strip()) > 0:
			executionMethod = methodLookup[int(line[10])]
		else:
			executionMethod = "Unknown"
		if len(str(line[7]).strip()) > 0:
			location = locationLookup[int(line[7])]
		else:
			location = "Unknown"
		if len(str(line[8]).strip()) > 0:
			jurisdiction = jurisdictionLookup[int(line[8])]
		else:
			jurisdiction = "Unknown"
		state = stateLookup[int(line[15])]
		
		
		if str(line[19]).strip() == "1":
			compensationCase = True
		else:
			compensationCase = False
		
		county = line[16]
		
		
		outList = [line[3], name.title(), date, line[5], race, sex, occupation, crime, executionMethod, location, jurisdiction, state, county, compensationCase, line[17]]
		
		outData.append(outList)

countList = ["Totals", nameCount, dateCount, ageCount, raceCount, sexCount, occupationCount, crimeCount, methodCount, locationCount, jurisdictionCount, stateCount, countyCount, compCount, codeCount]
outData.append(countList)
	
dataFile.close()

outFile = open(outPath, "w", newline='', encoding='utf-8')
writer = csv.writer(outFile, delimiter='|')
writer.writerows(outData)
outFile.close()