
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

