
# -------------
# gosper_curve:
# -------------
# write down and invoke the function that you are using for this testing
# in the space below

#print(profile_fn(lambda: gosper_curve(10)(0.1), 50))

# Time measurements
t1 = 3.3800
t2 = 3.5425
t3 = 4.1213
t4 = 3.4233
t5 = 2.9558
tavg = 3.4846
#  <...do for at least 5 times and take the average...>


# ------------------------
# gosper_curve_with_angle:
# ------------------------
# write down and invoke the function that you are using for this testing
# in the space below

#print(profile_fn(lambda: gosper_curve_with_angle(10,lambda lvl:pi/4)(0.1), 50))

# Time measurements
t1 = 3.2079
t2 = 3.2364
t3 = 3.3642
t4 = 4.1010
t5 = 2.1152
tavg = 3.2049
#  <...do for at least 5 times and take the average...>

#
# -----------------------------
# your_gosper_curve_with_angle:
# -----------------------------
# write down and invoke the function that you are using for this testing
# in the space below

def your_gosperize_with_angle(theta):
    def inner_gosperize(curve_fn):
        return put_in_standard_position(connect_ends(rotate(theta)(curve_fn),rotate(-theta)(curve_fn)))
    return inner_gosperize

def your_gosper_curve_with_angle(level, angle_at_level):
    if level == 0:
        return unit_line
    else:
        return your_gosperize_with_angle(angle_at_level(level))(your_gosper_curve_with_angle(level-1, angle_at_level))

#print(profile_fn(lambda: your_gosper_curve_with_angle(10,lambda lvl:pi/4)(0.1), 50))

# Time measurements
t1 = 43.0407
t2 = 37.3377
t3 = 38.0942
t4 = 42.5318
t5 = 42.6790
tavg = 40.7367
#  <...do for at least 5 times and take the average...>


# Conclusion:
'''
As the time taken for the customisable your_gosper_curve_with_angle function to run is significantly
higher than thetimings for the customised function (40 >> 3), the customised functions have a
significant speed advantage to the customisable function.
'''

from diagnostic import *
from hi_graph_connect_ends import *
original_rotate = rotate
replace_fn(rotate, original_rotate)
trace(x_of)
x_of(gosper_curve(1)(0.5))
untrace(x_of)
x_of(gosper_curve(1)(0.5))
replace_fn(rotate, joe_rotate)
trace(x_of)
x_of(gosper_curve(1)(0.5))
untrace(x_of)
x_of(gosper_curve(1)(0.5))
#
# Fill in this table:
#
#                    level      rotate       joe_rotate
#                      1          3             4
#                      2          5            10
#                      3          7            22
#                      4          9            46
#                      5          11           94
#
#  Evidence of exponential growth in joe_rotate.

