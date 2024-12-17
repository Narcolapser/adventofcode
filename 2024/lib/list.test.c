#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "list.h"
#include "assertions.h"

void test_init_list() {
    List my_list;
    init_list(&my_list, sizeof(int));
    ASSERT_TRUE(my_list.head == NULL);
    ASSERT_EQUAL(my_list.data_size, sizeof(int));
    free_list(&my_list);
}

void test_push() {
    List my_list;
    init_list(&my_list, sizeof(int));

    int val1 = 42, val2 = 84;
    push(&my_list, &val1);
    ASSERT_TRUE(my_list.head != NULL);
    ASSERT_EQUAL(*(int *)(my_list.head->data), 42);

    push(&my_list, &val2);
    ASSERT_EQUAL(*(int *)(my_list.head->data), 84);
    ASSERT_EQUAL(*(int *)(my_list.head->next->data), 42);

    free_list(&my_list);
}

void test_pop() {
    List my_list;
    init_list(&my_list, sizeof(int));

    int val1 = 42, val2 = 84, val3 = 168;
    push(&my_list, &val1);
    push(&my_list, &val2);
    push(&my_list, &val3);

    pop(&my_list);
    ASSERT_EQUAL(*(int *)(my_list.head->data), 84);
    ASSERT_EQUAL(*(int *)(my_list.head->next->data), 42);

    pop(&my_list);
    ASSERT_EQUAL(*(int *)(my_list.head->data), 42);

    pop(&my_list);
    ASSERT_TRUE(my_list.head == NULL);

    free_list(&my_list);
}

void test_append() {
    List my_list;
    init_list(&my_list, sizeof(int));

    int val1 = 42, val2 = 84, val3 = 168;
    append(&my_list, &val1);
    ASSERT_EQUAL(*(int *)(my_list.head->data), 42);

    append(&my_list, &val2);
    ASSERT_EQUAL(*(int *)(my_list.head->data), 42);
    ASSERT_EQUAL(*(int *)(my_list.head->next->data), 84);

    append(&my_list, &val3);
    ASSERT_EQUAL(*(int *)(my_list.head->data), 42);
    ASSERT_EQUAL(*(int *)(my_list.head->next->data), 84);
    ASSERT_EQUAL(*(int *)(my_list.head->next->next->data), 168);

    free_list(&my_list);
}

void test_free_list() {
    List my_list;
    init_list(&my_list, sizeof(int));

    int val1 = 42, val2 = 84, val3 = 168;
    push(&my_list, &val1);
    push(&my_list, &val2);
    push(&my_list, &val3);

    free_list(&my_list);
    ASSERT_TRUE(my_list.head == NULL);
}

// Implementation
void run_test(void (*test)(), const char *test_name) {
    printf("Running test: %s\n", test_name);
    test();
    printf("Test passed: %s\n", test_name);
}

int main() {
    run_test(test_init_list, "test_init_list");
    run_test(test_push, "test_push");
    run_test(test_pop, "test_pop");
    run_test(test_append, "test_append");
    run_test(test_free_list, "test_free_list");

    printf("All tests passed successfully.\n");
    return 0;
}
