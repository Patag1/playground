#include <stdio.h>
#include <cs50.h>
#include <ctype.h>
#include <stdlib.h>
#include <string.h>

int main(void)
{
    char *s = get_string("s: ");
    if (s == NULL) // get_string returns NULL if the input is too much to handle
    {
        return 1;
    }
    
    // char *t = s; copies the same memory address, so it uppercases "both" strings
    char *t = malloc(strlen(s) + 1); // give me x number of bytes for a string + 1 (\0)
    if (t == NULL) // same as get_string, returns NULL if the string is too long
    {
        return 1;
    }

    strcpy(t, s);

    // i.e strcpy under the hood
    // for (int i = 0, n = strlen(s) + 1; i < n; i++) + 1 = \0
    // {
    //     t[i] = s[i];
    // }

    if (strlen(t) > 0) // checks if there's a string in the first place to prevent segmentation faults
    {
        t[0] = toupper(t[0]);
    }

    printf("%s\n", s);
    printf("%s\n", t);

    free(t); // it is a law in C to free memory when you use malloc

    return 0;
}