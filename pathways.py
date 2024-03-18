import numpy as np
import matplotlib.pyplot as plt

# Dictionary to hold PES points
pes = {"I1":0.0, "TS1":20.0, "I2":-10.0, "TS2":2.0, "I3":-30.0}

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

# Create figure and remove top and right spines
fig, ax = plt.subplots()
ax.spines["right"].set_visible(False)
ax.spines["top"].set_visible(False)

# Plot PES data
plt.plot(x_dash, y_dash, linestyle = '--', linewidth = 0.75, color="black", alpha=0.4)
plt.plot(x_marker, y_marker, linestyle = '-', linewidth = 1.5, color="black")
plt.xticks([])
plt.xlabel("Reaction Coordinate", size=9)
plt.ylabel("ΔG [kcal/mol]", size=9)

# Add arrows to spines
ax.plot(0, 1, '^k', transform=ax.transAxes, clip_on=False)
ax.plot(1, 0, '>k', transform=ax.transAxes, clip_on=False)

# Annotate points with labels and relative energies
for i, label in enumerate(pes.keys()):
	plt.annotate(label, xy=(i, pes[label] + 0.25), ha="center", va="bottom", size=9)
	plt.annotate(f"{pes[label]:.1f}", xy=(i, pes[label] - 0.25), ha="center", va="top", size=9)

# Show plot
plt.show()