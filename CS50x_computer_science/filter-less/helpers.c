#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i <= height ; i++)
    {
        for (int j = 0; j <= width; j++)
        {
            double red = (image[i][j].rgbtRed);
            double blue = (image[i][j].rgbtBlue);
            double green = (image[i][j].rgbtGreen);
            double bw_value = round((red + blue + green) / 3);

            image[i][j].rgbtRed = bw_value;
            image[i][j].rgbtBlue = bw_value;
            image[i][j].rgbtGreen = bw_value;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height ; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int sepiared = round((0.393 * image[i][j].rgbtRed) + (0.769 * image[i][j].rgbtGreen) + (0.189 * image[i][j].rgbtBlue));
            int sepiagreen = round((0.349 * image[i][j].rgbtRed) + (0.686 * image[i][j].rgbtGreen) + (0.168 * image[i][j].rgbtBlue));
            int sepiablue = round((0.272 * image[i][j].rgbtRed) + (0.534 * image[i][j].rgbtGreen) + (0.131 * image[i][j].rgbtBlue));

            if (sepiared > 255)
            {
                sepiared = 255;
            }
            if (sepiagreen > 255)
            {
                sepiagreen = 255;
            }
            if (sepiablue > 255)
            {
                sepiablue = 255;
            }

            image[i][j].rgbtRed = sepiared;
            image[i][j].rgbtGreen = sepiagreen;
            image[i][j].rgbtBlue = sepiablue;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE tmp;
    for (int i = 0; i < height ; i ++)
    {
        if (width % 2 == 0)
        {
            for (int j = 0; j < (width / 2); j++)
            {
                tmp = image[i][j];
                image[i][j] = image[i][width - 1 - j];
                image[i][width - 1 - j] = tmp;
            }
        }
        else
        {
            for (int j = 0; j < ((width - 1) / 2); j++)
            {
                tmp = image[i][j];
                image[i][j] = image[i][width - 1 - j];
                image[i][width - 1 - j] = tmp;
            }
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE temp[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int sum_red = 0;
            int sum_green = 0;
            int sum_blue = 0;
            float counter = 0.00;

            //GET PIXIELS
            for (int x = -1; x < 2; x++)
            {
                for (int y = -1; y < 2; y++)
                {
                    int currentx = i + x;
                    int currenty = j + y;

                    if (currentx < 0 || currentx > (height - 1) || currenty < 0 || currenty > (width - 1))
                    {
                        continue;
                    }

                    sum_red += image[currentx][currenty].rgbtRed;
                    sum_green += image[currentx][currenty].rgbtGreen;
                    sum_blue += image[currentx][currenty].rgbtBlue;

                    counter++;
                }

                temp[i][j].rgbtRed = round(sum_red / counter);
                temp[i][j].rgbtGreen = round(sum_green / counter);
                temp[i][j].rgbtBlue = round(sum_blue / counter);
            }
        }

    }

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            image[i][j].rgbtRed = temp[i][j].rgbtRed;
            image[i][j].rgbtGreen = temp[i][j].rgbtGreen;
            image[i][j].rgbtBlue = temp[i][j].rgbtBlue;
        }
    }
    return;
}