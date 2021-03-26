import optlab

import matplotlib.pyplot as plt
import matplotlib

matplotlib.use("pgf")
matplotlib.rcParams.update({
    "pgf.texsystem": "pdflatex",
    'font.family': 'serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
})
matplotlib.rcParams['axes.unicode_minus'] = False

def plot_1():
    df = optlab.open_mat("LAB2/lab2_without_pitch_offset.mat", LABn=2)
    fig, ax = optlab.plot.plot_flight(
        df,
        columns = ['Travel', 'Pitch'],
        xlim=(0, 30),
        ylims=[[0, 5], None]
    )
    fig.suptitle("Optimal control of pitch/travel without feedback")
    optlab.plot.export_plot("LAB2_plot_1")

if __name__ == '__main__':
    plot_1()