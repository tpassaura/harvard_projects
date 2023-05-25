#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>

int main(int argc, string argv[1])
{

    //TO SEE IF THE PROGRAM HAS ONLY 1 COMANDA-LINE ARGUMENT:
    if (argc != 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }

    //TO SEE IF IT'S ONLY DIGITS ON COMANDA-LINE ARGUMENT:
    for (int i = 0; i < strlen(argv[1]); i++)
    {
        if (!isdigit(argv[1][i]))
        {
            printf("Usage: ./caesar key\n");
            return 1;
        }
    }

    //TRANSFORM THE KEY INTO INT:
    int key = (atoi(argv[1]) % 26);

    //ASK THE PLAINTEXT:
    string plaintext = get_string("plaintext:  ");

    printf("ciphertext: ");

    //CALCULATIONS
    for (int j = 0; j < (strlen(plaintext)); j++)
    {

        if (isalpha(plaintext[j]))
        {
            if (islower(plaintext[j]))
            {
                printf("%c", (plaintext[j] - 97 + key) % 26 + 97);
            }
            else if (isupper(plaintext[j]))
            {
                printf("%c", (plaintext[j] - 65 + key) % 26 + 65);
            }
        }
        else
            //PRINT WITHOUT CHANGE
        {
            printf("%c", plaintext[j]);
        }
    }
    printf("\n");
}
