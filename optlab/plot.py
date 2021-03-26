import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

import optlab

def export_plot(
        plotname,
        basepath: str = optlab.plot_basepath
    ):
    plt.tight_layout()

    if plotname[-4:] != ".pgf":
        plotname = plotname + ".pgf"

    plt.savefig(basepath+plotname)

@optlab.debug
def plot_comparisons(
    data_to_compare: list,
    labels: list,
    columns_to_compare: list
):
    """ Plots a comparison between different runs 
    
    Args;
        data: list of pandas object
        labels: labels of each pandas object in the datalist
        columns_to_compare: list of the columns that you want to plot against eachother
    """

    fig, ax = plt.subplots(len(columns_to_compare), 1)
    for data_i, data in enumerate(data_to_compare):
        for col_n, column in enumerate(columns_to_compare):
            ax[col_n].plot(
                data[column], label=labels[data_i]
            )
    
    ax[0].legend()


def plot_flight(
        data: pd.DataFrame,
        columns = ['Travel'],
        compares = ['OptTravel', 'OptPitch'],
        ylims: list = [],
        xlim = None,
    ):
    # Create the figure and axes
    fig, ax = plt.subplots(nrows=len(columns), sharex=True)

    # Plot the columns
    for i, col in enumerate(columns):
        ax[i].plot(data[col], label=col)
        ax[i].set_xlabel("Time [s]")

        # Add ylabel if it exist in the units
        if col in optlab.units:
            ax[i].set_ylabel(optlab.units[col])

        # Add ylim if it exists
        try:
            if ylims[i] is not None:
                ax[i].set_ylim(ylims[i])
        except IndexError:
            pass

        # Plot the comparison, if it exists.
        try:
            if compares[i]:
                try:
                    ax[i].plot(data[compares[i]], label=compares[i])
                except KeyError:
                    print("COMPARISON KEY ({}) for ({}) NOT PRESENT IN DATA!!!".format(
                        compares[i], col
                    ))
        except IndexError:
            pass
    
    if xlim is not None:
        plt.xlim(xlim)

    for axis in ax:
        axis.legend()
    
    return fig, ax