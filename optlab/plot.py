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
    columns_to_compare: list,
    plot_optimal_trajectory = False,
    xlim = None,
    legend_loc = None
):
    """ Plots a comparison between different runs 
    
    Args;
        data: list of pandas object
        labels: labels of each pandas object in the datalist
        columns_to_compare: list of the columns that you want to plot against eachother
    """
    fig = None
    ax = None

    # Plot the reference trajectory
    if plot_optimal_trajectory == True:
        fig, ax = plot_flight(
            data_to_compare[0],
            columns = [col + "_opt" for col in columns_to_compare],
            compares = [],
            flightlabel="optimal trajectory",
            linecolor='black',
            xlim = xlim,
            legend_loc = legend_loc
        )

    for i, data in enumerate(data_to_compare):
        fig, ax = plot_flight(
            data,
            columns = columns_to_compare,
            compares = [],
            flightlabel=labels[i] + " ",
            fig=fig,
            ax=ax,
            xlim=xlim,
            legend_loc = legend_loc
        )
    return fig, ax


@optlab.debug
def plot_flight(
        data: pd.DataFrame,
        columns = ['Travel'],
        compares = ['OptTravel', 'OptPitch'],
        ylims: list = [],
        xlim = None,
        fig = None,
        ax = None,
        flightlabel = "",
        label_on = False,
        linecolor = None,
        legend_loc = None
    ):
    if fig == None and ax == None:
        # Create the figure and axes
        fig, ax = plt.subplots(nrows=len(columns), sharex=True)

    # Plot the columns
    for i, col in enumerate(columns):
        ax[i].plot(data[col], label=flightlabel, color=linecolor)

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
                    ax[i].plot(data[compares[i]], label=fligthlabel)
                except KeyError:
                    print("COMPARISON KEY ({}) for ({}) NOT PRESENT IN DATA!!!".format(
                        compares[i], col
                    ))
        except IndexError:
            pass
    
    if xlim is not None:
        plt.xlim(xlim)

    for axis in ax:
        axis.legend(loc=legend_loc)
    
    for i, axis in enumerate(ax):
        axis.set_title(columns[i])
    
    ax[-1].set_xlabel("Time [s]")
    
    return fig, ax