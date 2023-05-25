import re
import sys


def main():
    try:
        result = convert(input("Hours: "))
        if result is not None:
            print(result)
    except ValueError as e:
        print("ValueError")
        sys.exit(1)


def convert(s):
    pattern = r'(\d{1,2})(?::(\d{2}))?\s?(AM|PM) to (\d{1,2})(?::(\d{2}))?\s?(AM|PM)'

    matches = re.findall(pattern, s)

    if matches:
        converted_times = []
        for match in matches:
            start_hour = int(match[0])
            start_minute = match[1] if match[1] else '00'
            start_meridian = match[2]

            end_hour = int(match[3])
            end_minute = match[4] if match[4] else '00'
            end_meridian = match[5]

            if (start_hour == 12 and start_meridian == 'AM') or (end_hour == 12 and end_meridian == 'AM'):
                start_hour = 0
            elif (start_hour == 12 and start_meridian == 'PM') or (end_hour == 12 and end_meridian == 'PM'):
                end_hour = 0

            if (start_hour >= 12 and start_meridian == 'AM') or (end_hour >= 12 and end_meridian == 'AM'):
                raise ValueError

            if start_meridian == 'PM' and start_hour != 12:
                start_hour += 12
            elif start_meridian == 'AM' and start_hour == 12:
                start_hour = 0

            if end_meridian == 'PM' and end_hour != 12:
                end_hour += 12
            elif end_meridian == 'AM' and end_hour == 12:
                end_hour = 0

            if start_hour >= 24 or end_hour >= 24 or int(start_minute) >= 60 or int(end_minute) >= 60:
                raise ValueError

            converted_times.append('{:02d}:{:02s}'.format(start_hour, start_minute))
            converted_times.append('{:02d}:{:02s}'.format(end_hour, end_minute))

        return ' to '.join(converted_times)
    else:
        raise ValueError

if __name__ == "__main__":
    main()
