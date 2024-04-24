import numpy as np
import utilFunctions as uf
import objectiveFunctions as of

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

        print(tournament_parents)

        best_tournament_parent = tournament_parents[best_tournament_parent_idx]
        selected_parents_idxs[t] = best_tournament_parent

        # Remove parent from subsequent tournaments
        # parents_pool = np.delete(parents_pool, np.where(parents_pool == best_tournament_parent))

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

        print(tournament_parents)

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

        print(tournament_parents_distances)

        # Select parent with max distance to prior selected parents
        largest_distance_idx = np.argmax(tournament_parents_distances)
        best_tournament_parent_idx = tournament_parents[largest_distance_idx]
        selected_parents_idxs[t] = best_tournament_parent_idx

        parents_pool = np.delete(parents_pool, np.where(parents_pool == best_tournament_parent_idx))

    return selected_parents_idxs

#np.random.seed(0)

parents = np.random.uniform(size = (10, 3), low = -100, high = 100)
p_fit = uf.evalFitness(parents, 0)

print(tournamentSelection(parents, p_fit, 4, 4))