import sys
import csv
import traceback

def main():
    try:
        # Check if size of argv is correct
        if len(sys.argv) != 3:
            raise ValueError
        # Get name of file
        input_name = sys.argv[1].strip()
        output_name = sys.argv[2].strip()
        # Check if it is a CSV file
        if input_name.split(".")[1] != "csv" and output_name.split(".")[1] != "csv" :
            raise ValueError
        else:
            # Separete names
            separate_names(input_name, output_name)


    except :
        traceback.print_exc()
        sys.exit(1)

def separate_names(input_name, output_name):
    with open(input_name) as input_file:
        reader = csv.DictReader(input_file)
        # Write new file
        with open(output_name, mode="w") as output_file:
            writer = csv.DictWriter(output_file, fieldnames = ["first", "last", "house"] )
            writer.writeheader()
            for row in reader:
                first_name = row["name"].split(',')[1]
                last_name = row["name"].split(',')[0].strip()
                house = row["house"]
                writer.writerow({"first":first_name, "last":last_name, "house":house})



if __name__ == "__main__":
    main()
