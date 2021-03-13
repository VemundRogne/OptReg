import scipy.io
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

import matplotlib
#matplotlib.use("pgf")
#matplotlib.rcParams.update({
#    "pgf.texsystem": "pdflatex",
#    'font.family': 'serif',
#    'text.usetex': True,
#    'pgf.rcfonts': False,
#})

import optlab

@optlab.debug
def open_mat(
        file_name: str,
        names: list = ['Travel', 'Travelrate', 'Pitch', 'Pitchrate', 'Elevation', 'Elevationrate'],
        names_ext: list = []
    ) -> pd.DataFrame:
    """ Opens a .mat file into a DataFrame 

    Args:
        file_name: str - path to the file
        names: list - colum names to use in the DataFrame. They are used in order
    
    Returns:
        df: DataFrame
    """
    names.extend(names_ext)
    mat = scipy.io.loadmat(file_name=file_name)
    mat = mat['ans']
    mat = np.transpose(mat)
    
    df = pd.DataFrame(data = mat[:, 1:], index = mat[:, 0])
    df.index.name = "time [s]"

    # Rename each column to the names provided
    for i in range(0, len(names)):
        df = df.rename(columns={i: names[i]})

    return df


if __name__ == '__main__':
    df = open_mat(file_name="data/Q_test_12.mat", names_ext=["u_opt", "u_used", 'opt_travel', 'opt_travelrate', 'opt_pitch', 'opt_pitchrate'])
    df.plot(y=["opt_travel", "Travel"])
    #plt.savefig('test_figure.pgf')
    plt.show()