#include <cs50.h>
#include <stdio.h>

int main(void)
{
int h;
do
{
     h = get_int ("HEIGHT?: ");
}
while (h<1 || h>8);

for(int i = 0; i<h; i++)
{
                for(int d=8; d>i; d--){
                        printf(" ");
                }
       for(int j=0; j<i;j++)
{
        printf("#");
}
           printf("\n");
}
}