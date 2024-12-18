#include <stdio.h>
#include <string.h>
#include "list.h"
#include "assertions.h"

// Utility function to populate a list with integers
void populate_list(List *list, int *values, int size) {
    for (int i = 0; i < size; i++) {
        push(list, &values[i]);
    }
}

void run_test(void (*test)(), const char *test_name) {
    printf("Running test: %s\n", test_name);
    test();
    printf("Test passed: %s\n", test_name);
}

// Test for initializing a list
void test_init_list() {
    List my_list;
    init_list(&my_list, sizeof(int));
    ASSERT_EQUAL(my_list.head, NULL);
    ASSERT_EQUAL(my_list.data_size, sizeof(int));
    free_list(&my_list);
}

// Test for pushing values into the list
void test_push() {
    List my_list;
    init_list(&my_list, sizeof(int));

    int value1 = 10;
    int value2 = 20;
    push(&my_list, &value1);
    push(&my_list, &value2);

    ASSERT_EQUAL(*(int *)my_list.head->data, 20);
    ASSERT_EQUAL(*(int *)my_list.head->next->data, 10);
    ASSERT_EQUAL(my_list.head->next->next, NULL);

    free_list(&my_list);
}

// Test for appending values to the list
void test_append() {
    List my_list;
    init_list(&my_list, sizeof(int));

    int value1 = 10;
    int value2 = 20;
    append(&my_list, &value1);
    append(&my_list, &value2);

    ASSERT_EQUAL(*(int *)my_list.head->data, 10);
    ASSERT_EQUAL(*(int *)my_list.head->next->data, 20);
    ASSERT_EQUAL(my_list.head->next->next, NULL);

    free_list(&my_list);
}

// Test for popping values from the list
void test_pop() {
    List my_list;
    init_list(&my_list, sizeof(int));

    int value1 = 10;
    int value2 = 20;
    push(&my_list, &value1);
    push(&my_list, &value2);

    int *popped_value = (int *)pop(&my_list);
    ASSERT_EQUAL(*popped_value, 20);
    free(popped_value);

    popped_value = (int *)pop(&my_list);
    ASSERT_EQUAL(*popped_value, 10);
    free(popped_value);

    ASSERT_EQUAL(my_list.head, NULL);

    free_list(&my_list);
}

// Test for getting a value at a specific index
void test_get() {
    List my_list;
    init_list(&my_list, sizeof(int));

    int values[] = {5, 10, 15};
    populate_list(&my_list, values, 3);

    int *value_at_index_0 = (int *)get(&my_list, 0);
    int *value_at_index_1 = (int *)get(&my_list, 1);
    int *value_at_index_2 = (int *)get(&my_list, 2);

    ASSERT_EQUAL(*value_at_index_0, 15);
    ASSERT_EQUAL(*value_at_index_1, 10);
    ASSERT_EQUAL(*value_at_index_2, 5);

    free_list(&my_list);
}

// Test for checking the length of the list
void test_length() {
    List my_list;
    init_list(&my_list, sizeof(int));

    ASSERT_EQUAL(length(&my_list), 0);

    int values[] = {5, 10, 15};
    populate_list(&my_list, values, 3);

    ASSERT_EQUAL(length(&my_list), 3);

    free_list(&my_list);
}

// Main test runner
int main() {
    run_test(test_init_list, "test_init_list");
    run_test(test_push, "test_push");
    run_test(test_append, "test_append");
    run_test(test_pop, "test_pop");
    run_test(test_get, "test_get");
    run_test(test_length, "test_length");

    printf("All tests passed!\n");
    return 0;
}
