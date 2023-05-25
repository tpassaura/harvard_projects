#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for(int i = 0; i <= height ; i++)
    {
        for(int j = 0; j <= width; j++)
        {
            double red = (image[i][j].rgbtRed);
            double blue = (image[i][j].rgbtBlue);
            double green = (image[i][j].rgbtGreen);
            double bw_value = round((red + blue + green)/3);

            image[i][j].rgbtRed = bw_value;
            image[i][j].rgbtBlue = bw_value;
            image[i][j].rgbtGreen = bw_value;
        }
    }
     return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    int tmp[3];
    for(int i = 0; i < height ; i ++)
    {
        if(width %2 == 0)
        {
            for(int j = 0; j < (width/2); j++)
            {
                tmp[0] = image[i][j].rgbtRed;
                tmp[1] = image[i][j].rgbtBlue;
                tmp[2] = image[i][j].rgbtGreen;

                image[i][j].rgbtRed = image[i][width - 1 - j].rgbtRed;
                image[i][j].rgbtBlue = image[i][width - 1 - j].rgbtBlue;
                image[i][j].rgbtGreen = image[i][width - 1 - j].rgbtGreen;

                image[i][width - 1 - j].rgbtRed = tmp[0];
                image[i][width - 1 - j].rgbtBlue = tmp[1];
                image[i][width - 1 - j].rgbtGreen = tmp[2];
            }
        }
        else
        {
            for(int j = 0; j < ((width-1)/2); j++)
            {
                tmp[0] = image[i][j].rgbtRed;
                tmp[1] = image[i][j].rgbtBlue;
                tmp[2] = image[i][j].rgbtGreen;

                image[i][j].rgbtRed = image[i][width - 1 - j].rgbtRed;
                image[i][j].rgbtBlue = image[i][width - 1 - j].rgbtBlue;
                image[i][j].rgbtGreen = image[i][width - 1 - j].rgbtGreen;

                image[i][width - 1 - j].rgbtRed = tmp[0];
                image[i][width - 1 - j].rgbtBlue = tmp[1];
                image[i][width - 1 - j].rgbtGreen = tmp[2];
            }
        }
    }
    return;
}


// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    return;
}

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    return;
}
