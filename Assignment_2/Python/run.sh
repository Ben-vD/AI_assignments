#! /bin/bash 

population_size=100
chromosome_size=10
generations=500

nr_breeding_parents=2
nr_offspring=100
nr_tournament=15

parent_selection_m=2
recomb_coef_m=1
next_gen_selection_m=0

objective_function=0

experiments=1

lower_bound=-100
upper_bound=100

python Main.py $population_size $chromosome_size $generations $nr_breeding_parents $nr_offspring $nr_tournament $parent_selection_m $recomb_coef_m $next_gen_selection_m $objective_function $experiments $lower_bound $upper_bound