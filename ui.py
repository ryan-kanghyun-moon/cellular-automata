import numpy as np
def get_surv():
    # TODO
    maze = [1, 1, 1, 1, 1, 0, 0, 0]
    life = [0, 1, 1, 0, 0, 0, 0, 0]
    return maze

def get_born():
    # TODO
    maze = [0, 0, 1, 0, 0, 0, 0, 0]
    life = [0, 0, 1, 0, 0, 0, 0, 0]
    return maze

def get_plane():
    #TODO
    r = 100
    return np.zeros((r, r))

def visualize(plane):
    # TODO
    ret = ""
    r = len(plane[1])
    
    for x in range(r):
        for y in range(r):
            if plane[x,y] == 0:
                ret += "X"
            else:
                ret += " "
            
            if y == r - 1:
                ret += '\n'
    print(ret)