#!/bin/bash

grid_width=50
grid_height=50
nr_ants=50
iterations=50000
gamma=1
gamma_1=0.5
gamma_2=0.5
patch_size=3

python Main.py $grid_width $grid_height $nr_ants $iterations $gamma $gamma_1 $gamma_2 $patch_size