#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int x = get_int("What's x? ");
    int y = get_int("What's y? ");
    char operator = get_char("Operation? ");

    if (operator == '+')
    {
        printf("%i\n", x + y);
    }
    else if (operator == '-')
    {
        printf("%i\n", x - y);
    }
    else if (operator == '*')
    {
        printf("%i\n", x * y);
    }
    else if (operator == '/')
    {
        printf("%i\n", x / y);
    }
    else
    {
        printf("Non-supported or invalid operator\n");
    }
}