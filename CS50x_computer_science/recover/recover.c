#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    //CHECK VALID INPUT
    if (argc != 2)
    {
        printf("Usage: ./recover IMAGE");
        return 1;
    }

    //OPEN FILE
    char *input = argv[1];
    FILE *input_file = fopen(input, "r");

    //CHECK IF THE FILE IS VALID
    if (input_file == NULL)
    {
        printf("INVALID FILE");
        return 2;
    }

    //VARIABLES
    unsigned char buffer[512];
    int counter = 0;
    FILE *output_file = NULL;
    char file_name[8];

    //READ 512 BYTES OF THE FILE AND STORE ON BUFFER
    while (fread(&buffer, sizeof(char), 512, input_file) != 0)
    {
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            sprintf(file_name, "%03i.jpg", counter);
            output_file = fopen(file_name, "w");
            counter++;
        }

        if (output_file != NULL)
        {
            fwrite(buffer, sizeof(char), 512, output_file);
        }
    }

    fclose(output_file);
    fclose(input_file);
    return 0;
}