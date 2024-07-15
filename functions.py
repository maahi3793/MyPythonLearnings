# functions class

def Hello():
    print("Hello,",end=" ")

name = input("Please enter your name: ")
Hello()
print(name)


# More simplified or next step

def goodnight(to):
    print(f"GoodNight, {to}")

nickName = input("enter a nickname: ")
goodnight(nickName)

# you can also give a default value to the parameter

def goodmorning(to = "Mahi"):
    print("Good Morning,",to)

goodmorning()


# functions are usually used to avoid repetative tasks

