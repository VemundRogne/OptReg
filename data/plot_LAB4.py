import matplotlib.pyplot as plt
import optlab


def load_tests():
    return [
        optlab.open_mat("LAB4/LQR tuning/"+path, LABn=4)
        for path in [
            "test"+str(n) for n in range(1, 17)
        ]
    ]


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


if __name__ == '__main__':
    fig, ax = plot_optimal_trajectory()
    fig.suptitle("The reference trajectory")
    optlab.plot.export_plot("LAB4_reference_trajectory")