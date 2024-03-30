#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#include "ObjectiveFunctions.h"
#include "UtilFunctions.h"

double** initialPopulation(int populationSize, int chromosomeSize, double lowerBound, double upperBound);

int main(int argc, char *argv[]){

    int populationSize = atoi(argv[1]), chromosomeSize = atoi(argv[2]), generations = atoi(argv[3]);
    double lowerBound = atof(argv[4]), upperBound = atof(argv[5]);

    srand(time(NULL));

    printf("Population size = %d, Chromosome size (Number of genes)) = %d, Generations = %d\n", populationSize, chromosomeSize, generations);
    printf("Lowerbound = %f, Upperbound = %f\n\n", lowerBound, upperBound);

    double **individuals = initialPopulation(populationSize, chromosomeSize, lowerBound, upperBound);

    printFloatArrayPtr(individuals, populationSize, chromosomeSize);

    free(individuals);

    return 0;
}

double** initialPopulation(int populationSize, int chromosomeSize, double lowerBound, double upperBound) {

    double **individuals = (double**) malloc (populationSize * sizeof(int*));

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