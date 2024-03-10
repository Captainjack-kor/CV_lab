#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

int readInt();
void printMenu();

int totalCount = 0;
char memo[0x10][8];

int main(int argc, char** argv)
{
    setbuf(stdin, 0);
    setbuf(stdout, 0);
    printf("Welcome to Osori's diary\n");
    while(totalCount < 2)
    {
        printMenu();
        printf("> ");
        int select = readInt();
        if (select == 1)
        {
            printf("Select index : ");
            int idx = readInt();
            if (idx >= 0x10)
            {
                puts("Don't cheat!");
                return 0;
            }
            printf("Write your memo : ");
            read(0, &memo[idx], 8);
        }
        else if (select == 2)
        {
            printf("Select index : ");
            int idx = readInt();
            if (idx >= 0x10)
            {
                puts("Don't cheat!");
                return 0;
            }
            printf(memo[idx]);
        }
        else
        {
            break;
        }
        totalCount++;
    }
    puts("bye~");
    return 0;
}

void printMenu()
{
    puts("1. Write memo");
    puts("2. read memo");
    puts("3. exit");
}

int readInt()
{
    char num[4];
    read(0, &num, 4);
    return atoi(num);
}