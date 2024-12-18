#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include "list.h"

void init_list(List *list, size_t data_size) {
    list->head = NULL;
    list->data_size = data_size;
}

void free_list(List *list) {
    while (list->head != NULL) {
        Node *next = list->head->next;
        free(list->head->data);
        free(list->head);
        list->head = next;
    }
}

void push(List *list, void *data) {
    Node *new_node = malloc(sizeof(Node));
    new_node->data = malloc(list->data_size);
    memcpy(new_node->data, data, list->data_size);
    new_node->next = list->head;
    list->head = new_node;
}

void append(List *list, void *data) {
    Node *new_node = malloc(sizeof(Node));
    new_node->data = malloc(list->data_size);
    memcpy(new_node->data, data, list->data_size);
    if (list->head == NULL) {
        list->head = new_node;
    } else {
        Node *current = list->head;
        while (current->next != NULL) {
            current = current->next;
        }
        current->next = new_node;
    }
}

void *pop(List* list) {
    if (list->head == NULL) {
        return NULL; // List is empty
    }

    Node *temp = list->head;
    void *data = malloc(list->data_size);
    memcpy(data, temp->data, list->data_size);

    list->head = list->head->next;
    free(temp->data);
    free(temp);

    return data; // This is where the memory leak is.
}

void *get(List *list, int index) {
    Node *cur = list->head;
    while(cur != NULL && index-->0){
        cur = cur->next;
    }
    if (cur==NULL) {
        return NULL;
    }
    
    void *data = malloc(list->data_size);
    memcpy(data, cur->data, list->data_size);
    return data;
}

int length(List *list) {
    int len = 0;
    Node *cur = list->head;
    while(cur != NULL) {
        cur = cur->next;
        len++;
    }
    return len;
}
