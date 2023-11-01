import re

day_names = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
suckerType = ["flavored", "gum filled", "tootsie roll", "carmel apple"]
email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'


def main():

    favorite_sucker, suckersEaten, cost, date_input, email_input = input_data()
    sumSuckers, totalCost, avgSuckers = calcs(suckersEaten, cost)
    header()
    output(favorite_sucker, suckersEaten, cost, sumSuckers, totalCost, avgSuckers, date_input, email_input)


def input_data():
    global email_pattern
    date_pattern = r'^\d{2}/\d{2}/\d{4}$'
    while True:
        date_input = input("Enter a date (mm/dd/yyyy): ").strip()
        if re.match(date_pattern, date_input):
            break
        else:
            print("Invalid date format. Please use mm/dd/yyyy.")

    while True:
        email_input = input("Enter your email address: ")
        if re.match(email_pattern, email_input):
            break
        else:
            print("Invalid email address. Please enter a valid email.")
    favorite_sucker = ""
    while favorite_sucker not in suckerType:
        favorite_sucker = input(
            f"Which sucker is your favorite? ({suckerType[0]}, {suckerType[1]}, {suckerType[2]}, {suckerType[3]}): ").lower()
        if favorite_sucker == suckerType[0]:
            print("You chose a flavored sucker.")
            break
        elif favorite_sucker == suckerType[1]:
            print("You chose a gum-filled sucker.")
            break
        elif favorite_sucker == suckerType[2]:
            print("You chose a tootsie roll sucker.")
            print("These are the best suckers!!!")
            break
        elif favorite_sucker == suckerType[3]:
            print("You chose a caramel apple sucker.")
            print("these are great except they stick to your teeth!")
            break
        else:
            print("Unknown sucker type. Please choose from: flavored, gumFilled, tootsieRoll, carmelApple.")

    daysTotal = []
    for day in range(7):
        while True:
            try:
                suckersEaten = int(input(f"How many {favorite_sucker} suckers did you eat on {day_names[day]}? "))
                daysTotal.append(suckersEaten)
                break
            except ValueError:
                print("Enter a valid numeric value for suckers eaten.")

    while True:
        try:
            cost = float(input("How much do you pay for a sucker?: $"))
            break
        except ValueError:
            print("Enter a valid cost.")

    return favorite_sucker, daysTotal, cost, date_input, email_input


def calcs(suckersEaten, cost):
    sumSuckers = sum(suckersEaten)
    totalCost = cost * sumSuckers
    avgSuckers = sumSuckers / len(suckersEaten)
    return sumSuckers, totalCost, avgSuckers


def header():
    print("Day   | Suckers Eaten | Average Daily Sucker Amount | Cost")


def output(favorite_sucker, daysTotal, cost, sumSuckers, totalCost, avgSuckers, date_input, email_input):
    for day in range(7):
        # length of code to show to user is used with len.. so i used len to alot for displayed length of characters i want shown.
        print(f"{day_names[day]} | {daysTotal[day]:.2f} | {daysTotal[day] / len(daysTotal):.2f} | {cost:.2f}")
    print(f"Total: {sumSuckers:.2f} | Average: {int(avgSuckers)} | Total Cost: ${totalCost:.2f}")
    print(f"Date: {date_input}")
    print(f"Email: {email_input}")


main()
