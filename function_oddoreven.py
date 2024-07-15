# Odd or even

def Odd_Even(x):
    return True if x % 2 == 0 else False

def main():
    x = int(input("Enter a number: "))

    if Odd_Even(x) == True:
        print("Even Number")
    else:
        print("Odd Number")

main()