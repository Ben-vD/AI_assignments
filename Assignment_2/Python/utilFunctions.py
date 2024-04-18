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
        elif (objective_function == 1):
            fitness[i] = of.ackley_1(individuals[i, :])
        elif (objective_function == 2):
            fitness[i] = of.alpine_1(individuals[i, :])
        elif (objective_function == 3):
            fitness[i] = of.step_2(individuals[i, :])
        elif (objective_function == 4):
            fitness[i] = of.schwefel_2_23(individuals[i, :])
        elif (objective_function == 5):
            fitness[i] = of.step_3(individuals[i, :])
        elif (objective_function == 6):
            fitness[i] = of.shubert_4(individuals[i, :])
        elif (objective_function == 7):
            fitness[i] = of.discus(individuals[i, :])
        elif (objective_function == 8):
            fitness[i] = of.egg_crate(individuals[i, :])
        elif (objective_function == 9):
            fitness[i] = of.deb1(individuals[i, :])

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

def selectParentsForBreeding(parent_selection_m, parents, parent_fitness, nr_breeding_parents, nr_tournament):
    
    if (parent_selection_m == 0):
        return randomSelection(parents, nr_breeding_parents)
    elif (parent_selection_m == 1):
        return tournamentSelection(parents, parent_fitness, nr_breeding_parents, nr_tournament)
    elif (parent_selection_m == 2):
        return maxDisTournament(parents, parent_fitness, nr_breeding_parents, nr_tournament)    

# Works and Tested
def randomSelection(parents, nr_breeding_parents):

    population_size, chromosome_size = parents.shape
    return np.random.choice(range(population_size), nr_breeding_parents, replace = False)


def tournamentSelection(parents, parent_fitness, nr_breeding_parents, nr_tournament):

    population_size, chromosome_size = parents.shape
    selected_parents_idxs = np.zeros(nr_breeding_parents, dtype=int)

    # Array used to prevent selecting 1 parent more than once
    parents_pool = np.arange(population_size)

    # Run nr_breeding_parents for nr of parents needed to breed
    for t in range(nr_breeding_parents):

        tournament_parents = np.random.choice(parents_pool, nr_tournament, replace = False)
        tournament_parents_fitness = parent_fitness[tournament_parents]
        best_tournament_parent_idx = np.argmin(tournament_parents_fitness)

        best_tournament_parent = tournament_parents[best_tournament_parent_idx]
        selected_parents_idxs[t] = best_tournament_parent

        # Remove parent from subsequent tournaments
        parents_pool = np.delete(parents_pool, np.where(parents_pool == best_tournament_parent))

    return selected_parents_idxs

def maxDisTournament(parents, parent_fitness, nr_breeding_parents, nr_tournament):
    
    population_size, chromosome_size = parents.shape
    selected_parents_idxs = np.zeros(nr_breeding_parents, dtype=int)

    # Array used to prevent selecting 1 parent more than once
    parents_pool = np.arange(population_size)

    # Select Parent 1 using noraml tournament selection
    selected_parents_idxs[0] = tournamentSelection(parents, parent_fitness, 1, nr_tournament)

    # Remove 1st selected parent from the pool
    parents_pool = np.delete(parents_pool, np.where(parents_pool == selected_parents_idxs[0]))

    # Run tournaments. Range starts as 1 since 1st parent already selected
    for t in range(1, nr_breeding_parents):
        tournament_parents = np.random.choice(parents_pool, nr_tournament, replace = False)

        # Sum Euclidean distance of each individual to all prior selected parents
        tournament_parents_distances = np.zeros(nr_tournament)
        for i in range(nr_tournament):
            sum_distances = 0
            tournament_parent = parents[tournament_parents[i]]
            for j in range(t):
                prior_selected = parents[selected_parents_idxs[j]]
                distance = np.linalg.norm(tournament_parent - prior_selected)
                sum_distances += distance

            tournament_parents_distances[i] = sum_distances

        # Select parent with max distance to prior selected parents
        largest_distance_idx = np.argmax(tournament_parents_distances)
        best_tournament_parent_idx = tournament_parents[largest_distance_idx]
        selected_parents_idxs[t] = best_tournament_parent_idx

        parents_pool = np.delete(parents_pool, np.where(parents_pool == best_tournament_parent_idx))

    return selected_parents_idxs
            

# Works and Tested
def createRecombCoefArray(nr_breeding_parents, chromosome_size, equal):

    if (equal):
        return 1 / nr_breeding_parents * np.ones((nr_breeding_parents, chromosome_size))

    random_arr = np.random.uniform(size = (nr_breeding_parents, chromosome_size))
    cols_sum = np.sum(random_arr, axis = 0)[np.newaxis, :]
    norm_random_arr_cols = (1 / cols_sum) * random_arr

    return norm_random_arr_cols

def diversity(individuals):
    population_size, chromosome_size = individuals.shape
    avg_genes = np.average(individuals, axis = 0)[np.newaxis,:]

    inner_sum = np.sqrt(np.sum(np.square(individuals - avg_genes), axis = 1))
    outer_sum = np.sum(inner_sum)

    return outer_sum / population_size