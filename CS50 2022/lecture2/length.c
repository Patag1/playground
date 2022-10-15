#include <stdio.h>
#include <cs50.h>
#include <string.h>

int main(void)
{
    string name = get_string("What's your name? ");

    int n = 0;
    while (name[n] != '\0')
    {
        n++;
    }

    string s = get_string("What's your name? ");
    int l = strlen(name);

    printf("%i\n", n);
    printf("%i\n", l);
}