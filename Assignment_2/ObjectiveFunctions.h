#include <stdio.h>
#include <stdlib.h>
#include <math.h>

double absolute(double *ptr, int d) {

    double sum = 0;
    for (int i = 0; i < d; i++) {
        sum = sum + fabs(*(ptr + i));
    }
    return sum;
}