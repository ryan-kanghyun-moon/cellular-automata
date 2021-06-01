import numpy as np
import ui as ui
from random import random, seed
nit = 200
rand_p = 0.03

def randomize(plane):
    x = len(plane)
    y = len(plane[1])
    seed(1)
    for xi in range(x):
        for yi in range(y):
            if  random() < rand_p :
                plane[xi][yi] = 1 
    return plane

def init_ca(p):
    #TODO
    plane = p

    l = int(len(plane[1]))
    
   
    # # left straight
    # l /= 2
    # plane[l][l-1] = 1
    # plane[l][l] = 1
    # plane[l][l+1] = 1

    # # cross
    # l = int(l/2)
    # plane[l][l-1] = 1
    # plane[l][l] = 1
    # plane[l][l+1] = 1
    # plane[l-1][l] = 1
    # plane[l+1][l] = 1

    # # cross - one down
    # l = int(l/2)
    # plane[l][l-1] = 1
    # plane[l][l] = 1
    # plane[l][l+1] = 1
    # plane[l+1][l] = 1

    # # cross in diffrent place
    # l +=  15
    # plane[l][l-1] = 1
    # plane[l][l] = 1
    # plane[l][l+1] = 1
    # # plane[l-1][l] = 1
    # plane[l+1][l] = 1

    # l +=  25
    # plane[l][l-1] = 1
    # plane[l][l] = 1
    # plane[l][l+1] = 1
    # plane[l-1][l] = 1
    # # plane[l+1][l] = 1

    # l +=  -30
    # # plane[l][l-1] = 1
    # plane[l][l] = 1
    # plane[l][l+1] = 1
    # plane[l-1][l] = 1
    # # plane[l+1][l] = 1

    # # l +=  20
    # # plane[l][l-1] = 1
    # # plane[l][l] = 1
    # # plane[l][l+1] = 1
    # # # plane[l-1][l] = 1
    # # plane[l+1][l] = 1
    
    # l +=  -60
    # # plane[l][l-1] = 1
    # plane[l][l] = 1
    # plane[l][l+1] = 1
    # plane[l-1][l] = 1
    # plane[l+1][l] = 1

    

    randomize(plane)

    return plane

def cnt_nb(plane, x, y):
    ret = 0
    for h in range(3):
        x_coord = x + h - 1
        if x_coord >= 0 and x_coord < len(plane):
            
            for v in range(3):
                y_coord = y + v - 1
                
                if y_coord >= 0 and y_coord < len(plane[0]) and (y_coord != y or x_coord != x):
                    ret += int(plane[x_coord][y_coord])
    
    return ret


def insert(s, plane, coord):
    x = coord[0]
    y = coord[1]
    
    for h in range(3):
        x_coord = x + h - 1
        if x_coord >= 0 and x_coord < len(plane):
            
            for v in range(3):
                y_coord = y + v - 1
                
                if y_coord >= 0 and y_coord < len(plane[0]):
                    s.add((x_coord, y_coord))
    
    return s


def init_scan(plane):
    s = set()
    for x in range(len(plane)):
        for y in range(len(plane[0])):
            if plane[x][y] == 1:
                insert(s, plane, (x,y))
                
    return s


def ca(plane, surv, born):
    currp = plane
    ui.visualize(plane)
    
    s = init_scan(plane)

    for i in range(nit):
        
        nplane = ui.get_plane()
        nset = set()
        
        for coord in s:
            x = coord[0]
            y = coord[1]

            nb = cnt_nb(currp, x, y)
                
            if currp[x][y] == 0 and born[nb] == 1:
                nplane[x][y] = 1
                insert(nset, plane, (x, y))
              
            
            elif currp[x][y] == 1 and surv[nb] == 0:
                nplane[x][y] = 0
                insert(nset, plane, (x, y))
              

            elif currp[x][y] == 1:
                nplane[x][y] = 1
                nset.add((x, y))
            
        ui.visualize(nplane)
        currp = nplane
        s = nset

    ui.visualize(currp)


