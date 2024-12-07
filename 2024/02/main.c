#include <stdio.h>
#include <stdlib.h>
#include "list.h"

void read_file_to_list(const char *filename, Node **list) {
    FILE *file = fopen(filename, "r");
    if (file == NULL) {
        perror("Error opening file");
        exit(2);
    }

    int ch;
    int val = 0;
    while ((ch = fgetc(file)) != EOF) {
        if (ch >= '0' && ch <='9') {
            int num = ch - '0';
            val = val * 10 + num;
        } else {
            if (val)
                push(list, val);
            val = 0;
        }
    }
    if (val)
        push(list,val);
    fclose(file);
}

int main() {
    Node *head = NULL; // Start with an empty list

    read_file_to_list("./input.txt", &head);

    // Split list into two lists:
    Node *left = NULL;
    Node *right = NULL;
    print_list(head);
    while(length(head)){
        push(&left,pop(&head,0));
        push(&right,pop(&head,0));
    }

    // Print the list to verify
    print_list(left);
    print_list(right);

    // Solution for part 1
    // sort(&left);
    // sort(&right);

    // print_list(left);
    // print_list(right);

    // int sum_dif = 0;
    // while(length(left)) {
    //     int cur_dif = abs(pop(&left,0)-pop(&right,0));
    //     printf("Current diff: %d\n", cur_dif);
    //     sum_dif += cur_dif;
    // }
    // printf("The sum of the differences is: %d", sum_dif);

    // Solution for part 2
    int diff = 0;
    while(length(left)) {
        int val = pop(&left, 0);
        // printf("Searching for: %d\n", val);
        diff += count_instances(right, val) * val;
    }
    printf("Alt diff is: %d\n", diff);

    return 0;
}