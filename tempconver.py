# Program to convert Celcius to Fahrenheit

def Celcius_to_Fahrenheit(tempc):
    return tempc * 9/5 + 32

def Fahrenheit_to_Celcius(tempf):
    return (tempf - 32) * 5/9

def main():
    while True:
        choseConversion = input("Please pick the temperature unit you are about to enter (either C or F): ").strip().capitalize()
    
        if choseConversion == "C":
            tempInCelcius = int(input("Please enter Temperature in Celcius: "))
            print("Temperature converted to Fahrenheit is: ",Celcius_to_Fahrenheit(tempInCelcius))
            break
        elif choseConversion == "F":
            tempInFahrenheit = int(input("Please enter Temperature in Fahrenheit: "))
            print("Temperature converted to Celcius is: ",Fahrenheit_to_Celcius(tempInFahrenheit))
            break
        else:
            print("Please enter the right choice (Either C or F): ")


main()
