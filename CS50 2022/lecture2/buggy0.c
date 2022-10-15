#include <stdio.h>

int main(void)
{
    // bug at <=, supposed to print only 3 #s
    for (int i = 0; i <= 3; i++)
    {
        // printf("i = %i\n", i);
        printf("#\n");
    }
}