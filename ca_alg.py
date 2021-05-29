import numpy as np
import ui as ui

nit = 700

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

    # cross - one down
    l = int(l/2)
    plane[l][l-1] = 1
    plane[l][l] = 1
    plane[l][l+1] = 1
    plane[l+1][l] = 1

    # cross in diffrent place
    l +=  15
    plane[l][l-1] = 1
    plane[l][l] = 1
    plane[l][l+1] = 1
    plane[l-1][l] = 1
    # plane[l+1][l] = 1

    l +=  30
    plane[l][l-1] = 1
    plane[l][l] = 1
    plane[l][l+1] = 1
    # plane[l-1][l] = 1
    plane[l+1][l] = 1
    
    l +=  -60
    # plane[l][l-1] = 1
    plane[l][l] = 1
    plane[l][l+1] = 1
    plane[l-1][l] = 1
    plane[l+1][l] = 1



    return plane

def cnt_nb(plane, x, y):
    ret = 0
    r = len(plane[0])
    for h in range(3):
        x_coord = x + h - 1
        if x_coord >= 0 and x_coord < r:
            
            for v in range(3):
                y_coord = y + v - 1
                
                if y_coord >= 0 and y_coord < r and (y_coord != y or x_coord != x):
                    ret += int(plane[x_coord][y_coord])
    
    return ret

def ca(plane, surv, born):
    l = len(plane[0])
    currp = plane
    ui.visualize(plane)
    
    for i in range(nit):
        nplane = ui.get_plane()
        for x in range(l):
            for y in range(l):
                nb = cnt_nb(currp, x, y)
                # if not nb == 0:
                #     print("nb for " + str(x) + ", " + str(y) + ": " + str(nb) + "\n")
            
                if currp[x][y] == 0 and nb > 0 and born[nb - 1] == 1:
                    nplane[x][y] = 1

                if currp[x][y] == 1:
                    nplane[x][y] = 1
                
                if nb > 0 and surv[nb - 1] == 0:
                    nplane[x][y] = 0

        ui.visualize(nplane)
        currp = nplane
    ui.visualize(currp)



