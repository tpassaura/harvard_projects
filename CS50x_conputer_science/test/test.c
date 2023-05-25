#include <stdio.h>
#include <cs50.h>

int main(void)
{
    char *s = "hello";
    char *z = &s [0];

        printf("%p\n",s);
        printf("%p\n", z);
    }
