import numpy as np
import matplotlib.pyplot as plt

def plot_pes(pes_arr, same_ref=False):
    # Create figure and remove top and right spines
    fig, ax = plt.subplots()
    ax.spines["right"].set_visible(False)
    ax.spines["top"].set_visible(False)

    # Add arrows to spines
    ax.plot(0, 1, '^k', transform=ax.transAxes, clip_on=False)
    ax.plot(1, 0, '>k', transform=ax.transAxes, clip_on=False)
    
    # Axes labels
    plt.xticks([])
    plt.xlabel("Reaction Coordinate", size=9)
    plt.ylabel("ΔG [kcal/mol]", size=9)

    # Amount to offset by on x-axis
    x_gap = 0.2

    for i,surface in enumerate(pes_arr):
        print(i)
        len_pes = len(surface)

        # Data to plot
        x = np.arange(len_pes)
        y = np.array(list(surface.values()))

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

        # Plot PES data
        if same_ref and i != 0:
            plt.plot(x_dash[0], y_dash[0], linestyle = '--', linewidth = 0.75, color="black", alpha=0.0)
            plt.plot(x_marker[0], y_marker[0], linestyle = '-', linewidth = 1.5, color="black", alpha=0.0)
            plt.plot(x_dash[1:], y_dash[1:], linestyle = '--', linewidth = 0.75, color="black", alpha=0.4)
            plt.plot(x_marker[1:], y_marker[1:], linestyle = '-', linewidth = 1.5, color="black")
        elif i == 0:
            plt.plot(x_dash, y_dash, linestyle = '--', linewidth = 0.75, color="black", alpha=0.4)
            plt.plot(x_marker, y_marker, linestyle = '-', linewidth = 1.5, color="black")

        # Annotate points with labels and relative energies
        for i, label in enumerate(surface.keys()):
        	plt.annotate(label, xy=(i, surface[label] + 0.25), ha="center", va="bottom", size=9)
        	plt.annotate(f"{surface[label]:.1f}", xy=(i, surface[label] - 0.25), ha="center", va="top", size=9)

    # Show plot
    plt.show()

# Dictionary to hold PES points
pes = [{"R":0.0, "TS1":20.0, "I2":-10.0, "TS2":2.0, "P":-30.0},{"R2":0.0, "TS1":30.0, "I2":-15.0, "TS2":10.0, "P":-20.0}]

# Calling plotting function
plot_pes(pes, same_ref=True)