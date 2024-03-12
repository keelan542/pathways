from goodvibes import GoodVibes as gv

# Call GoodVibes
#gv.main()

# Dictionary to hold PES points
pes = {}

# Read GoodVibes output file (.dat)
with open("Goodvibes_output.dat") as output:
	for line in output:
		print(line)