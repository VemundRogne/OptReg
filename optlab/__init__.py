import functools
import importlib

statenames = ['Travel', 'Travelrate', 'Pitch', 'Pitchrate', 'Elevation', 'Elevationrate']
statelabels = statenames

units = {
    "Travel": 'Rad', "Travelrate": "Rad/s",
    "Pitch": "Rad", "Pitchrate": "Rad/s",
    "Elevation": "Rad", "Elevationrate": "Rad/s"
}

LQRnames = ["u_opt", "u_k"]
LQRnames.extend([statename+"_opt" for statename in statenames])

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