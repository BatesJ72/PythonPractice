from side_by_side import print_side_by_side

def main():
    print("This program illustrates a chaotic function.\n")
    n = eval(input("How many numbers should I print?\n"))
    x = eval(input("Enter a number between 0 and 1.\n"))
    for i in range(n):
        x = 2.0 * x * (1 - x)
        print(x)

main()