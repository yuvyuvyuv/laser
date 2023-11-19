d = 0.475
""" TODO: range between laser and camera, in meters """


def get_range(center_x, laser_x):

    # 11.5/28.5 + diff
    diff = 0.071
    magic = 1
    q = laser_x/center_x
    if q == 1:
        return 0
    print(q)
    final_dist_to_wall = d/((1-q)*(11.5/28.5)+diff)
    # 11.5/28.5 is the tan of half of camera opening
    return final_dist_to_wall


