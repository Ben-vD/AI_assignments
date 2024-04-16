import numpy as np
import utilFunctions as uf
from tqdm import tqdm

def evolution(population_size, chromosome_size, generations, nr_breeding_parents, nr_offspring, nr_tournament,
              parent_selection_m, recomb_coef_m, objective_function, objective_function_name, lower_bound, upper_bound):

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

    # Evolution
    pbar = tqdm(range(generations))
    pbar.set_description(f'{objective_function_name}: Avg F = {parent_avg}')
    for g in pbar:

        # Generate offspring population
        offspring = np.zeros((nr_offspring, chromosome_size))
        for o in range(nr_offspring):
            
            # Select Parents
            selected_parents_idxs = uf.selectParentsForBreeding(parent_selection_m, parents, parent_fitness, nr_breeding_parents, nr_tournament)
            selected_parents = parents[selected_parents_idxs, :]

            # Spawn offspring from selected parents
            offspring[o, :] = np.average(selected_parents, 0, recomb_coef_arr)
        
        # Selext next generation (new parents)
        parents, parent_fitness = uf.selectNextGeneration(parents, parent_fitness, offspring, objective_function)
        parent_avg = parent_avg = np.average(parent_fitness)        
        pbar.set_description(f'{objective_function_name}: Avg F = {parent_avg}')