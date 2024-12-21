#include <stdbool.h>
#include "../lib/list.h"

typedef struct rule {
    int left;
    int right;
} Rule;

int list_index(List *list, int val);
bool evaluate(Rule *rule, List *list);