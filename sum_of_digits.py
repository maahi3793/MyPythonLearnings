def SumOfDigits(number):

    sum = 0
    while number > 0:
        sum = sum + number%10

        number = number//10
    return sum

def main():

    number1 = int(input("Enter a number: "))

    print(f"sum of the digits of the number is {SumOfDigits(number1)}")

main()