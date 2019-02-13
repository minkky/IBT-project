import string, os, sys

def printDash():
	print("\n=================================\n")

def printMolecularMenu():
	printDash()
	print("Molecular Weight(up to) 입력하세요.")
	index = -1
	weight = 150
	while index < 10:
		weight = weight + 50 if weight < 300 or weight >= 450 else weight + 25
		index = index + 1
		if index == 10:
			print("\t" + string.ascii_uppercase[index], ":", weight-50,"~")
			break
		print("\t" + string.ascii_uppercase[index], ": ~", weight)
	printDash()

def printLogPMenu():
	printDash()
	print("logP(up to) 입력하세요.")
	logp = -2.0
	index = -1
	while logp < 6 :
		logp = logp + 1 if logp < 2 else logp + 0.5
		index = index + 1
		if logp == 5.5:
			print("\t", string.ascii_uppercase[index], ":", logp-0.5,"~")
			break
		print("\t", string.ascii_uppercase[index], ":", logp)
	printDash()

def getRangeLetter(letter):
	letters = []
	if len(letter.split("~")) == 1:
		letters.append(letter)
	else:
		start = ord(letter.split("~")[0])
		end  = ord(letter.split("~")[1])
		
		while start <= end:
			letters.append(chr(start))
			start = start + 1
	return letters

def printMenuWithMeaning(alpha, meaning):
	printDash()
	for index, mean in zip(alpha, meaning):
		print("\t" + index, ":", mean)
	printDash()

fileURL = "http://files.docking.org/3D/"

printMolecularMenu()
molecular_weight = input("Molecular Weight(ex, A or C~F) : ") # need input molecular except code
molecular_weight = molecular_weight.upper()
printLogPMenu()
logP = input("logP(ex, A or C~F) : ").upper()
print()

firstLetter = getRangeLetter(molecular_weight)
secondLetter = getRangeLetter(logP)
thirdLetter = ["A", "B", "C", "E", "G", "I"] # reactivity - E is standard(default)
fourthLetter = ["A", "B", "C", "D", "E", "F"] #  purchasability - D is Wait OK(default)
fifthLetter = ["H", "L", "M", "R"] # pH range
sixthLetter = ["L", "M", "N", "O", "P"] # net molecular charge
thirdMeaning = ["anodyne", "Bother", "clean", "mild reactivity", "reactivity ok", "hot chemistry ok"]
fourthMeaning = ["in stock", "in stock", "in stock via agent", "make on demand", "boutique", "annotated"]
fifthMeaning = ["ref (7.4)", "mid (near 7.4)", "low (around 6.4)", "high (around 8.4)"]
sixthMeaning = ["neutral", "minus", "minus 2", "plus 1", "plus 2"]


printMenuWithMeaning(thirdLetter, thirdMeaning)
third = input("reactivity(E is default) : ").upper()
thirdLetter = thirdLetter[:thirdLetter.index(third)+1]

printMenuWithMeaning(fourthLetter, fourthMeaning)
fourth = input("purchasability(D is default) : ").upper()
fourthLetter = fourthLetter[:fourthLetter.index(fourth)+1]

printMenuWithMeaning(fifthLetter, fifthMeaning)
fifth = input("pH range(R, M is default) : ").upper()
fifthLetter = [x.strip() for x in fifth.split(",")]

printMenuWithMeaning(sixthLetter, sixthMeaning)
sixth = input("net molecular charge(default is All) : ").upper()
if sixth != "ALL":
	sixthLetter = [x.strip() for x in sixth.split(",")]

substances = []
subsets = []

for first in firstLetter:
	for second in secondLetter:
		substances.append(first + second)

for third in thirdLetter:
	for fourth in fourthLetter:
		for fifth in fifthLetter:
			for sixth in sixthLetter:
				subsets.append(third +  fourth + fifth + sixth)

dir_name = "zinc/"
extension = ".xaa.sdf.gz "
url = "http://files.docking.org/3D/"
cmd = "curl --remote-time --fail --create-dirs -o "

for substance in substances:
	for subset in subsets:
		command = cmd + dir_name + substance+subset+extension + url + substance+"/" + subset+"/"+substance+subset+extension
		os.system(command)
		#print(command)