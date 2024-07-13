# let me write this code based on the knowledge i have so far

# comparing my code with the chatgpt code


#Write a Python program that calculates the area and perimeter of a rectangle and the area and circumference of a circle. The program should:

#Prompt the user to choose between calculating the properties of a rectangle or a circle.
#For a rectangle, prompt the user to input the length and width. For a circle, prompt the user to input the radius.
#Define separate functions for calculating the area and perimeter of a rectangle, and the area and circumference of a circle.
#Use conditionals to ensure that the length, width, and radius are positive numbers.
#Ensure the user inputs a valid shape option (rectangle or circle).
#Return and print the results of the calculations.

def area_rectangle(length,breadth):
    return length * breadth

def perimeter_rectangle(length,breadth):
    return 2 * (length + breadth)

def area_circle(radius):
    return 3.14 * radius * radius

def perimeter_circle(radius):
    return 2 * 3.14 * radius

def main():

    shape = input("select a shape between circle and rectangle: ").lower().strip()
    
    while shape not in ["rectangle", "circle"]:
        print("Please select only between rectangle and circle")
        shape = input("select a shape between circle and rectangle: ").lower().strip()

    if shape == 'rectangle':
        length = float(input("Enter the length of the rectangle: "))
        breadth = float(input("Enter the breadth of the rectangle: "))

        area = area_rectangle(length,breadth)
        print("Area of the rectangle is",area)

        perimeter = perimeter_rectangle(length,breadth)
        print("perimeter of the circle is",perimeter)

    elif shape == 'circle':
        radius = float(input("Enter the radius of the circle: "))

        area = area_circle(radius)
        print(f"Area of the circle is {area}")

        perimeter = perimeter_circle(radius)
        print(f"Perimeter of the circle is {perimeter}")


main()