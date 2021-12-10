# Wind_Calculation
Calculation of wind direction, U and V components and average wind speed. 

If you want to adapt the code to another software, make sure he uses the programming language convention: atan2(y,x) needs to return the arctangent of y/x.
Spreadsheets, including Microsoft Excel, LibreOffice Calc and Google Docs switch the arguments, so that atan2(x,y) is the arctangent of y/x (most details are described in the reference). To test it, compute atan2(1,-1). If the result is 2.36 radians (135 degrees) you can use these formulas unchanged.

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
