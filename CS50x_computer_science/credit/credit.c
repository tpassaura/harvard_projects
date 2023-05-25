#include <cs50.h>
#include <stdio.h>
int get_num_of_digits(long long a);
int get_cc_num(void);
int main(void)
{
//GET CREDIT CARD NUMBER
    long long ccn;
    do
    {
        ccn = get_long_long("Number: ");
    }
    while (ccn < 0);

//GET NUMBERS OF DIGITS
    int n = get_num_of_digits(ccn);

//CHECK IF THE NUMBER OF DIGITS IS VALID
    if (n != 13 && n != 15 && n != 16)
    {
        printf("INVALID\n");
    }
    else
    {
//MULTIPLY EVERY OTHER DIGIT
        int sum1 = 0;
        int sum2 = 0;
        long cc = ccn;
        int total = 0;
        int n1;
        int n2;
        int d1;
        int d2;
        do
        {
            n1 = cc % 10;
            cc = cc / 10;
            sum1 = sum1 + n1;

            n2 = cc % 10;
            cc = cc / 10;

            n2 = n2 * 2;
            d1 = n2 % 10;
            d2 = n2 / 10;
            sum2 = sum2 + d1 + d2;
        }
        while (cc > 0);
        total = sum1 + sum2;

//CHECK IF IS A VALID CARD NUMBER
        if (total % 10 != 0)
        {
            printf("INVALID\n");
        }
        else
        {
            //GET START DIGITS
            long sn = ccn;
            do
            {
                sn = sn / 10;
            }
            while (sn > 100);

            //CHECK IF IS VISA
            if (sn / 10 == 4)
            {
                printf("VISA\n");
            }
            //CHECK IF IS AMEX
            else if (sn == 34 || sn == 37)
            {
                printf("AMEX\n");
            }
            //CHECK IF IS MASTERCARD
            else if ((sn == 51) || (sn == 52) || (sn == 53) || (sn == 54) || (sn == 55))
            {
                printf("MASTERCARD\n");
            }

            else
            {
                printf("INVALID\n");
            }
        }
    }
}





//FUNCTIONS

//GET NUMBERS OF DIGITS
int get_num_of_digits(long long a)
{
    int num_digits = 0;
    while (a > 0)
    {
        a = a / 10;
        num_digits++;
    }
    return num_digits;
}

