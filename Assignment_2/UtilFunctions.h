#include <stdio.h>
#include <stdlib.h>

double rand_range_double(double min, double max) {

    double random = ((double) rand()) / RAND_MAX;
    double range = (max - min)  * random;
    double rand_double = min + range;

    return rand_double;
}

void printFloatArrayPtr(double **arr, int rows, int cols) {

    for (int r = 0; r < rows; r++) {

        for (int c = 0; c < cols; c++) {
            printf("%f ", *(*(arr + r) + c));
        }
    printf("\n");
    }

}