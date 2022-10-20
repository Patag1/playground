#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int n = 50;
    int *p = &n;
    // printf("%p\n", &n); both ways are valid
    printf("%p\n", p); // shows address
    printf("%i\n", *p); // shows to whatever the pointer points at (50)

    // CS50 string
    // string s = "HI!";

    // C pointer to string (array of chars)
    char *s = "HI!";
    printf("%p\n", &s[0]);  // prints address of a char
    printf("%p\n", &s[1]);
    printf("%p\n", &s[2]);
    printf("%p\n", &s[3]);
    
    printf("%c\n", *s);     // prints whatever char is at *s
    printf("%c\n", *(s+1));
    printf("%c\n", *(s+2));
    printf("%c\n", *(s+3)); // if we go beyond the string's limit, we might cause a segmentation fault

    printf("%c\n", s);     // prints FROM s onward ("HI!")
    printf("%c\n", s+1);   // "I!"
    printf("%c\n", s+2);   // "!"
}