#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
//#include "example.h"
#include "input.h"

char *forward = "XMAS";
char *reverse = "SAMX";

int scan_horizontal() {
    int count = 0;
    for(int j=0; j<HEIGHT; j++) {
        int ftrack = 0;
        int rtrack = 0;
        for(int i=0; i<WIDTH; i++) {
            if (grid[j][i] == forward[ftrack]){
                // printf("Found a potential XMAS at %dx%d\n", j, i);
                ftrack++;
            } else {
                if (grid[j][i] == forward[0])
                    ftrack = 1;
                else
                    ftrack = 0;
            }

            if (ftrack == 4) {
                // printf("XMAS found by %d,%d\n", j, i);
                count++;
                ftrack = 0;
            }

            if (grid[j][i] == reverse[rtrack]){
                // printf("Found a potential SMAX at %dx%d\n", j, i);
                rtrack++;
            } else {
                if (grid[j][i] == reverse[0]){
                    rtrack = 1;
                } else {
                    rtrack = 0;
                }
            }

            if (rtrack == 4) {
                // printf("SMAX found by %d,%d\n", j, i);
                count++;
                rtrack = 0;
            }
        }
    }
    return count;
}

int scan_vertical() {
    int count = 0;
    for(int i=0; i<HEIGHT; i++) {
        int ftrack = 0;
        int rtrack = 0;
        for(int j=0; j<WIDTH; j++) {
            if (grid[j][i] == forward[ftrack]){
                // printf("Found a potential XMAS at %dx%d\n", j, i);
                ftrack++;
            } else {
                if (grid[j][i] == forward[0])
                    ftrack = 1;
                else
                    ftrack = 0;
            }

            if (ftrack == 4) {
                // printf("XMAS found by %d,%d\n", j, i);
                count++;
                ftrack = 0;
            }

            if (grid[j][i] == reverse[rtrack]){
                // printf("Found a potential SMAX at %dx%d\n", j, i);
                rtrack++;
            } else {
                if (grid[j][i] == reverse[0]){
                    rtrack = 1;
                } else {
                    rtrack = 0;
                }
            }

            if (rtrack == 4) {
                // printf("SMAX found by %d,%d\n", j, i);
                count++;
                rtrack = 0;
            }
        }
    }
    return count;
}

bool check_next_se(int i, int j, int pos, char *str) {
    //printf("Checking potential match at %dx%d currently at %d\n",i,j,pos);
    if (pos == 3) {
        return true;
    } else if (i+1 == HEIGHT) {
        return false;
    } else if (j+1 == WIDTH) {
        return false;
    } else if (grid[i+1][j+1] == str[pos+1]) {
        return check_next_se(i+1, j+1, pos + 1, str);
    } else {
        return false;
    }
}

int scan_se() {
    int count = 0;
    for(int i=0; i<HEIGHT; i++) {
        for(int j=0; j<WIDTH; j++) {
            if (grid[i][j] == forward[0]) 
                if (check_next_se(i, j, 0, forward)) 
                    count += 1;
            if (grid[i][j] == reverse[0]) 
                if (check_next_se(i, j, 0, reverse)) 
                    count += 1;
        }
    }
    return count;
}

bool check_next_sw(int i, int j, int pos, char *str) {
    //printf("Checking potential match at %dx%d currently at %d\n",i,j,pos);
    if (pos == 3) {
        return true;
    } else if (i+1 == HEIGHT) {
        return false;
    } else if (j-1 < 0) {
        return false;
    } else if (grid[i+1][j-1] == str[pos+1]) {
        return check_next_sw(i+1, j-1, pos + 1, str);
    } else {
        return false;
    }
}

int scan_sw() {
    int count = 0;
    for(int i=0; i<HEIGHT; i++) {
        for(int j=0; j<WIDTH; j++) {
            if (grid[i][j] == forward[0]) 
                if (check_next_sw(i, j, 0, forward)) 
                    count += 1;
            if (grid[i][j] == reverse[0]) 
                if (check_next_sw(i, j, 0, reverse)) 
                    count += 1;
        }
    }
    return count;
}

int main() {
    int count = 0;
    count += scan_horizontal();
    count += scan_vertical();
    count += scan_se();
    count += scan_sw();

    printf("Count is: %d\n", count);
}