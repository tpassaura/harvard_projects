#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <math.h>

int count_letters(string text, int tl);
int count_words(string text, int tl);
int count_sentences(string text, int tl);
int main(void)
{
    //GET TEXT
    string text = get_string("TEXT: ");

    //GET TEXT LENGHT
    float tl = strlen(text);

    //GET NUMBEROF LETTERS
    float nl = count_letters(text, tl);

    //GET NUMBER OF WORDS
    float nw = count_words(text, tl);

    //GET NUMBER OF SENTENCES
    float ns = count_sentences(text, tl);

    //CALCULATE L
    float l = (nl * 100) / nw;

    //CALCULATE S
    float s = (ns * 100) / nw;

    //CALCULATE GRADE
    float index = (0.0588 * l - 0.296 * s - 15.8);

    int grade = round(index);

    //PRINT GRADE
    if (grade < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (grade > 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n", grade);
    }
}

//FUNCIONS


//GET NUMBEROF LETTERS
int count_letters(string text, int tl)
{
    int i = 0, count = 0;
    do
    {
        if (isalpha(text[i]))
        {
            count++;
            i++;
        }
        else
        {
            i++;
        }
    }
    while (i < tl);
    return count;
}


//GET NUMBER OF WORDS
int count_words(string text, int tl)
{
    int i = 0, count = 0;
    do
    {
        if (isspace(text[i]))
        {
            count++;
            i++;
        }
        else
        {
            i++;
        }
    }
    while (i < tl);
    return count + 1;
}

//GET NUMBER OF SENTENCES
int count_sentences(string text, int tl)
{
    int i = 0, count = 0;
    char s1 = '.', s2 = '!', s3 = '?';
    do
    {
        if (text[i] == s1 || text[i] == s2 || text[i] == s3)
        {
            count++;
            i++;
        }
        else
        {
            i++;
        }
    }
    while (i < tl);
    return count;
}