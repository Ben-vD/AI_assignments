#include <stdio.h>
#include <stdlib.h>

double** copy_array(double **arr, int rows, int cols) {

    double **c_arr = (double**) malloc(rows * sizeof(double*));

    for (int r = 0; r < rows; r++) {
        *(c_arr + r) = (double*) malloc(cols * sizeof(double*));   
    }

    for (int r = 0; r < rows; r++) {
        for (int c = 0; c < cols; c++) {
            *(*(c_arr + r) + c) = *(*(arr + r) + c);
        }
    }

    return c_arr;
}

double rand_range_double(double min, double max) {

    double random = ((double) rand()) / RAND_MAX;
    double range = (max - min)  * random;
    double rand_double = min + range;

    return rand_double;
}

int rand_range_int(int min, int max) {

    int random = (rand() % (max - min + 1)) + min;
    return random;
}

void printDouble2DArrayPtr(double **arr, int rows, int cols) {

    for (int r = 0; r < rows; r++) {
        for (int c = 0; c < cols; c++) {
            printf("%lf ", *(*(arr + r) + c));
        }
        printf("\n");
    }
    printf("\n");
}

void printDoubleArray(double *arr, int l) {
    for (int i = 0; i < l; i++) {
        printf("%lf ", *(arr + i));
    }
    printf("\n");
}

double sumArray(double* arr, int l) {
    double sum = 0;
    for (int i = 0; i < l; i++) {
        sum = sum + *(arr + i);
    }
    return sum;
}

void freeDouble2DArray(double** arr, int rows) {

    for (int r = 0; r < rows; r++) {
        free(*(arr + r));
    }
    free(arr);
}