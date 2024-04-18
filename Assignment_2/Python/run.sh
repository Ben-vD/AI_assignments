#! /bin/bash 

population_size=100
chromosome_size=2
generations=250

nr_breeding_parents=5
nr_offspring=100
nr_tournament=10

parent_selection_m=2
recomb_coef_m=1

objective_function=-1

experiments=30

lower_bound=-100
upper_bound=100

python Main.py $population_size $chromosome_size $generations $nr_breeding_parents $nr_offspring $nr_tournament $parent_selection_m $recomb_coef_m $objective_function $experiments $lower_bound $upper_bound