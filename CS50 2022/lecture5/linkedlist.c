#include <stdio.h>
#include <stdlib.h>
#include <cs50.h>

typedef struct node
{
    int num;
    struc node *next;
}
node;


int main(void)
{
    // Create list
    node *list = NULL;

    // Add a number to list
    node *n = malloc(sizeof(node));
    if (n == NULL)
    {
        return 1;
    }
    // (*n).num = 1;
    n->num = 1; // GO to whatever n is pointing to and place 1 in its num variable
    n->next = NULL; // and NULL to its next variable

    list = n;

    // Add a number to list
    n = malloc(sizeof(node));
    if (n == NULL)
    {
        free(list);
        return 1;
    }
    n->num = 2;
    n->next = NULL;
    list->next = n;

    // Add a number to list
    n = malloc(sizeof(node));
    if (n == NULL)
    {
        free(list->next);
        free(list);
        return 1;
    }
    n->num = 3;
    n->next = NULL;
    list->next->next = n;

    // Print numbers
    for (node *tmp = list; tmp != NULL; tmp = tmp->next)
    {
        printf("%i\n", tmp->num);
    }

    // Free memory
    while (list != NULL)
    {
        node *tmp = list->next;
        free(list);
        list = tmp;
    }

    return 0;
}