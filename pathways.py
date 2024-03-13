from goodvibes import GoodVibes as gv

# Call GoodVibes
#gv.main()

# Dictionary to hold PES points
pes = {}

# Flag for finding relative energies in output file
found = False

# Read GoodVibes output file (.dat)
with open("Goodvibes_output.dat") as output:
	for line in output:
		if "RXN" in line:
			next(output)
			found = True
		elif "*" in line:
			found = False
		elif found:
			pes[line.split()[1]] = float(line.split()[11])

print(pes)
		