#include <stdio.h>
#include <stdlib.h>

typedef struct node {
    int val;
    struct node *next;
} Node;

int obCheck(Node *l){
    if (l == NULL) {
        fprintf(stderr, "Error: index out of bounds. \n");
        exit(1);
    } else {
        return 1;
    }
}

int length(Node *l){
    if (l == NULL) {
        return 0;
    } else {
        return 1 + length(l->next);
    }
}

int get(Node *l, int i){
    if (l == NULL) {
    }
    if (i >= 0) {
        return get(l->next, i-1);
    } else {
        return l->val;
    };
}

void push(Node **l, int i) {
    if (*l == NULL) {
        *l = calloc(1, sizeof(Node));
        (*l)->val = i;
        (*l)->next = NULL;
    } else {
        push(&((*l)->next), i);
    }
}

int pop(Node *l, int i) {
    obCheck(l);
    if (i == 1) {
        obCheck(l->next);
        Node *target = l->next;
        int ret = target->val;
        l->next = target->next;
        free(target);
        return ret;        
    } else {
        return pop(l, i-1);
    }
}