import functools
import importlib

statenames = ['Travel', 'Travelrate', 'Pitch', 'Pitchrate', 'Elevation', 'Elevationrate']
statelabels = statenames

units = {
    "Travel": 'Rad', "Travelrate": "Rad/s",
    "Pitch": "Rad", "Pitchrate": "Rad/s",
    "Elevation": "Rad", "Elevationrate": "Rad/s",
    "u": "Pitch setpoint [Rad]"
}

LQRnames = ["u_opt", "u"]
LQRnames.extend([statename+"_opt" for statename in statenames])

LQRnames_with_elevation = ["u_opt", "e_opt", "u", "e"]
LQRnames_with_elevation.extend([statename+"_opt" for statename in statenames])

plot_basepath = "../Latex report/figures/"

def enable_pgf_plots():
    import matplotlib
    matplotlib.use("pgf")
    matplotlib.rcParams.update({
        "pgf.texsystem": "pdflatex",
        'font.family': 'serif',
        'text.usetex': True,
        'pgf.rcfonts': False,
    })
    matplotlib.rcParams['axes.unicode_minus'] = False

def debug(func):
    """Print the function signature and return value"""
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]                      # 1
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]  # 2
        signature = ", ".join(args_repr + kwargs_repr)           # 3
        print(f"Calling {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__!r} returned \r\n{value!r}")           # 4
        return value
    return wrapper_debug


import optlab.open_matfiles as open_matfiles
from optlab.open_matfiles import open_mat
import optlab.plot as plot