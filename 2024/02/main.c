#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include "list.h"

#define MAX_LINE_LENGTH 256 // Define maximum line length for a line in the file

int main() {
    const char *fname = "./input.txt"; // Path to the file
    FILE *file = fopen(fname, "r");

    if (!file) {
        fprintf(stderr, "Error: Could not open file %s\n", fname);
        return EXIT_FAILURE;
    }

    char line[MAX_LINE_LENGTH];
    int safe_count = 0;

    // Read each line from the file
    while (fgets(line, sizeof(line), file)) {
        // Remove the newline character, if present
        size_t len = strlen(line);
        if (len > 0 && line[len - 1] == '\n') {
            line[len - 1] = '\0';
        }

        // Perform some action with the line
        Node *head = NULL;
        parse_line(&head, line);
        bool sorted = sorted_check(head);
        bool spaced = spacing_check(head);
        bool safe = sorted && spaced;
        safe ? safe_count++ : safe_count;
        printf("Processing line: %s, sorted: %s spaced: %s\n", line, sorted?"true":"false", spaced?"true":"false" );
    }
    printf("there were %d safe lines\n", safe_count);

    fclose(file);
    return EXIT_SUCCESS;
}