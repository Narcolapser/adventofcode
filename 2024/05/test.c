#include <stdio.h>
#include <string.h>
#include "../lib/assertions.h"
#include "../lib/list.h"
#include "rule.h"


void test_index() {
    List update_list;
    init_list(&update_list, sizeof(int));
    int values[] = {75, 47, 61, 53, 29};
    for (int i = 4; i >= 0; i--) {
        push(&update_list, &values[i]);
    }

    ASSERT_EQUAL(list_index(&update_list, 1),-1);
    ASSERT_EQUAL(list_index(&update_list, 75),0);
    ASSERT_EQUAL(list_index(&update_list, 47),1);
    ASSERT_EQUAL(list_index(&update_list, 61),2);
    ASSERT_EQUAL(list_index(&update_list, 53),3);
    ASSERT_EQUAL(list_index(&update_list, 29),4);
}

void test_update_1_passes_example_1() {
    Rule rule = {47,53};
    List update_list;
    init_list(&update_list, sizeof(int));

    int values[] = {75, 47, 61, 53, 29};
    for (int i = 4; i >= 0; i--) {
        push(&update_list, &values[i]);
    }
    ASSERT_TRUE(evaluate(&rule, &update_list));
}

void test_update_4_fails_example_16() {
    Rule rule = {97,75};
    List update_list;
    init_list(&update_list, sizeof(int));

    int values[] = {75,97,47,61,53};
    for (int i = 4; i >= 0; i--) {
        push(&update_list, &values[i]);
    }
    ASSERT_FALSE(evaluate(&rule, &update_list));
}

// Implementation
void run_test(void (*test)(), const char *test_name) {
    printf("Running test: %s\n", test_name);
    test();
    printf("Test passed: %s\n", test_name);
}

int main() {
    run_test(test_index, "Testing Index function");
    run_test(test_update_1_passes_example_1, "Testing u1r1");
    run_test(test_update_4_fails_example_16,"testing u4r16");
    printf("Passed\n");
}