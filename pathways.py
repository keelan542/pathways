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

# Dashed line
x_dash = np.empty(len_pes * 2)
for i in range(len_pes):
    x_dash[i * 2 + 0] = x[i] - x_gap
    x_dash[i * 2 + 1] = x[i] + x_gap
y_dash = np.repeat(y, 2)

# Marker
x_marker = np.empty(len_pes * 3)
for i in range(len_pes):
    x_marker[i * 3 + 0] = x[i] - x_gap
    x_marker[i * 3 + 1] = x[i] + x_gap
    x_marker[i * 3 + 2] = None
y_marker = np.repeat(y, 3)

# Plot potential energy surface
fig = plt.figure(figsize=(8, 6))
plt.plot(x_dash, y_dash, linestyle = '--', linewidth = 0.75, color="black", alpha=0.4)
plt.plot(x_marker, y_marker, linestyle = '-', linewidth = 1.5, color="black")
plt.xticks([])
plt.xlabel("Reaction Coordinate")
plt.ylabel("ΔG [kcal/mol]")

# Annotate points with species labels
for i, label in enumerate(pes.keys()):
	plt.annotate(label, xy=(i, pes[label]), ha="center", va="bottom")
	plt.annotate(f"{pes[label]:.1f}", xy=(i, pes[label]), ha="center", va="top")

# Show plot
plt.show()