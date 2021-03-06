import matplotlib.pyplot as plt
import optlab


def load_tests():
    return [
        optlab.open_mat("LAB4/LQR tuning/"+path, LABn=4)
        for path in [
            "test"+str(n) for n in range(1, 17)
        ]
    ]


def plot_tunings():
    tests = load_tests()

    fig, ax = plt.subplots(nrows=3, ncols=2, sharex=True)
    ax = list(ax.flatten())

    fig, ax = optlab.plot.plot_comparisons(
        data_to_compare = [
            #tests[12],
            #tests[13],
            tests[14],
            #tests[15],
        ],
        columns_to_compare=["Travel", "Travelrate", "Pitch", "Pitchrate", "Elevation", "Elevationrate"],
        labels = [
            #"Q = diag([50,1,1,1,50,1])",
            #"Q = diag([15,1,1,1,15,1])",
            "Q = diag([15,1,0.1,1,15,1])",
            #"Q = diag([15,1,10,1,15,1])"
        ],
        plot_optimal_trajectory=True,
        xlim=[0, 22.5],
        fig = fig,
        ax = ax,
        forced_xlabel_loc=[4],
        legend_ncols=4
    )

    fig.set_size_inches(12, 9)

    return fig, ax


def plot_optimal_trajectory():
    tests = load_tests()

    fig, ax = plt.subplots(nrows=3, ncols=2, sharex=True)
    ax = list(ax.flatten())

    fig, ax = optlab.plot.plot_comparisons(
        data_to_compare = [tests[5]],
        columns_to_compare=["Travel", "Travelrate", "Pitch", "Pitchrate", "Elevation", "Elevationrate"],
        labels = ["Hello, world! <3"],
        plot_optimal_trajectory=True,
        plot_only_optimal_trajectory=True,
        xlim=[2.5, 17.5],
        fig = fig,
        ax = ax,
        forced_xlabel_loc=[4]
    )

    fig.set_size_inches(11, 8)

    return fig, ax


def plot_different_travel_gains():
    tests = load_tests()

    fig, ax = plt.subplots(nrows=3, ncols=2, sharex=True)
    ax = list(ax.flatten())

    fig, ax = optlab.plot.plot_comparisons(
        data_to_compare = [
            tests[10],
            tests[9],
            tests[3],
            tests[2],
            tests[1],
            tests[0],
        ],
        columns_to_compare=["Travel", "Travelrate", "Pitch", "Pitchrate", "Elevation", "Elevationrate"],
        labels = [
            "Q = diag([1000, ...]",
            "Q = diag([50, ...]",
            "Q = diag([15, ...]",
            "Q = diag([10, ...]",
            "Q = diag([5, ...]",
            "Q = diag([1, ...]",
        ],
        plot_optimal_trajectory=True,
        xlim=[0, 22.5],
        fig = fig,
        ax = ax,
        forced_xlabel_loc=[4],
        legend_ncols=4
    )

    fig.set_size_inches(12, 9)

    return fig, ax

def plot_different_elevation_gains():
    tests = load_tests()

    fig, ax = plt.subplots(nrows=3, ncols=2, sharex=True)
    ax = list(ax.flatten())

    fig, ax = optlab.plot.plot_comparisons(
        data_to_compare = [
            tests[3],
            tests[4],
            tests[5],
            tests[6],
            tests[7],
            tests[8],
        ],
        columns_to_compare=["Travel", "Travelrate", "Pitch", "Pitchrate", "Elevation", "Elevationrate"],
        labels = [
            "Q = diag([15,...,1,...]",
            "Q = diag([15,...,5,...]",
            "Q = diag([15,...,10,...]",
            "Q = diag([15,...,15,...]",
            "Q = diag([15,...,20,...]",
            "Q = diag([15,...,50,...]",
        ],
        plot_optimal_trajectory=True,
        xlim=[5, 15],
        fig = fig,
        ax = ax,
        forced_xlabel_loc=[4],
        legend_ncols=4
    )

    ax[4].set_ylim((-0.1,0.2))

    fig.set_size_inches(12, 9)

    return fig, ax

if __name__ == '__main__':
    #fig, ax = plot_optimal_trajectory()
    #fig.suptitle("The reference trajectory")
    #optlab.plot.export_plot("LAB4_reference_trajectory")

    #fig, ax = plot_different_travel_gains()
    #fig.suptitle("Different travel-gains")
    #optlab.plot.export_plot("LAB4_travel_gains", rect=(0,0.05, 1, 1))

    #fig, ax = plot_tunings()
    #fig.suptitle("Best tuning of the helicopter in LAB4")
    #optlab.plot.export_plot("LAB4_best_tunings", rect=(0, 0.05, 1, 1))

    fig, ax = plot_different_elevation_gains()
    fig.suptitle("Different elevation-gains")
    optlab.plot.export_plot("LAB4_elevation_gains", rect=(0,0.05, 1, 1))
