import string

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

fileURL = "http://files.docking.org/3D/"

printMolecularMenu()
molecular_weight = input("Molecular Weight(ex, A or C~F) : ") # need input molecular except code
molecular_weight = molecular_weight.upper()
printLogPMenu()
logP = input("logP(ex, A or C~F) : ")
logP = logP.upper()

print(molecular_weight, logP)

