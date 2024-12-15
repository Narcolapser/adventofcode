#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include "assertions.h" // Assuming assertions from the earlier example
#include "list.h"

void run_test(void (*test)(), const char *test_name);

void test_parsing_line() {
    Node *head = NULL;
    char *line = "7 6 4 2 1";
    parse_line(&head, line);

    ASSERT_EQUAL(head->val, 7);
    ASSERT_EQUAL(head->next->val, 6);
    ASSERT_EQUAL(head->next->next->val, 4);
    ASSERT_EQUAL(head->next->next->next->val, 2);
    ASSERT_EQUAL(head->next->next->next->next->val, 1);
}

// Implementation
void run_test(void (*test)(), const char *test_name) {
    printf("Running test: %s\n", test_name);
    test();
    printf("Test passed: %s\n", test_name);
}

int main() {
    run_test(test_parsing_line, "parsing_line");

    printf("All tests passed!\n");
    return 0;
}
