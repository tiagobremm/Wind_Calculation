import numpy as np


class WindCalculator:
    """
    All speeds must be in m/s
    The direction must be in degrees
    The equations are implemented for the meteorological method, where the direction is given by where the wind
    is coming from.
    EX: if wind direction is east, wind_dir = 90, u_ms = -1, v_ms = 0.
    In the 2D Cartesian plane, "u" represents the x axis and "v" the y axis. If u_ms = -1, the wind blows in the
    negative direction of u axis.
    Comparison Values:
    u_ms = -3.19
    v_ms = 1.16
    wind_dir = 110
    mean_wind_ms = 3.39
    REFERENCES: https://www.eol.ucar.edu/content/wind-direction-quick-reference
    """

    def __init__(self):
        self.rad_degree = np.pi / 180
        self.deg_rad = 180 / np.pi

    def wind_direction(self, u_ms, v_ms):
        wind_dir1 = np.arctan2(-v_ms, -u_ms) * self.deg_rad
        wind_dir = 270 - (np.arctan2(v_ms, u_ms) * self.deg_rad)

        return round(wind_dir, 2)

    def wind_component_speed(self, wind_speed_ms, wind_dir):
        u_ms = - wind_speed_ms * (np.sin(wind_dir * self.rad_degree))
        v_ms = - wind_speed_ms * (np.cos(wind_dir * self.rad_degree))

        return round(u_ms, 2), round(v_ms, 2)

    @staticmethod
    def mean_wind_speed(u_ms, v_ms):
        mean_wind_ms = np.sqrt((u_ms ** 2) + (v_ms ** 2))

        return round(mean_wind_ms, 2)


## Apply over array
calc = WindCalculator()

calc.mean_wind_speed(-3.19, 1.16)
calc.wind_component_speed(3.4, 110)
calc.wind_direction(-3.19, 1.16)
calc.wind_direction(-1, 0)

## How to apply over array with multiple lines
test = np.vectorize(calc.wind_direction)
u_s = np.array([fluxos.u_unrot])
v_s = np.array([fluxos.v_unrot])

dir_vento = test(u_s, v_s)


