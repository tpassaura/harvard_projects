from pyfiglet import Figlet
import sys

figlet = Figlet()
fonts = figlet.getFonts()

# Check if user input no argv.
if len(sys.argv) == 1:
    text = input("Input: ")
    print(f"output: \n{figlet.renderText(text)}")
# Check if user input only 2 argv.
elif len(sys.argv) == 3:
    # Check if frist argv is right.
    if sys.argv[1] == "-f" or sys.argv[1] == "--font"
        # Check if font exist.
        if sys.argv[2] in fonts:
            # Set font.
            figlet.setFont(font=sys.argv[2])
            # Get input, convert and print.
            text = input("Input: ")
            print(f"output:\n{figlet.renderText(text)}")
        else:
            sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")

else:
    sys.exit("Invalid usage")
