
# old implementation iterating every cell each time
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

                if currp[x][y] == 0 and nb > 0 and born[nb] == 1:
                    nplane[x][y] = 1

                if currp[x][y] == 1 and surv[nb] == 1:
                    nplane[x][y] = 1

                if currp[x][y] == 1 and surv[nb] == 0:
                    nplane[x][y] = 0

        ui.visualize(nplane)
        currp = nplane
    ui.visualize(currp)

# one-stack two-plane implementation

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
                
            if currp[x][y] == 0 and nb > 0 and born[nb - 1] == 1:
                nplane[x][y] = 1
                insert(nset, plane, (x, y))
              
            
            elif currp[x][y] == 1 and nb > 0 and surv[nb - 1] == 0:
                nplane[x][y] = 0
                insert(nset, plane, (x, y))
              

            elif currp[x][y] == 1:
                nplane[x][y] = 1
                nset.add((x, y))
           
            
        ui.visualize(nplane)
        currp = nplane
        s = nset

    ui.visualize(currp)