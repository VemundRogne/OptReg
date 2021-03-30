""" Plots LAB 3 """
import matplotlib.pyplot as plt
import optlab


def plot_different_R_values():
    R_tests = [
        optlab.open_mat("LAB3/"+path, LABn=3)
        for path in [
            "data_R0.010.mat",
            "data_R0.100.mat",
            "data_R1.000.mat",
            "data_R10.000.mat"
        ]
    ]
    R_tests_labels = ["R=0.01", "R=0.10", "R=1.0", "R=10"]

    fig, ax = optlab.plot.plot_comparisons(
        R_tests,
        R_tests_labels,
        ['Travel', 'Travelrate', 'Pitch', 'Pitchrate', 'u'],
        plot_optimal_trajectory=True,
        xlim=[0, 25],
        legend_loc='right'
    )

    fig.set_size_inches(6.5, 9)

    return fig, ax


if __name__ == '__main__':
    optlab.enable_pgf_plots()
    fig, ax = plot_different_R_values()
    fig.suptitle("Effect of varying R-values in the LQR regulator")
    optlab.plot.export_plot("LAB3_R_variations")
