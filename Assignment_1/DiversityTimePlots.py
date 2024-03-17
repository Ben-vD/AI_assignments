import numpy as np
import sys
import matplotlib.pyplot as plt

inputDim = int(sys.argv[1])
itr_count = int(sys.argv[2])
experiments = int(sys.argv[3])
appr = int(sys.argv[4])
evalFunc = int(sys.argv[5])
PARTICLES_NR = 30

runs = appr + 1
if (appr == 5):
    runs = 5
    appr = 0

plots, axis = plt.subplots(1,2, figsize=(10,5))

for a in range(appr, runs):

    inputDivFile = "Data/diversityData" + str(a) + "_" + str(evalFunc) + ".txt"
    inputFitFile = "Data/fitnessData" + str(a) + "_" + str(evalFunc) + ".txt"

    dataDiv = np.loadtxt(inputDivFile, delimiter = ",")
    dataDiv = dataDiv.reshape(experiments, itr_count)
    meanDiv = np.mean(dataDiv, axis = 0)
    stdDiv = np.std(dataDiv, axis = 0)
    medDiv = np.median(dataDiv, axis = 0)

    dataFit = np.loadtxt(inputFitFile, delimiter = ",")
    dataFit = dataFit.reshape((experiments, itr_count))
    meanFit = np.mean(dataFit, axis = 0)
    stdFit = np.std(dataFit, axis = 0)
    medFit = np.median(dataFit, axis = 0)


    #for exp in range(experiments):
    #    axis[0].plot(range(itr_count), dataDiv[exp,:], linestyle = "dashed")
    #    axis[1].plot(range(itr_count), dataFit[exp, :], linestyle = "dashed")

    axis[0].plot(range(itr_count), meanDiv)
    axis[1].plot(range(itr_count), meanFit)

    axis[0].set_ylabel("Diversity")
    axis[1].set_ylabel("Fitness")

    print("Diversity, Approach: ", a, meanDiv[itr_count - 1], u"\u00B1", stdDiv[itr_count - 1], "Median:", medDiv[itr_count - 1])
    print("Fitness, Approach: ", a, meanFit[itr_count - 1], u"\u00B1", stdFit[itr_count - 1], "Median:", medFit[itr_count - 1])

plots.legend(["1", "2", "3", "4", "5"], title = "Approach", borderaxespad = 0.1, loc = "center right", bbox_to_anchor=(1.1, 0.6))

plt.tight_layout()  

axis[0].set_yscale('symlog')
axis[1].set_yscale('symlog') 
plt.savefig("./Results/dataPlot_" + str(evalFunc) + ".pdf", format="pdf", bbox_inches="tight")

#plt.show()

print()

plt.show(block=False)
#plt.pause(2)
plt.close()