# Let's code a calculator

x = int(input("enter a number: "))
y = int(input("Enter another number: "))

z = x + y

print(z)
print(f"{z:,}")


a = float(input("enter a fraction number: "))
b = float(input("enter another fraction number: "))

c = a + b

print(c)
print(round(c))


num1 = float(input("enter any number: "))
num2 = float(input("enter any number again: "))

div = num1 / num2

print(div)
print(f"{div:,.2f}")