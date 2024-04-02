#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#include <omp.h>

#include "ObjectiveFunctions.h"
#include "UtilFunctions.h"

double** initInitialPopulation(int populationSize, int chromosomeSize, double lowerBound, double upperBound);

void evolution(double **initialPopulation, int generations, int populationSize, int chromosomeSize, int recombCoefM);
double** nextGeneration (double **initialPopulation, int generations, int populationSize, int chromosomeSize, int recombCoefM);

double* populationFitness(double** individuals, int populationSize, int chromosomeSize, int obectiveFunction);
double individualFitness(double* individual, int chromosomeSize, int obectiveFunction);

int main(int argc, char *argv[]){

    int populationSize = atoi(argv[1]), chromosomeSize = atoi(argv[2]), generations = atoi(argv[3]);
    double lowerBound = atof(argv[4]), upperBound = atof(argv[5]);
    int recombCoefM = atoi(argv[6]);

    srand(time(NULL));

    printf("Population size = %d, Chromosome size (Number of genes)) = %d, Generations = %d\n", populationSize, chromosomeSize, generations);
    printf("Lowerbound = %lf, Upperbound = %lf\n", lowerBound, upperBound);
    printf("Recombination coefficient method = %d\n\n", recombCoefM);

    // Generate Random initial population
    double **initialPopulation = initInitialPopulation(populationSize, chromosomeSize, lowerBound, upperBound);
    printDouble2DArrayPtr(initialPopulation, populationSize, chromosomeSize);

    double *fitness = populationFitness(initialPopulation, populationSize, chromosomeSize, 0);

    printDoubleArray(fitness, populationSize);

    //Evolution for number of generations
    //evolution(individuals, generations, populationSize, chromosomeSize, recombCoefM);

    freeDouble2DArray(initialPopulation, populationSize);
    free(fitness);

    return 0;
}

double** initInitialPopulation(int populationSize, int chromosomeSize, double lowerBound, double upperBound) {

    double **individuals = (double**) malloc (populationSize * sizeof(double*));
 
    for (int i = 0; i < populationSize; i++) {
        *(individuals + i) = (double*) malloc(chromosomeSize * sizeof(double));
    }

    for (int i = 0; i < populationSize; i++) {
        for (int j = 0; j < chromosomeSize; j++) {
            *(*(individuals + i) + j) = rand_range_double(lowerBound, upperBound); // OR individuals[i][j] = ...
        }
    }

    return individuals;
}

void evolution(double **initialPopulation, int generations, int populationSize, int chromosomeSize, int recombCoefM) {

    double **parents = copy_array(initialPopulation, populationSize, chromosomeSize);

    for (int g = 0; g < generations; g++) {



        double **offspring = nextGeneration(parents, generations, populationSize, chromosomeSize, recombCoefM);

    }

    freeDouble2DArray(parents, populationSize);

}

double** nextGeneration (double **parents, int generations, int populationSize, int chromosomeSize, int recombCoefM) {


    return NULL;

}

double* populationFitness(double** individuals, int populationSize, int chromosomeSize, int obectiveFunction) {
    
    double *fitnessArray = (double*) malloc(populationSize * sizeof(double));

    #pragma omp parallel for 
    for (int i = 0; i < populationSize; i++) {
        *(fitnessArray + i) = individualFitness(*(individuals + i), chromosomeSize, obectiveFunction);

        //int tid = omp_get_thread_num();
        //printf("The thread %d  executes i = %d\n", tid, i);
    }
    return fitnessArray;
}

double individualFitness(double* individual, int chromosomeSize, int obectiveFunction) {

    if (obectiveFunction == 0) {
        return absolute(individual, chromosomeSize);
    }

}