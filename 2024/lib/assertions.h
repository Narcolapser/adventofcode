#ifndef ASSERTIONS_H
#define ASSERTIONS_H

#include <stdio.h>
#include <stdlib.h>

#define ASSERT_EQUAL(expected, actual) \
    if ((expected) != (actual)) { \
        printf("Test failed: %s:%d: expected %d, got %d\n", __FILE__, __LINE__, (expected), (actual)); \
        exit(1); \
    }

#define ASSERT_NOT_NULL(ptr) \
    if ((ptr) == NULL) { \
        printf("Test failed: %s:%d: pointer is NULL\n", __FILE__, __LINE__); \
        exit(1); \
    }

#define ASSERT_TRUE(condition) \
    if (!(condition)) { \
        printf("Test failed: %s:%d: condition is false\n", __FILE__, __LINE__); \
        exit(1); \
    }

#define ASSERT_FALSE(condition) \
    if (condition) { \
        printf("Test failed: %s:%d: condition is false\n", __FILE__, __LINE__); \
        exit(1); \
    }

#endif
