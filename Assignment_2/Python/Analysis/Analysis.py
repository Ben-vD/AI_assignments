import numpy as np
import matplotlib.pyplot as plt
import sys

def Analysis(function, experiments, generations):

    file_name = "../Results/{}_Iteration.txt".format(f)
    data = np.loadtxt(file_name, delimiter = " ")

    fitness_data = data[:, 2]
    diversity_data = data[:, 3]

    fitness_data = np.reshape(fitness_data, (generations, experiemnts), order = 'F')
    diversity_data = np.reshape(diversity_data, (generations, experiemnts), order = 'F')

    fitness_data_avg = np.mean(fitness_data, axis = 1)
    diversity_data_avg = np.mean(diversity_data, axis = 1)


    plt.plot(range(generations + 1), fitness_data_avg)
    graph_name = "./Graphs/{}_fitness.pdf".format(function)
    plt.title("{}".format(function))
    plt.xlabel("Generations")
    plt.ylabel("Avg Fitness")
    plt.savefig(graph_name, format="pdf")

    plt.clf()

    plt.plot(range(generations + 1), diversity_data_avg)
    graph_name = "./Graphs/{}_diversity.pdf".format(function)
    plt.title("{}".format(function))
    plt.xlabel("Generations")
    plt.ylabel("Diversity")
    plt.savefig(graph_name, format="pdf")


experiemnts = int(sys.argv[1])
generations = int(sys.argv[2])

objective_function_names = ["Absolute", "Ackley_1", "Alpine_1", "Step_2", "Schwefel_2.23", "Step_3", "Shubert_4", "Discus", "Egg_Crate", "Deb_1"]

for i, f in enumerate(objective_function_names):
    Analysis(f, experiemnts, generations)
    plt.clf()