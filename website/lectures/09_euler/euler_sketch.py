from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

# Get the directory of the current file
script_dir = Path(__file__).parent

## update rcparams
plt.rcParams["mathtext.fontset"] = "custom"
plt.rcParams["mathtext.rm"] = "STIXGeneral"
plt.rcParams["mathtext.it"] = "STIXGeneral:italic"
plt.rcParams["mathtext.bf"] = "STIXGeneral:bold"
plt.rcParams["font.family"] = "STIXGeneral"
plt.rcParams["font.size"] = 12

fig, ax = plt.subplots()
# Move the left and bottom spines to x = 0 and y = 0, respectively.
ax.spines[["left", "bottom"]].set_position(("data", 0))
# Hide the top and right spines.
ax.spines[["top", "right"]].set_visible(False)

# Remove tick marks
ax.tick_params(left=False, bottom=False, labelleft=False, labelbottom=False)

# Draw arrows (as black triangles: ">k"/"^k") at the end of the axes.  In each
# case, one of the coordinates (0) is a data coordinate (i.e., y = 0 or x = 0,
# respectively) and the other one (1) is an axes coordinate (i.e., at the very
# right/top of the axes).  Also, disable clipping (clip_on=False) as the marker
# actually spills out of the Axes.
ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)

# Add axis labels near the arrows
ax.text(
    1.0,
    0.1,
    "$t$",
    transform=ax.get_yaxis_transform(),
    ha="right",
    va="top",
    fontsize=18,
)
ax.text(
    -0.05,
    1.0,
    "$y(t)$",
    transform=ax.get_xaxis_transform(),
    ha="right",
    va="bottom",
    fontsize=18,
)


def local_slope(point, x, y):
    """Calculate slope using adjacent points"""
    if point == 0 or point >= len(x) - 1:
        return 0  # Can't calculate slope at endpoints

    dx = x[point + 1] - x[point - 1]
    dy = y[point + 1] - y[point - 1]

    return dy / dx


def slope_line(point, x, y, length=10):
    fsx = x[(point - length) : (point + length)]
    fsy = y[point] + (fsx - x[point]) * local_slope(point, x, y)
    return fsx, fsy


def snapshot(fig, i):
    fig.savefig(script_dir / f"euler_sketch_{i}.png", dpi=300, bbox_inches="tight")
    return i + 1


# Some sample data.
t = np.linspace(-0.05, 1, 100)
dt_points = 7
dydt_length = 14
points_back = dydt_length - dt_points
point = 60
y = 0.05 + (t - 0.15) ** 3
fsx, fsy = slope_line(point, t, y, length=dydt_length)

# file index
i = 0

# Unknown function
ax.plot(t, y, label="Unknown function")


# Initial condition
ax.scatter(t[point], y[point], marker="o", c="k", zorder=5)

ax.scatter(t[point], 0, marker="|", c="k", zorder=5)
ax.text(
    t[point],
    -0.05,
    "$t_0$",
    transform=ax.get_xaxis_transform(),
    ha="center",
    va="bottom",
    fontsize=16,
)

i = snapshot(fig, i)

# Slope at initial condition
ax.plot(fsx, fsy, "-k", linewidth=0.5)

i = snapshot(fig, i)

# A small step
ax.scatter(t[point + dt_points], 0, marker="|", c="k", zorder=5)
ax.text(
    t[point + dt_points],
    -0.05,
    "$t_0 + \Delta t$",
    transform=ax.get_xaxis_transform(),
    ha="left",
    va="bottom",
    fontsize=16,
)

i = snapshot(fig, i)

# The prediction
ax.scatter(fsx[-points_back], fsy[-points_back], marker="x", c="r", zorder=5)

i = snapshot(fig, i)

# ax.legend()

# plt.show()
