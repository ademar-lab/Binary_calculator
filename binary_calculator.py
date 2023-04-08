# Binary Calculator

# Import the files needed
import functions
  

print("Hi! This is the progam 'Binary Calculator'. Here you will be able to ask for:"
"\n1)Addition\n2)Subtraction\n3)Multiplication\n4)Division\n5)Conversion of decimal numbers to binary numbers and vicerversa.\n")

# Ask the type of calculation wanted
type_calculation = input("What is the type of calculation that you want to perform? Enter a number form 0 to 5    ")
try:
    type_calculation = int(type_calculation)
    if functions.check_number(type_calculation) == False:
        raise ValueError
    else:
        pass

except ValueError:
    while True:
        type_calculation = input("\nYou must type a number from 1 to 5. Type 'end' if you want to exit the program.    ")
        if type_calculation == 'end':
            quit()
        try:
            type_calculation = int(type_calculation)
            if functions.check_number(type_calculation):
                break

        except ValueError:
            pass            


# Addition
#if type_calculation == 1: