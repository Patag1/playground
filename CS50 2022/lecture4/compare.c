#include <stdio.h>
#include <cs50.h>
#include <string.h>

int main(void)
{
    char *s = get_string("s: ");
    char *t = get_string("t: ");

    if (strcmp(s, t) == 0) // instead of s == t
    {
        printf("Same\n");
    }
    else
    {
        printf("Different\n");
    }
}