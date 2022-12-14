#include <stdio.h>
#include <stdlib.h>
#include <bool.h>
#include <cs50.h>

typedef struct node
{
    int num;
    struct node *left;
    struct node *right;
}
node;

void free_tree(node *root);
void print_tree(node *root);
bool search_tree(node *root, int num);

int main(void)
{
    // Tree of size 0
    node *tree = NULL;

    // Add number to tree
    node *n = malloc(sizeof(node));
    if (n == NULL)
    {
        return 1;
    }
    n->num = 2;
    n->left = NULL;
    n->right = NULL;
    tree = n;

    // Add number to tree
    n = malloc(sizeof(node));
    if (n == NULL)
    {
        return 1;
    }
    n->num = 1;
    n->left = NULL;
    n->right = NULL;
    tree->left = n;

    // Add number to tree
    n = malloc(sizeof(node));
    if (n == NULL)
    {
        return 1;
    }
    n->num = 3;
    n->left = NULL;
    n->right = NULL;
    tree->right = n;

    // Print tree
    print_tree(tree);
    
    // Free tree
    free_tree(tree);

    return 0;
}

void free_tree(node *root)
{
    if (root == NULL)
    {
        return;
    }
    free_tree(root->left);
    free_tree(root->right);
    free(root);
}

void print_tree(node *root)
{
    if (root == NULL)
    {
        return;
    }
    print_tree(root->left);
    printf("%i\n", root->num);
    print_tree(root->right);
}

bool search_tree(node *root, int num)
{
    if (root == NULL)
    {
        return false;
    }

    if (root->num < num)
    {
        return search_tree(root->right, num);
    }
    else if (root->num > num)
    {
        return search_tree(root->left, num);
    }
    else
    {
        return true;
    }

    return false;
}