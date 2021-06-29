# (32°F − 32) × 5/9 = 0°C

def conversion():
    F = eval(input("What is the temperature in Fahrenheit?\n"))
    C = round(((F - 32) * (5/9)),2)
    print("The temperature is", C, "degrees Celsius")

conversion()