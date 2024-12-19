#include <stdio.h>
#include <stdlib.h>
#include "example.h"

char *forward = "XMAS";
char *reverse = "SAMX";

int scan_horizontal() {
    int ftrack = 0;
    int rtrack = 0;
    int count = 0;
    for(int j=0; j<HEIGHT; j++) {
        for(int i=0; i<WIDTH; i++) {
            if (grid[j][i] == forward[ftrack]){
                printf("Found a potential XMAS at %dx%d\n", j, i);
                ftrack++;
            } else {
                if (grid[j][i] == forward[0])
                    ftrack = 1;
                else
                    ftrack = 0;
            }

            if (ftrack == 4) {
                printf("XMAS found by %d,%d\n", j, i);
                count++;
                ftrack = 0;
            }

            if (grid[j][i] == reverse[rtrack]){
                printf("Found a potential SMAX at %dx%d\n", j, i);
                rtrack++;
            } else {
                if (grid[j][i] == reverse[0]){
                    rtrack = 1;
                } else {
                    rtrack = 0;
                }
            }

            if (rtrack == 4) {
                printf("SMAX found by %d,%d\n", j, i);
                count++;
                rtrack = 0;
            }
        }
    }
    return count;
}

int main() {
    int count = 0;
    count += scan_horizontal();

    printf("Count is: %d\n", count);
}