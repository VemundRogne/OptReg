import scipy.io
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

import matplotlib
matplotlib.use("pgf")
matplotlib.rcParams.update({
    "pgf.texsystem": "pdflatex",
    'font.family': 'serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
})

import debug

@debug.debug
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


df = open_mat(file_name="LAB2/lab2_without_pitch_offset.mat", names=["Travel"])
df.plot()
plt.savefig('test_figure.pgf')
#plt.show()