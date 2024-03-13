from goodvibes import GoodVibes as gv
import numpy as np
import matplotlib.pyplot as plt

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

# Length of pes dictionary
len_pes = len(pes)

# Amount to offset by on x-axis
x_gap = 0.2

# Data to plot
x = np.arange(len_pes)
y = np.array(list(pes.values()))