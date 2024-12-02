#include <stdio.h>
#include "list.h"

int main() {
    Node *list = NULL;

    push(&list, 10);
    push(&list, 20);
    push(&list, 30);

    printf("Length: %d\n", length(list));
    printf("Element at index 1: %d\n", get(list, 1));

    return 0;
}