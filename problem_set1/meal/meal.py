def main():
    answer = input("What time is it ? ")
    time = convert(answer)
    if 7.0 <= time <=8.0:
        print("it’s customary to eat breakfast")
    elif 12.0 <= time <= 13.0 :
        print("it's customary to eat lunch")
    elif 18.0 <= time <= 19.0 :
        print("it's customary to eat dinner")
    else:
        pass     

     

def convert(time):
    hours, minutes = time.split(":")
    new_hours = float(hours)
    new_minutes = float(minutes)/60

    return new_hours + new_minutes


if __name__ == "__main__":
    main()