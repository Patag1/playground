#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int scores[1024];
    for (int i = 0; i < 1024; i++)
    {
        printf("%i\n", scores[i]); // prints remnants of that memory space's past usage
    }

    int *x;
    int *y;

    x = malloc(sizeof(int));

    *x = 42;
    // *y = 13; this assigns value to a potential garbage value since we did not allocate memory for it

    // instead...
    y = x;
    *y = 13;
}