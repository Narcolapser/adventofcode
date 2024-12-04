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

int pop(Node **head, int index) {
    if (*head == NULL) {
        fprintf(stderr, "Error: Index out of bounds.\n");
        exit(1);
    }

    // If the index is 0, remove the current node
    if (index == 0) {
        Node *temp = *head;      // Save the current node
        int val = temp->val;     // Extract its value
        *head = (*head)->next;   // Update the head pointer to skip this node
        free(temp);              // Free the removed node
        return val;              // Return the popped value
    }

    // Recursively call pop on the next node with index - 1
    return pop(&((*head)->next), index - 1);
}

void print_list(Node *current) {
    printf("List contents: ");
    while (current != NULL) {
        printf("%d ", current->val);
        current = current->next;
    }
    printf("\n");
}

void split(Node *source, Node **left, Node **right) {
    int len = length(source);
    int mid = len / 2;

    Node *current = source;
    Node *left_tail = NULL, *right_tail = NULL;

    for (int i = 0; i < mid; i++) {
        if (*left == NULL) {
            *left = current;
        } else {
            left_tail->next = current;
        }
        left_tail = current;
        current = current->next;
    }

    left_tail->next = NULL;

    for (int i = mid; i < len; i++) {
        if (*right == NULL) {
            *right = current;
        } else {
            right_tail->next = current;
        }
        right_tail = current;
        current = current->next;
    }

    right_tail->next = NULL;
}

Node *merge(Node *left, Node *right) {
    if (!left) return right;
    if (!right) return left;

    Node *result = NULL;

    if (left->val <= right->val) {
        result = left;
        result->next = merge(left->next, right);
    } else {
        result = right;
        result->next = merge(left, right->next);
    }

    return result;
}

void sort(Node **head) {
    if (*head == NULL || (*head)->next == NULL) {
        // Base case: Empty list or single element
        return;
    }

    Node *left = NULL;
    Node *right = NULL;

    // Split the list into two halves
    split(*head, &left, &right);

    // Recursively sort the two halves
    sort(&left);
    sort(&right);

    // Merge the sorted halves
    *head = merge(left, right);
}


