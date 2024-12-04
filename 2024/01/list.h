#ifndef LIST_H
#define LIST_H

// Define the Node struct
typedef struct node {
    int val;
    struct node *next;
} Node;

// Declare functions
Node* create_list(int val);
void push(Node **l, int i);
int pop(Node **head, int index);
int get(Node *l, int i);
int length(Node *l);
void print_list(Node *current);
void sort(Node **head);

#endif // LIST_H
