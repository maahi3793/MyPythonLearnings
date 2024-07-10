name = input("what's your name: ")
school = input("Where did you go to school: ")
town = input("which town: ")
print("Hello, " + name + " of " + town)
print("I know where you went for schooling and in which town:", school, town)


fullName = input("What's your Full Name: ").strip().title()
# instead of adding these two lines of methods to strip and capitalize title you can add them to the variable itself like above
# fullName = fullName.title().strip
# instead of giving another method in the next line like this fullName = fullName.strip() you can chain the methods

print(f"your full name is: {name},",fullName)


# Now let's separate the first name and the last name

myName = input("Please enter your Full Name: ").strip().title()

first, last = myName.split(" ")

print("Hello,",first)

# Now let's look at integers

