import numpy as np
import utilFunctions as uf
from tqdm import tqdm

def evolution(population_size, chromosome_size, generations, nr_breeding_parents, nr_offspring, nr_tournament,
              parent_selection_m, recomb_coef_m, next_gen_selection_m, objective_function, objective_function_name,
              lower_bound, upper_bound, experiment):

    np.random.seed()

    # Create recombination Coefficients (Works)
    recomb_coef_arr = np.zeros((nr_breeding_parents, chromosome_size))
    if (recomb_coef_m == 0):
        recomb_coef_arr = uf.createRecombCoefArray(nr_breeding_parents, chromosome_size, True)

    # Create Initial Population (Works)
    parents = np.random.uniform(size = (population_size, chromosome_size,), low = lower_bound, high = upper_bound)
    parent_fitness = uf.evalFitness(parents, objective_function)
    parent_avg = np.average(parent_fitness)
    parent_div = uf.diversity(parents)

    # Write out initial results
    #iteration_data_file_name = "../Results/{}_Iteration.txt".format(objective_function_name)
    #iteration_result = "{} {} {} {}\n".format(experiment, 0, parent_avg, parent_div)
    #f_it = open(iteration_data_file_name, "a")
    #f_it.write(iteration_result)

    # Evolution
    pbar = tqdm(range(1, generations), leave = False)
    pbar.set_description(f'{objective_function_name}: Avg F = {parent_avg}')

    linear_increasing_tournament_size = False
    if (nr_tournament == -1):
        linear_increasing_tournament_size = True


    for g in pbar:

        # Recombination for random weights 
        if (recomb_coef_m == 1):
            recomb_coef_arr = uf.createRecombCoefArray(nr_breeding_parents, chromosome_size, False)

        # Linear increasing tournament size
        if (linear_increasing_tournament_size):
            nr_tournament = int(((g + 1) / generations) * population_size)

        # Generate offspring population
        offspring = np.zeros((nr_offspring, chromosome_size))
        for o in range(nr_offspring):

            # Select Parents
            selected_parents_idxs = uf.selectParentsForBreeding(parent_selection_m, parents, parent_fitness, nr_breeding_parents, nr_tournament)
            selected_parents = parents[selected_parents_idxs, :]

            # Spawn offspring from selected parents
            offspring[o, :] = np.average(a = selected_parents, axis = 0, weights = recomb_coef_arr)
        
        # Selext next generation (new parents)
        parents, parent_fitness = uf.selectNextGeneration(parents, parent_fitness, offspring, objective_function, nr_tournament, next_gen_selection_m)
        parent_avg = parent_avg = np.average(parent_fitness)
        parent_div = uf.diversity(parents)       
        pbar.set_description(f'{objective_function_name}: Avg F = {parent_avg}')

        # Write out iteration results
        #iteration_result = "{} {} {} {}\n".format(experiment, g, parent_avg, parent_div)
        #f_it.write(iteration_result)

    final_file_name = "../Results/{}_Final.txt".format(objective_function_name)
    final_result = "{} {} {}\n".format(experiment, parent_avg, parent_div)
    #result = "Exp {}, Final Avg Fitness = {}; Final Diversity = {}\n".format(experiment, parent_avg, parent_div)

    f = open(final_file_name, "a")
    f.write(final_result)

    f.close()
    #f_it.close()