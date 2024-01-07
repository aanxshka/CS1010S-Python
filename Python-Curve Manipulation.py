##########
# Task 1 #
##########
def connect_ends(curve1, curve2):
    x = x_of(curve1(1)) - x_of(curve2(0))
    y = y_of(curve1(1)) - y_of(curve2(0))
    newcurve2 = translate(x,y)(curve2)
    return connect_rigidly(curve1, newcurve2)
  
#########
# Task 2 #
##########

def gosper_curve2 (level,initial_curve):
    return repeated (gosperize , level)(initial_curve)

def show_points_gosper(level, num_points, initial_curve):
    squeezed_curve = squeeze_curve_to_rect (- 0.5 , -0.5 , 1.5 , 1.5)\
                     (gosper_curve2(level, initial_curve))
    draw_points(num_points, squeezed_curve)


def your_gosper_curve_with_angle(level, angle_at_level):
    if level == 0:
        return unit_line
    else:
        return your_gosperize_with_angle(angle_at_level(level))(your_gosper_curve_with_angle(level-1, angle_at_level))


def your_gosperize_with_angle(theta):
    def inner_gosperize(curve_fn):
        return put_in_standard_position(connect_ends(rotate(theta)(curve_fn),rotate(-theta)(curve_fn)))
    return inner_gosperize

