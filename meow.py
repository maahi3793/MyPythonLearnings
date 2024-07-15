# while loop

def meow(n):
    return print("Meow!")

def woof(n):
    return print("Woof!\n")


def main():

    x = int(input("Enter how many meows: "))
    y = int(input("Enter how many times you want the dog to bark: "))
    while x != 0:
        meow(x)
        x -= 1
    
    for i in range(y):
        woof(y)

main()
