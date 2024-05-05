#!/bin/bash

grid_width=40
grid_height=40
nr_ants=25
iterations=200000
gamma=2
gamma_1=0.2
gamma_2=0.2
patch_size=1

python Main.py $grid_width $grid_height $nr_ants $iterations $gamma $gamma_1 $gamma_2 $patch_size