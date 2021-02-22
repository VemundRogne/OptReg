import scipy.io
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import debug

@debug.debug
def open_mat(
        file_name: str,
        names: list = None,
    ) -> pd.DataFrame:
    """ Opens a .mat file into a DataFrame 

    Args:
        file_name: str - path to the file
        names: list - colum names to use in the DataFrame. They are used in order
    
    Returns:
        df: DataFrame
    """
    mat = scipy.io.loadmat(file_name=file_name)
    mat = mat['ans']
    mat = np.transpose(mat)
    
    print(mat[:, 0])
    df = pd.DataFrame(data = mat[:, 1:], index = mat[:, 0])
    df.index.name = "time [s]"

    # Rename each column to the names provided
    for i in range(0, len(names)):
        df = df.rename(columns={i: names[i]})

    return df


df = open_mat(file_name="LAB2/lab2_without_pitch_offset.mat", names=["Travel"])
df.plot()
plt.show()