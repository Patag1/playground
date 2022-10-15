#include <stdio.h>
#include <cs50.h>

const int N = 3;

float average(int array[]);

int main(void)
{
    int scores[N];

    for (int i = 0; i < N; i++)
    {
        scores[i] = get_int("Score: ");
    }
    
    printf("Average: %f\n", average(scores));
}

float average(int array[])
{
    int total = 0;

    for (int i = 0; i < N; i++)
    {
        total += array[i];
    }

    return total / (float) N;
}