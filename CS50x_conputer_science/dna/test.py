import csv
import sys


def main():

    dnaSequence_data = "ABCDABCDABCDABCDEEEABCDABCDABCDABCDABCD"


    #TODO: Find longest match of each STR in DNA sequence
    STR_max = 0
    STR = "ABCD"
    STR_count = 0
    index = 0
    while index in range (0, len(dnaSequence_data)):

        if dnaSequence_data[index:(index+len(STR))] == STR:
            STR_count += 1
            index = STR_count*(len(STR))+STR_max*len(STR)
        elif dnaSequence_data[index:(index+len(STR))] != STR:
            index += 1
            if STR_max < STR_count:
                STR_max = STR_count
            STR_count = 0

    print(STR_max)

main()






