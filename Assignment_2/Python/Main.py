import numpy as np
import sys
import utilFunctions as uf

population_size = int(sys.argv[1])
chromosome_size = int(sys.argv[2])
generations = int(sys.argv[3])

nr_breeding_parents = int(sys.argv[4])
nr_offspring = int(sys.argv[5])
nr_tournament = int(sys.argv[6])

parent_selection_m = int(sys.argv[7])
recomb_coef_m = int(sys.argv[8])

objective_function = int(sys.argv[9])
lower_bound = float(sys.argv[10])
upper_bound = float(sys.argv[11])

print(f"{'Population Size:' : <30}{population_size}")
print(f"{'Chromosome Size:' : <30}{chromosome_size}")
print(f"{'Generations:' : <30}{generations}")
print(f"{'Nr of Breeding Parents:' : <30}{nr_breeding_parents}")
print(f"{'Nr of Offspring:' : <30}{nr_offspring}")
print(f"{'Nr Parents in Tournament:' : <30}{nr_tournament}")
print(f"{'Parent Selection Method:' : <30}{parent_selection_m}")
print(f"{'Recomb Coef Method:' : <30}{recomb_coef_m}")
print(f"{'Obective Function:' : <30}{objective_function}")
print(f"{'Lower Bound:' : <30}{lower_bound}")
print(f"{'Upper Bound:' : <30}{upper_bound}")
print()

# Create recombination Coefficients (Works)
recomb_coef_arr = np.zeros((nr_breeding_parents, chromosome_size))
if (recomb_coef_m == 0):
    recomb_coef_arr = uf.createRecombCoefArray(nr_breeding_parents, chromosome_size, True)

elif (recomb_coef_m == 1):
    recomb_coef_arr = uf.createRecombCoefArray(nr_breeding_parents, chromosome_size, False)

# Create Initial Population (Works)
parents = np.random.uniform(size = (population_size, chromosome_size,), low = lower_bound, high = upper_bound)
parent_fitness = uf.evalFitness(parents, objective_function)
parent_avg = np.average(parent_fitness)

print(parent_avg)

# Evolution
for g in range(generations):

    # Generate offspring population
    offspring = np.zeros((nr_offspring, chromosome_size))
    for o in range(nr_offspring):
        
        # Select Parents
        selected_parents_idxs = uf.selectParentsForBreeding(parent_selection_m, parents, nr_breeding_parents)
        selected_parents = parents[selected_parents_idxs, :]

        # Spawn offspring from selected parents
        offspring[o, :] = np.average(selected_parents, 0, recomb_coef_arr)
    
    # Selext next generation (new parents)
    parents, parent_fitness = uf.selectNextGeneration(parents, parent_fitness, offspring, objective_function)
    parent_avg = parent_avg = np.average(parent_fitness)
    print(parent_avg)