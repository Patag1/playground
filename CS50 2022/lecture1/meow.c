#include <stdbool.h>
#include <stdio.h>

int main(void)
{
    int i = 0;

    while (i < 3)
    {
        printf("meow\n");
        i++;
    }

    for (int j = 0; j < 3; j++)
    {
        printf("woof\n");
    }

    while (true)
    {
        printf("neigh\n");
    }
}