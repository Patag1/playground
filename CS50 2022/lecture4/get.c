#include <stdio.h>

int main(void)
{
    // C version of CS50's get_int
    int x = NULL;
    printf("x: ");
    scanf("%i", &x);

    printf("x: %i\n", x);

    // C version of CS50's get_string
    char s[4];
    printf("s: ");
    scanf("%s", s);

    printf("s: %s", s);
}