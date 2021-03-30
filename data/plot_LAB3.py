""" Plots LAB 3 """
import matplotlib.pyplot as plt
import optlab


def get_Q_metadata():
    Q_paths = ["Q_test_"+str(i)+".mat" for i in range(1, 13)]
    Q_labels = [
        "diag([0.1, 1, 1 1])",
        "diag([10, 1, 1, 1])",
        "diag([100, 1, 1, 1])",
        "diag([1, 0.1, 1, 1])",
        "diag([1, 10, 1, 1])",
        "diag([1, 100, 1, 1])",
        "diag([1, 1, 0.1, 1])",
        "diag([1, 1, 10, 1])",
        "diag([1, 1, 100, 1])",
        "diag([1, 1, 1, 0.1])",
        "diag([1, 1, 1, 10])",
        "diag([1, 1, 1, 100])"
    ]
    return Q_paths, Q_labels


def select_by_index(input_list, indexes):
    output_list = [input_list[i] for i in indexes]
    return output_list


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


def plot_different_Q_values():
    Q_paths, Q_labels = get_Q_metadata()

    # This is where we can select different runs to plot
    Q_paths = select_by_index(Q_paths, [2, 1, 0])
    Q_labels = select_by_index(Q_labels, [2, 1, 0])

    Q_tests = [
        optlab.open_mat("LAB3/"+path, LABn=3)
        for path in Q_paths
    ]

    fig, ax = optlab.plot.plot_comparisons(
        Q_tests,
        Q_labels,
        ['Travel', 'Travelrate', 'Pitch', 'Pitchrate', 'u'],
        plot_optimal_trajectory=True,
        xlim=[0, 25],
        legend_loc='right'
    )

    fig.set_size_inches(6.5, 9)

    return fig, ax


if __name__ == '__main__':
    optlab.enable_pgf_plots()
    
    #fig, ax = plot_different_R_values()
    #fig.suptitle("Effect of varying R-values in the LQR regulator")
    #optlab.plot.export_plot("LAB3_R_variations")
    
    fig, ax = plot_different_Q_values()
    fig.suptitle("Effect of varying Q-values in the LQR regulator")
    optlab.plot.export_plot("LAB3_Q_variations")
