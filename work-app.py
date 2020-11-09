# program that calculates amount of time spent at work
print("Let's calculate how much time you spend at work.")
print("Please enter the number of days you work in a week.")
while True:
    val = input("Please enter a number")
    try:
        workDays = int(val)
        if int(val) > 7:
            print("Enter a number less than 7")
            continue
        break
    except ValueError:
        print("Please enter a number")
        continue
print("You work " + str(workDays) + " days a week")
