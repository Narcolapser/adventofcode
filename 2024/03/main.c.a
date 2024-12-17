#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

enum STATE
{
    READY,
    M,
    U,
    L,
    OPEN_PAREN,
    LEFT,
    COMMA,
    RIGHT,
    CLOSE_PAREN,
    RESET,
};

int main() {
    FILE *file = fopen("./input.txt", "r");
    if (file == NULL) {
        perror("Error opening file");
        exit(2);
    }

    int ch;
    int val = 0;
    int temp = 0;
    int left = 0;
    int digit_counter = 0;
    enum STATE state = READY;
    while ((ch = fgetc(file)) != EOF) {
        if (state == RESET){
            temp = 0;
            left = 0;
            digit_counter = 0;
            state = READY;
        }
        if (ch == 'm' && state == READY) {
            state = M;
        } else if (ch == 'u' && state == M) {
            state = U;
        } else if (ch == 'l' && state == U) {
            state = L;
        } else if (ch  == '(' && state == L){
            state = OPEN_PAREN;
        } else if (ch >= '0' && ch <= '9' && (state == LEFT || state == RIGHT || state == OPEN_PAREN || state == COMMA)) {
            digit_counter++;
            temp = temp * 10 + ch - '0';
            if (state == OPEN_PAREN) {
                state = LEFT;
            } else if (state == COMMA) {
                state = RIGHT;
            }
        } else if (ch == ',' && state == LEFT) {
            if (digit_counter <= 3) {
                left = temp;
                state = COMMA;
                temp = 0;
                digit_counter = 0;
            } else {
                state = RESET;
            }
        } else if (ch == ')' && state == RIGHT) {
            if (digit_counter <= 3) {
                val += left * temp;
            } 
            state = RESET;
        } else {
            state = RESET;
        }
    }
    printf("The sum of the multiplications is: %d\n", val);
}