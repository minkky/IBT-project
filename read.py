import os, csv

csv_file = open("zinc.csv", "w", encoding="utf-8", newline="\n")
writer = csv.writer(csv_file)

for root, dirs, files in os.walk('.'):
	for fname in files:
		full_fname = os.path.join(root, fname)
		if ".sdf" in full_fname and ".gz" not in full_fname:
			print(full_fname)
			read_file = open(full_fname, 'r')
			while True:
				line = read_file.readline()
				
				if not line:
					break

				if "ZINC" in line:
					new_line = True
					compound = []
				
				line = " ".join(line.split())

				if "END" in line or "$$$$" in line:
					new_line = False
					if len(compound) == 0:
						continue
					writer.writerow(compound)
					del compound[:]

				if new_line:
					compound.extend(line.split(" "))



csv_file.close()