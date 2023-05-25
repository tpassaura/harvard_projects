import csv
import sys


def main():

    # TODO: Check for command-line usage
    if len(sys.argv) == 3:
        dataBase_name = sys.argv[1]
        dnaSequence_name = sys.argv[2]
    else:
        print("Usage: python dna.py data.csv sequence.txt")
        return

    # TODO: Read database file into a variable
    dataBase_file = open(f"./{dataBase_name}")
    dataBase_data = csv.DictReader(dataBase_file, delimiter=',')
    dataBase_list = list(dataBase_data)

    # TODO: Read DNA sequence file into a variable
    dnaSequence_file = open(f"./{dnaSequence_name}")
    dnaSequence_data = dnaSequence_file.read()

    # TODO: Find longest match of each STR in DNA sequence
    STR_max = []
    for i in range(1, len(dataBase_data.fieldnames)):
        STR = dataBase_data.fieldnames[i]
        STR_max.append(0)

        for index in range(len(dnaSequence_data)):
            STR_count = 0

            if dnaSequence_data[index:(index+len(STR))] == STR:
                j = 0
                while dnaSequence_data[(index + j):(index + j + len(STR))] == STR:
                    STR_count += 1
                    j += len(STR)
                if STR_max[i-1] < STR_count:
                    STR_max[i-1] = STR_count

    # TODO: Check database for matching profiles
    for i in range(len(dataBase_list)):
        matches = 0
        for j in range(1, len(dataBase_data.fieldnames)):
            if int(STR_max[j - 1]) == int(dataBase_list[i][dataBase_data.fieldnames[j]]):
                matches += 1
            if matches == (len(dataBase_data.fieldnames) - 1):
                print(dataBase_list[i]['name'])
                exit(0)
    print("No match")


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run

main()