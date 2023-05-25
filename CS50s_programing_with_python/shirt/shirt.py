import sys
from PIL import Image
from PIL import ImageOps
import traceback


def main():
    # Define variables
    input_name = sys.argv[1].lower()
    output_name = sys.argv[2].lower()
    input_extension = input_name.split(".")[-1]
    output_extension = output_name.split(".")[-1]
    # Check if the input if correct
    check_input(input_extension, output_extension)

    # Open shirt image
    try:
        input_file = Image.open(input_name)

    except:
        sys.exit(1)

    # Open shirt file
    shirt_img = Image.open("shirt.png")
    # Set image size
    size = shirt_img.size
    input_img = ImageOps.fit(input_file, size)
    # Join images
    input_img.paste(shirt_img, shirt_img)
    input_img.save(output_name)


def check_input(input_extension, output_extension):
    # if the user does not specify exactly two command-line arguments
    if len(sys.argv) != 3:
        sys.exit(1)
    # if the input’s and output’s names do not end in .jpg, .jpeg, or .png, case-insensitively,
    elif (
        input_extension != "jpg"
        and input_extension != "jpeg"
        and input_extension != "png"
    ):
        sys.exit(1)
    elif (
        output_extension != "jpg"
        and output_extension != "jpeg"
        and output_extension != "png"
    ):
        sys.exit(1)
    # if the input’s name does not have the same extension as the output’s name, or
    elif input_extension != output_extension:
        sys.exit(1)
    else:
        return 0


if __name__ == "__main__":
    main()
