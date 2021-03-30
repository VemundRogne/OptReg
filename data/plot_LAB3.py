""" Plots LAB 3 """
import matplotlib.pyplot as plt
import optlab


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

optlab.plot.plot_comparisons(
    R_tests,
    R_tests_labels,
    ['Travel', 'Travelrate', 'Pitch', 'Pitchrate']
)

plt.show()