# Calculator with functions

def main():
    x = int(input("Enter a number: "))
    print(f"square of {x} is:",square(x))

def square(n):
    return n * n


main()