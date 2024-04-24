import sys
import Evolution as ev

import threading
import multiprocessing
from tqdm import tqdm

population_size = int(sys.argv[1])
chromosome_size = int(sys.argv[2])
generations = int(sys.argv[3])

nr_breeding_parents = int(sys.argv[4])
nr_offspring = int(sys.argv[5])
nr_tournament = int(sys.argv[6])

parent_selection_m = int(sys.argv[7])
recomb_coef_m = int(sys.argv[8])
next_gen_selection_m = int(sys.argv[9])

objective_function = int(sys.argv[10])
experiments = int(sys.argv[11])
#lower_bound = float(sys.argv[12])
#upper_bound = float(sys.argv[13])

print(f"{'Population Size:' : <30}{population_size}")
print(f"{'Chromosome Size:' : <30}{chromosome_size}")
print(f"{'Generations:' : <30}{generations}")
print(f"{'Nr of Breeding Parents:' : <30}{nr_breeding_parents}")
print(f"{'Nr of Offspring:' : <30}{nr_offspring}")
print(f"{'Nr Parents in Tournament:' : <30}{nr_tournament}")
print(f"{'Parent Selection Method:' : <30}{parent_selection_m}")
print(f"{'Recomb Coef Method:' : <30}{recomb_coef_m}")
print(f"{'Next Gen Selection Method:' : <30}{next_gen_selection_m}")
print(f"{'Obective Function:' : <30}{objective_function}")
print(f"{'Experiments:' : <30}{experiments}")
#print(f"{'Lower Bound:' : <30}{lower_bound}")
#print(f"{'Upper Bound:' : <30}{upper_bound}")
print()

objective_function_names = ["Absolute", "Ackley_1", "Alpine_1", "Step_2", "Schwefel_2.23", "Step_3", "Shubert_4", "Discus", "Egg_Crate", "Deb_1"]
lower_bounds = [-100.0, -32.0, -10.0, -100.0, -10.0, -5.12, -10.0, -100.0, -5.0, -1.0]
upper_bounds = [100.0, 32.0, 10.0, 100.0, 10.0, 5.12, 10.0, 100.0, 5.0, 1.0]

if (objective_function == -1): # Go over all functions

    for e in tqdm(range(experiments), desc="Exp"):

        processes = []
        for f in range(len(objective_function_names)):

            lower_bound = lower_bounds[f]
            upper_bound = upper_bounds[f]

            objective_function_name = objective_function_names[f]
            p = multiprocessing.Process(target = ev.evolution, args = [population_size, chromosome_size, generations, nr_breeding_parents, nr_offspring,
                                                                nr_tournament, parent_selection_m, recomb_coef_m, next_gen_selection_m, f,
                                                                objective_function_name, lower_bound, upper_bound, e])
            p.start()
            processes.append(p)
            
        for p in processes:
            p.join()
    
else:
    for e in tqdm(range(experiments), desc="Exp"):
        lower_bound = lower_bounds[objective_function]
        upper_bound = upper_bounds[objective_function]
        
        objective_function_name = objective_function_names[objective_function]
        ev.evolution(population_size, chromosome_size, generations, nr_breeding_parents, nr_offspring,
                nr_tournament, parent_selection_m, recomb_coef_m, next_gen_selection_m, objective_function,
                objective_function_name, lower_bound, upper_bound, e)