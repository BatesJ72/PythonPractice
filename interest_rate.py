def interest_rate():
    print("This program calculates a future value. ")
    p = eval(input("What is the principal amount invested?\n"))
    i = eval(input("What is the annual interest rate?\n"))
    y = eval(input("How many years will it accrue interest?\n"))
    print(f"Wow! You're investing ${p} for {y} years at {i}% interest!")
    for i in range(y):
        p = p + (1 * i)
    print(f"After {y} years, you'll have ${p}!")

interest_rate()