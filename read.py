import os, csv

csv_file = open("zinc.csv", "w", encoding="utf-8", newline="\n")
writer = csv.writer(csv_file)

counts_line = ["numberOfAtoms", "numberOfBonds"] #for header

for root, dirs, files in os.walk('.'):
	for fname in files:
		full_fname = os.path.join(root, fname)
		if ".sdf" in full_fname and ".gz" not in full_fname:
			print(full_fname)
			read_file = open(full_fname, 'r')
			line_num = 0
			while True:
				line = read_file.readline()
				
				if not line:
					break

				if "ZINC" in line:
					line_num = 0
					numberOfAtoms = 0
					numberOfBonds = 0
					new_line = True
					compound = []

				line_num = line_num + 1
				line = " ".join(line.split())

				if line_num == 4:
					numberOfAtoms = int(line.split(" ")[0])
					numberOfBonds = int(line.split(" ")[1])
					
				if "END" in line or "$$$$" in line:
					new_line = False
					if len(compound) == 0:
						continue
					writer.writerow(compound)
					del compound[:]

				if new_line:

					if line_num > 4 and line_num <= numberOfAtoms + 4:
						line_split = line.split(" ")
						position_atom = line_split[:4]
						extras = [str(','.join(line_split[4:]))]
						line_split = [position_atom + extras]
						#print(line_split, ','.join(line_split))
						# line_split = position_atom + extras --> extras 만 한 컬럼에 같이 들어감

					elif line_num > numberOfAtoms + 4 and line_num <= numberOfBonds + numberOfAtoms + 4:
						line_split = line.split(" ")
						relation_atom = line_split[:3]
						extras = [','.join(line_split[3:])]
						line_split = [relation_atom + extras]

					else:
						line_split = line.split(" ")

					compound.extend(line_split)



csv_file.close()