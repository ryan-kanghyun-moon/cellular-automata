# Cellular Automaton #
Simple experimental environment for cellular automata following various rules

---
## How To Use ##
download code and 
``python main.py`` to start!

---
## Optimization / Implementation ##

### V1 ###
On each iteration, every cell was scanned for the live/death condition check. Running time was increasing significantly as the size of the plane was increasing.

### V2 ###
A single set and a second plane were used to keep track of the active cells and their neighbors to be tested and rendered on the next iteration. Total running time was reduced by a third compared to the first version. 

### V3 (current) ###
Two sets and a single plane were used to keep track of changed cells and their respective neighbor to be tested on the next iteration. Running time was again reduced by a half for rules that are explosive (e.g. **Maze**). (not much change for **Game of Life**)