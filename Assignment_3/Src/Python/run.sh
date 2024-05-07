#!/bin/bash

grid_width=50
grid_height=50
nr_ants=15
iterations=100000

gamma=2
gamma_1=0.15
gamma_2=0.25

patch_size=2

speed_min=1
speed_max=6

python Main.py $grid_width $grid_height $nr_ants $iterations $gamma $gamma_1 $gamma_2 $patch_size $speed_min $speed_max
