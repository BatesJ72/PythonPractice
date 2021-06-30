# (32°F − 32) × 5/9 = 0°C

# Specify valid input options
# valid_temps = []

# def create_list(num1, num2):
#     if num1 == num2:
#         return num1
#     else:
#         while (num1 < num2 + 1):
#             valid_temps.append(num1)
#             num1 += 1
#         return valid_temps

# create_list(-50000, 50000)

# OPTIONS = valid_temps[:]

val = ''
# Determine if user input a valid option
def is_valid(temp):
    try:
        val = int(temp)
    except ValueError:
        val = "That's not a number!"

def get_temp():
    temp = eval(input("What is the temperature in Fahrenheit?\n"))

    # if is_valid(temp):
    #     raise Exception("Invalid: Please enter a number!")
    # try:
    #     val = int(temp)
    # except ValueError:
    #     print("That's not a number!")

    is_valid(temp)

    if val == "That's not a number!":
        return val
    else:
        return temp

# Main function
def main():
    print("Let's get the temperature!")
    temp = get_temp()
    C = round(((temp - 32) * (5/9)),2)
    print(f"The temperature in Fahrenheit is {temp} and the temperature in Celsius is {C}")

main()