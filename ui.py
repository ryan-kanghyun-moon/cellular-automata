import numpy as np
import ca_alg as alg


def show():
   
    surv, born = get_cond()
    plane = get_plane()

    alg.init_ca(plane)
    alg.ca(plane, surv, born)


def get_cond():
    # TODO
    maze_s = [0, 1, 1, 1, 1, 1, 0, 0, 0]
    maze_b = [0, 0, 0, 1, 0, 0, 0, 0, 0]

    mazectric_s = [0, 1, 1, 1, 1, 0, 0, 0, 0]
    mazectric_b = [0, 0, 0, 1, 0, 0, 0, 0, 0]

    life_s = [0, 0, 1, 1, 0, 0, 0, 0, 0]
    life_b = [0, 0, 0, 1, 0, 0, 0, 0, 0]


    return maze_s, maze_b


def get_plane():
    #TODO
    x = 50
    y = 80
    return np.zeros((x, y))

def visualize(plane):
    # TODO
    ret = ""
    xl = len(plane)
    yl = len(plane[1])
    
    for x in range(xl):
        for y in range(yl):
            if plane[x,y] == 0:
                ret += "X "
            else:
                ret += "  "
            
            if y == yl - 1:
                ret += '\n'
    print(ret)