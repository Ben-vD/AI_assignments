import numpy as np
import objectiveFunctions as of

# Works and Tested
def evalFitness(individuals, objective_function):
    
    population_size, chromosome_size = individuals.shape
    fitness = np.zeros(population_size)

    # Go over individuals and get calculate fitness 
    for i in range(population_size):

        if (objective_function == 0):
            fitness[i] = of.absolute(individuals[i, :])

    return fitness


# Works and Tested
def selectNextGeneration(parents, parentFitness, offspring, objective_function):

    population_size, chromosome_size = parents.shape

    # Calculate offspring fitness values
    offspringFitness = evalFitness(offspring, objective_function)

    # Combine parents and offspring
    population = np.concatenate((parents, offspring), axis = 0)
    population_fitness = np.concatenate((parentFitness, offspringFitness), axis = 0)

    # Select next generation (top population_size)
    population_sorted_idxs = np.argsort(population_fitness)
    population_sorted = population[population_sorted_idxs]
    population_fitness_sorted = population_fitness[population_sorted_idxs]

    next_generation = population_sorted[:population_size, :]
    next_generation_fitness = population_fitness_sorted[:population_size]

    return next_generation, next_generation_fitness

def selectParentsForBreeding(parent_selection_m, parents, nr_breeding_parents):
    
    if (parent_selection_m == 0):
        return randomParentSelection(parents, nr_breeding_parents)
    elif (parent_selection_m == 1):
        return tournament(parents, nr_breeding_parents)
    elif (parent_selection_m == 2):
        return maxDisTournament(parents, nr_breeding_parents)    

# Works and Tested
def randomParentSelection(parents, nr_breeding_parents):

    population_size, chromosome_size = parents.shape
    return np.random.choice(range(population_size), nr_breeding_parents, replace = False)


def tournament(parents, nr_breeding_parents):
    population_size, chromosome_size = parents.shape

def maxDisTournament(parents, nr_breeding_parents):
    population_size, chromosome_size = parents.shape

# Works and Tested
def createRecombCoefArray(nr_breeding_parents, chromosome_size, equal):

    if (equal):
        return 1 / nr_breeding_parents * np.ones((nr_breeding_parents, chromosome_size))

    random_arr = np.random.uniform(size = (nr_breeding_parents, chromosome_size))
    cols_sum = np.sum(random_arr, axis = 0)[np.newaxis, :]
    norm_random_arr_cols = (1 / cols_sum) * random_arr

    return norm_random_arr_cols