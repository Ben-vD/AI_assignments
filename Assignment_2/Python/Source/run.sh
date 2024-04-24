#! /bin/bash 

population_size=250
chromosome_size=30
generations=500

nr_breeding_parents=250
nr_offspring=250
nr_tournament=-1        # -1 for linear increasing

parent_selection_m=1    # 0 (random), 1 (normal tournament), 2 (max dis tournament)
recomb_coef_m=1         # 0 equal weights, 1 random weights
next_gen_selection_m=0

objective_function=-1    # -1 for all functions
experiments=30

#-----------------
lower_bound=-100
upper_bound=100

#python Main.py $population_size $chromosome_size $generations $nr_breeding_parents $nr_offspring $nr_tournament $parent_selection_m $recomb_coef_m $next_gen_selection_m $objective_function $experiments $lower_bound $upper_bound

for i in {2..10}
do
    nr_breeding_parents=$i
    python Main.py $population_size $chromosome_size $generations $nr_breeding_parents $nr_offspring $nr_tournament $parent_selection_m $recomb_coef_m $next_gen_selection_m $objective_function $experiments $lower_bound $upper_bound
done

for i in {20..250..10}
do
    nr_breeding_parents=$i
    echo $nr_breeding_parents
    #python Main.py $population_size $chromosome_size $generations $nr_breeding_parents $nr_offspring $nr_tournament $parent_selection_m $recomb_coef_m $next_gen_selection_m $objective_function $experiments $lower_bound $upper_bound
done

#python ../Analysis/Analysis.py 