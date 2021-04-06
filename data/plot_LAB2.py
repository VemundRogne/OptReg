import optlab

import matplotlib.pyplot as plt
import matplotlib

#matplotlib.use("pgf")
#matplotlib.rcParams.update({
#    "pgf.texsystem": "pdflatex",
#    'font.family': 'serif',
#    'text.usetex': True,
#    'pgf.rcfonts': False,
#})
#matplotlib.rcParams['axes.unicode_minus'] = False

def add_opt(df):
    df_with_opt = optlab.open_mat("LAB3/data_R0.010.mat", LABn=3)

    for col in ["Travel_opt", "Pitch_opt"]:
        df[col] = df_with_opt[col]
    return df

def plot_1():
    df = optlab.open_mat("LAB2/lab2_without_pitch_offset.mat", LABn=2)
    df = add_opt(df)

    df_2 = optlab.open_mat("LAB2/lab2_without_pitch_setpoints.mat", LABn=2)
    df_2 = add_opt(df_2)

    df_3 = df.copy(deep=True)
    df_3['Travel'] = df_3['Travel'] - (df_2['Travel'] - 3.14159)
    df_3['Pitch'] = None

    fig, ax = optlab.plot.plot_comparisons(
        [df, df_2, df_3],
        labels = [
            "Flight with optimal setpoints",
            "Flight without setpoints",
            "Compensated travel (postprocessed)"],
        columns_to_compare = ['Travel', 'Pitch'],
        xlim=(0, 30),
        #ylims=[[0, 5], None],
        plot_optimal_trajectory=True
    )
    fig.suptitle("Optimal control of pitch/travel without feedback")
    fig.set_size_inches(8, 6)
    optlab.plot.export_plot("LAB2_plot_1")

if __name__ == '__main__':
    plot_1()
    #plt.show()