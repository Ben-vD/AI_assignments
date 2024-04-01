#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#include "ObjectiveFunctions.h"
#include "UtilFunctions.h"

double** initialPopulation(int populationSize, int chromosomeSize, double lowerBound, double upperBound);
void evolution(double **initialPopulation, int generations, int populationSize, int chromosomeSize, int recombCoefM);
double** nextGeneration (double **initialPopulation, int generations, int populationSize, int chromosomeSize, int recombCoefM);

int main(int argc, char *argv[]){

    int populationSize = atoi(argv[1]), chromosomeSize = atoi(argv[2]), generations = atoi(argv[3]);
    double lowerBound = atof(argv[4]), upperBound = atof(argv[5]);
    int recombCoefM = atoi(argv[6]);

    srand(time(NULL));

    printf("Population size = %d, Chromosome size (Number of genes)) = %d, Generations = %d\n", populationSize, chromosomeSize, generations);
    printf("Lowerbound = %f, Upperbound = %f\n", lowerBound, upperBound);
    printf("Recombination coefficient method = %d\n\n", recombCoefM);

    // Generate Random initial population
    double **individuals = initialPopulation(populationSize, chromosomeSize, lowerBound, upperBound);
    printFloatArrayPtr(individuals, populationSize, chromosomeSize);

    //Evolution for number of generations
    evolution(individuals, generations, populationSize, chromosomeSize, recombCoefM);

    free(individuals);

    return 0;
}

double** initialPopulation(int populationSize, int chromosomeSize, double lowerBound, double upperBound) {

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
}

double** nextGeneration (double **parents, int generations, int populationSize, int chromosomeSize, int recombCoefM) {



    return NULL;

}