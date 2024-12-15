#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include "assertions.h" // Assuming assertions from the earlier example
#include "list.h"

void run_test(void (*test)(), const char *test_name);

void test_sorted_check_empty() {
    Node *head = NULL;
    ASSERT_TRUE(sorted_check(head));
}

void test_sorted_check_single_element() {
    Node node = {5, NULL};
    ASSERT_TRUE(sorted_check(&node));
}

void test_sorted_check_ascending() {
    Node n3 = {3, NULL};
    Node n2 = {2, &n3};
    Node n1 = {1, &n2};
    ASSERT_TRUE(sorted_check(&n1));
}

void test_sorted_check_descending() {
    Node n3 = {1, NULL};
    Node n2 = {2, &n3};
    Node n1 = {3, &n2};
    ASSERT_TRUE(sorted_check(&n1));
}

void test_sorted_check_unsorted() {
    Node n3 = {2, NULL};
    Node n2 = {3, &n3};
    Node n1 = {1, &n2};
    ASSERT_FALSE(sorted_check(&n1));
}

void test_spacing_check_empty() {
    Node *head = NULL;
    ASSERT_TRUE(spacing_check(head));
}

void test_spacing_check_single_element() {
    Node node = {5, NULL};
    ASSERT_TRUE(spacing_check(&node));
}

void test_spacing_check_valid_spacing() {
    Node n3 = {3, NULL};
    Node n2 = {2, &n3};
    Node n1 = {1, &n2};
    ASSERT_TRUE(spacing_check(&n1));
}

void test_spacing_check_invalid_spacing() {
    Node n3 = {10, NULL};
    Node n2 = {2, &n3};
    Node n1 = {1, &n2};
    ASSERT_FALSE(spacing_check(&n1));
}

void test_spacing_check_invalid_spacing_two_the_same() {
    Node n3 = {4, NULL};
    Node n2 = {4, &n3};
    Node n1 = {1, &n2};
    ASSERT_FALSE(spacing_check(&n1));
}

// Implementation
void run_test(void (*test)(), const char *test_name) {
    printf("Running test: %s\n", test_name);
    test();
    printf("Test passed: %s\n", test_name);
}

int main() {
    run_test(test_sorted_check_empty, "test_sorted_check_empty");
    run_test(test_sorted_check_single_element, "test_sorted_check_single_element");
    run_test(test_sorted_check_ascending, "test_sorted_check_ascending");
    run_test(test_sorted_check_descending, "test_sorted_check_descending");
    run_test(test_sorted_check_unsorted, "test_sorted_check_unsorted");

    run_test(test_spacing_check_empty, "test_spacing_check_empty");
    run_test(test_spacing_check_single_element, "test_spacing_check_single_element");
    run_test(test_spacing_check_valid_spacing, "test_spacing_check_valid_spacing");
    run_test(test_spacing_check_invalid_spacing, "test_spacing_check_invalid_spacing");
    run_test(test_spacing_check_invalid_spacing_two_the_same, "test_spacing_check_invalid_spacing_two_the_same");

    printf("All tests passed!\n");
    return 0;
}
