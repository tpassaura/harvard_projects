def main():
    # Define list of months
    months = {
        "January" : 1,
        "February" : 2,
        "March" : 3,
        "April" : 4,
        "May" : 5,
        "June" : 6,
        "July" : 7,
        "August" : 8,
        "September" : 9,
        "October" : 10,
        "November" : 1,
        "December" : 12
    }

    while True:
        try:
            # Get user input
            date = input("Date: ").strip()
            # Check if fomart is alphabetic
            if date[0].isalpha():
                # Extract month and year
                date = date.split()
                month = date[0]
                year = date[2]
                # check and Extract day
                if date[1][-1] != ",":
                    pass
                else:
                    day = int(date[1].split("," , 1)[0])
                # Validade values
                if month in months:
                        month = months[month]
                        if 0 < day <= 31:
                            if len(year) == 4:
                                #print result
                                print(f"{year}-{month:02}-{day:02}")
                                break
            # Check if fomart is numeric
            elif date[0].isdigit():
                # Extract day, month and year
                date = date.split("/")
                month = int(date[0])
                day = int(date [1])
                year = date[2]
                # Validade values
                if 0 < month <= 12:
                    if 0 < day <= 31:
                        if len(year) == 4:
                             #print result
                            print(f"{year}-{month:02}-{day:02}")
                            break
            else: pass

        except:
            pass



main()