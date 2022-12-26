def main():
    timme = convert(input("What time is it? "))
    if 7.00 <= timme <= 8.00:
        print("Breakfast time")
    elif 12.00 <= timme <= 13.00:
        print("Lunch time")
    elif 18.00 <= timme <= 19.00:
        print("Dinner time")

def convert(time):
    time = time.replace(":",'.')
    return float (time)

if __name__ == "__main__":
    main()