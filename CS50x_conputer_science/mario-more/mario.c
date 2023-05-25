#include <cs50.h>
#include <stdio.h>

//FUCTIONS PROTOTYPES
int userInput(void);
int draw(int height);

int main(void)
{
    int height = userInput();
    draw(height);
}

//FUNCTIONs DECLARATIONS

//GET USER INPUT
int userInput(void)
{
    int height;
    do
    {
        height = get_int("what't the height?\n");
    }
    while (height < 1 || height > 8);
    return height;
}

//DRAW
int draw(int height)
{
    //PRINT SPACES BEFORE
    for (int i = 0; i < height; i++)
    {
        for (int s = height - 1; s > i; s--)
        {
            printf(" ");
        }

        //PRINT FRIST ROW OF "#"
        for (int j = 0; j < i + 1; j++)
        {
            printf("#");
        }

        //PRINT MIDDLE SPACES
        printf("  ");

        //PRINT LAST ROW OF "#"
        for (int j = 0; j < i + 1; j++)
        {
            printf("#");
        }

        printf("\n");
    }
    return 1;
}