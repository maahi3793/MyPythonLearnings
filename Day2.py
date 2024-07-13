# Odd or even

x = 20

if x % 2 == 0:
    print("even")
else:
    print("odd")


# Leap year or not

year = 2100

if year % 400 == 0:
    print("leap Year")
elif year % 100 == 0:
    print("Not Leap Year")
elif year % 4 == 0:
    print("leap year")



# Prime number or not

num1 = int(input("enter a number to check prime or not: "))
count = 0
for i in range(2, num1):
    if num1 % i == 0:
        count = count + 1
        print("Number is divisible by: ",i)

if count > 0 or num1 <=1:
    print("not a prime number")
else:
    print("Prime Number")



# factorial

num2 = int(input("Enter a number for factorial: "))
fact = 1

for i in range(1, num2 + 1):
    fact *= i

print(f"Factorial of the number is: {fact}")


# fibonacii series

a = 0
b = 1
fibo = 0
range1 = int(input("enter a number for range: "))

print(a)
for range1 in range(1, range1 + 1):
    print(b)
    fibo = a + b
    a = b
    b = fibo
