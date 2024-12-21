#include "rule.h"

int list_index(List *list, int val) {
    int counter = 0;
    int len = length(list);
    while (counter < len) {
        int *value = (int *)get(list, counter);
        // printf("Checking at %d for %d, it is %d\n", counter, val, *value);
        if (*value == val) {
            return counter;
        }
        counter++;
    }
    return -1;
}

bool evaluate(Rule *rule, List *list) {
    int left_index = list_index(list, rule->left);
    int right_index = list_index(list, rule->right);
    return left_index < right_index;
}