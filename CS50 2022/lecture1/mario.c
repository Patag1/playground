#include <stdio.h>
#include <cs50.h>

int get_size(void);
void print_block(int size);

int main(void)
{
    // ???? row
    for (int i = 0; i < 3; i++)
    {
        printf("?");
    }
    printf("\n");

    // # block column
    for (int j = 0; j < 3; j++)
    {
        printf("#\n");
    }

    // sets block size
    int n = get_size();

    // prints requested block size
    print_block(n);
}

int get_size(void)
{
    int n;
    do
    {
        n = get_int("Dimensions? ");
    }
    while (n < 1);

    return n;
}

void print_block(int size)
{
    for (int i = 0; i < size; i++)
    {
        for (int j = 0; j < size; j++)
        {
            printf("#");
        }
        printf("\n");
    }
    printf("\n");
}