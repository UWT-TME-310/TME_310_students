from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def import_log_file(log_file):
    """
    Import pile-driving log data from a CSV file.

    Reads pile identification, final tip elevation, and driving data
    (depth, BPM, BPF) from a formatted pile-driving log file.

    Parameters
    ----------
    log_file : str or Path
        Path to the pile-driving log CSV file. File should have pile ID
        on line 1, final tip elevation on line 2, and data starting at
        line 5 with columns: depth, BPM, BPF.

    Returns
    -------
    pile_id : str
        Pile identification string.
    elevation : ndarray
        Array of elevations in feet, calculated from depth measurements.
    bpm : ndarray
        Array of blows per minute values.
    bpf : ndarray
        Array of blows per foot values.
    """
    with open(log_file, "r") as f:
        pile_id = f.readline().strip().split(",")[1]
        final_tip_elevation = float(f.readline().strip().split(",")[1])
    data = np.loadtxt(log_file, delimiter=",", skiprows=4)
    depth = data[:, 0]
    elevation = final_tip_elevation + depth[-1] - depth
    bpm = data[:, 1]
    bpf = data[:, 2]
    return pile_id, elevation, bpm, bpf


def bpm_to_stroke(bpm):
    """
    Convert blows per minute to hammer fall height.

    Calculates the hammer stroke (fall height) based on the driving rate,
    assuming the hammer is in free fall between blows.

    Parameters
    ----------
    bpm : float or ndarray
        Blows per minute (driving rate).

    Returns
    -------
    float or ndarray
        Hammer fall height in feet.

    Notes
    -----
    The calculation assumes:
    - Hammer is in free fall between blows
    - Half the time between blows is spent falling
    - Gravitational acceleration g = 32.2 ft/s²
    - Uses kinematic equation: h = (1/2)gt²
    """
    g = 32.2  # feet/second/second
    time_between_blows = (
        60 / bpm
    )  # seconds (60 (seconds/minute)/(blows/minute) --> seconds/blow
    height = g / 2 * (time_between_blows / 2) ** 2  # feet
    return height


def s0_pile_capacity(bpf, fall_height, w, a, length, area, mod):
    """
    Calculate pile capacity using the S₀ equation.

    Estimates pile ultimate capacity based on driving resistance and
    pile/hammer properties using a simplified wave equation approach.

    Parameters
    ----------
    bpf : float or ndarray
        Blows per foot (driving resistance).
    fall_height : float or ndarray
        Hammer fall height in feet.
    w : float
        Hammer weight in pounds.
    a : float
        Hammer efficiency (dimensionless, typically 0.3-0.5).
    length : float
        Pile length in feet.
    area : float
        Pile cross-sectional area in square inches.
    mod : float
        Pile modulus of elasticity in psi.

    Returns
    -------
    float or ndarray
        Estimated pile capacity in pounds.

    Notes
    -----
    The S₀ equation accounts for:
    - Hammer energy transfer
    - Pile elastic compression
    - Driving resistance (set per blow)

    The equation is: Q = (a * h * W) / (s + s₀)
    where s₀ = sqrt((a * h * W * L) / (2 * A * E))
    """
    pile_set = 1 / bpf
    s0 = np.sqrt((a * fall_height * w * length) / (2 * area * mod))
    capacity = (a * fall_height * w) / (pile_set + s0)
    return capacity


def run_analysis(
    log_file,
    hammer_weight=20_000,
    hammer_efficiency=0.4,
    pile_length=150,
    pile_area=477,
    modulus=6_000_000,
    summary=False,
):
    """
    Perform complete pile-driving analysis from log file.

    Imports pile-driving log data, calculates hammer stroke heights,
    estimates pile capacity, and optionally prints a summary.

    Parameters
    ----------
    log_file : str or Path
        Path to the pile-driving log CSV file.
    hammer_weight : float, optional
        Hammer weight in pounds. Default is 20,000.
    hammer_efficiency : float, optional
        Hammer efficiency (dimensionless, 0-1). Default is 0.4.
    pile_length : float, optional
        Pile length in feet. Default is 150.
    pile_area : float, optional
        Pile cross-sectional area in square inches. Default is 477.
    modulus : float, optional
        Pile modulus of elasticity in psi. Default is 6,000,000.
    summary : bool, optional
        If True, print a text summary of results. Default is False.

    Returns
    -------
    pile_id : str
        Pile identification string.
    elevation : ndarray
        Array of elevations in feet.
    bpm : ndarray
        Array of blows per minute values.
    bpf : ndarray
        Array of blows per foot values.
    q : ndarray
        Array of estimated pile capacities in pounds.
    """
    pile_id, elevation, bpm, bpf = import_log_file(log_file)
    height = bpm_to_stroke(bpm)
    q = s0_pile_capacity(
        bpf,
        fall_height=height,
        w=hammer_weight,
        a=hammer_efficiency,
        length=pile_length,
        area=pile_area,
        mod=modulus,
    )
    if summary:
        print("\nPile installation summary")
        print("-" * 40)
        print(f"{'Pile ID:':<20} {pile_id:>6}")
        print(f"{'Final tip elevation:':<20} {elevation[-1]:>8.1f} {'feet':>6}")
        print(f"{'Pile capacity:':<20} {q[-1] / 1000:>6.0f} {'kips':>8}")
        print("-" * 40)
    return pile_id, elevation, bpm, bpf, q


def pile_plot(pile_id, elevation, bpm, bpf, q):
    """
    Create visualization of pile-driving analysis results.

    Generates a two-panel plot showing driving performance (BPM and BPF)
    and estimated pile capacity versus elevation.

    Parameters
    ----------
    pile_id : str
        Pile identification string for plot title.
    elevation : ndarray
        Array of elevations in feet.
    bpm : ndarray
        Array of blows per minute values.
    bpf : ndarray
        Array of blows per foot values.
    q : ndarray
        Array of estimated pile capacities in pounds.

    Returns
    -------
    None
        Displays the plot using matplotlib.

    Notes
    -----
    The plot includes:
    - Left panel: BPM (bottom x-axis) and BPF (top x-axis) vs elevation
    - Right panel: Pile capacity in kips vs elevation
    - Both panels share the same y-axis (elevation in feet)
    """
    # Create figure
    fig, ax = plt.subplots(nrows=1, ncols=2, dpi=300)
    log_ax = ax[0]
    q_ax = ax[1]

    # Plot BPM on primary axis (bottom)
    log_ax.plot(bpm, elevation, label="BPM", color="tab:red", alpha=0.7)
    log_ax.set_xlabel("Blows per minute (BPM)")
    log_ax.set_ylabel("Elevation (ft)")

    # Create twin axis for BPF (top)
    log_ax_top = log_ax.twiny()
    log_ax_top.plot(bpf, elevation, label="BPF", color="tab:blue")
    log_ax_top.set_xlabel("Blows per foot (BPF)")

    # Plot capacity
    q_ax.plot(q / 1000, elevation, label=pile_id, color="tab:green")
    q_ax.xaxis.tick_top()
    q_ax.xaxis.set_label_position("top")
    q_ax.set_xlabel("Capacity (kips)")
    q_ax.set_ylabel("Elevation (ft)")
    q_ax.set_xlim(left=0)

    # Add grid
    log_ax.grid()
    q_ax.grid()

    # Add legend combining both lines
    lines1, labels1 = log_ax_top.get_legend_handles_labels()
    lines2, labels2 = log_ax.get_legend_handles_labels()
    log_ax.legend(
        lines1 + lines2, labels1 + labels2, bbox_to_anchor=(0.85, 1), loc="best"
    )

    fig.suptitle(f"Pile Analysis: {pile_id}")

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    cwd = Path.cwd()
    log_file = cwd / "sample_pile_log_01.csv"
    pile_id, elevation, bpm, bpf, q = run_analysis(log_file)
    pile_plot(pile_id, elevation, bpm, bpf, q)
