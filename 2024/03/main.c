#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

enum STATE
{
    READY,
    RESET,
    READ_COMMAND,
    READ_NUMBER,
    READ_SEPERATOR,
};

#define MAX_LINE_LENGTH 7

bool is_cmd_char(char ch) {
    switch (ch) {
        case 'd':
        case 'o':
        case 'n':
        case '\'':
        case 't':
        case 'm':
        case 'u':
        case 'l':
            return true;
            break;
        default:
            return false;
    }
}

bool is_number(char ch) {
    return ch >= '0' && ch <= '9'
}

int main() {
    FILE *file = fopen("./example.txt", "r");
    if (file == NULL) {
        perror("Error opening file");
        exit(2);
    }

    int ch;
    int val = 0;
    int temp = 0;
    
    int left = 0;
    int digit_counter = 0;

    char line[MAX_LINE_LENGTH];
    int line_ptr = 0;
    
    enum STATE state = RESET;
    bool isEnabled = true;

    while ((ch = fgetc(file)) != EOF) {
        switch (state) {
            case RESET:
                temp = 0;
                left = 0;
                digit_counter = 0;
                state = READ_COMMAND;
                for(int i=MAX_LINE_LENGTH; i-->0; line[i] = '\0');
                line_ptr = 0;
                fputc(ch,file);
                break;
            case READ_COMMAND:
                while(is_cmd_char(ch) && state == READ_COMMAND) {
                    line[line_ptr] = ch;
                    line_ptr++;
                    if (line_ptr > 5) {
                        state = RESET;
                        fputc(ch,file);
                        break;
                    }
                }
                if (state == RESET) { continue; }

                if (strcmp(line,"mul") && isEnabled) {
                    state = READ_NUMBER;
                } else if (strcmp(line,"do")) {
                    isEnabled = true;
                } else if (strcmp(line,"don't")) {
                    isEnabled = false;
                } else {
                    state = RESET;
                }
                break;
            case READ_NUMBER:
                while(is_number(ch) && state == READ_NUMBER) {
                    temp = temp * 10 + ch - '0';
                    digit_counter++;
                    if (digit_counter>3) {
                        state == RESET;
                        fputc(ch,file);
                        break;
                    }
                }

                if (state == RESET) { continue; }

                if (left == 0 && ch == ',') { // This works if left is parsed as 0 because anything times 0 is zero so it doesn't matter.
                    left = temp;
                    temp = 0;
                } else if (left != 0 && ch == ')') {
                    val += left * temp;
                    state = RESET;
                } else {
                    state = RESET;
                }
                break;
            default:
                state = RESET;
        }
    }
    printf("The sum of the multiplications is: %d\n", val);
}