import ui as ui
import ca_alg as alg
import numpy as np
def main():
    surv = ui.get_surv()
    born = ui.get_born()
    plane = ui.get_plane()

    alg.init_ca(plane)
    alg.ca(plane, surv, born)



# if __main__ == '__name__':
main()
