#ifndef LIST_H
#define LIST_H

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Define the Node struct
typedef struct node {
    void *data;
    struct node *next;
} Node;

typedef struct list {
    Node *head;
    size_t data_size;
} List;

// Declare functions
void init_list();
void free_list(List *list);
void push(List *list, void *data);
void pop(List *list);
void append(List *list, void *data);

#endif // LIST_H
