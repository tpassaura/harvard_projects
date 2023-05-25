from datetime import datetime, timedelta, date
import inflect
import sys
import traceback

def main():
    print(convert(input("Date of Birth: ")))


def convert(birthday):
    current_date = date.today()

    try:
        birthday = datetime.strptime(birthday, "%Y-%m-%d").date()

        days_of_life = (current_date - birthday).days
        minutes_of_life = days_of_life * 24 * 60

        p = inflect.engine()
        minutes_in_words = p.number_to_words(minutes_of_life, andword="").capitalize()
        return f"{minutes_in_words} minutes"

    except:
        sys.exit("Invalid date")

if __name__ == "__main__":
    main()