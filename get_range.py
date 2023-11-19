d = 0.475  # TODO: measure d
""" TODO: range between laser and camera, in meters """


def get_range(center_x, laser_x):
    q = laser_x/center_x
    final_dist_to_wall = d/(1-q)*(11.5/28.5)
    # 11.5/28.5 is the tan of half of camera opening
    return final_dist_to_wall


