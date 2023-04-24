# Binary Calculator

# Import the files needed.
import functions
  

print("Hi! This is the progam 'Binary Calculator'. Here you will be able to ask for:"
"\n1)Addition\n2)Subtraction\n3)Multiplication\n4)Division\n5)Conversion of decimal numbers to binary numbers and vicerversa.\n")

# Ask the type of calculation wanted.
type_calculation = input("What is the type of calculation that you want to perform? Enter a number from 0 to 5    ")
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
            # Check if the number given is > 0 and < 6
            if functions.check_number(type_calculation):
                break

        except ValueError:
            pass            

# Addition
if type_calculation == 1:
    print("You chose the Binary Addition option.")
    while True:
        print("Type 'end' at any moment if you want to return to the main menu.")   
        a = input("\nEnter the first binary number you want to use for the addition.   ")
        print(f"Your first number is {a}")
        b = input("Enter the second binary number you want to use for the addition.   ")
        print(f"Your second number is {b}")
        # Make sure that a has more digits than b
        # If it does not, set a = b and b = a
        if len(a) < len(b):
            x = a
            a = b
            b = x
        # Make sure a and b have the same number of digits
        for num in range(len(a) - len(b)):
            b = f"0{b}"
        # Check if the numbers entered have only binary digits. The numbers are still strings.
        if functions.check_binary(a, b):
            # The addition process starts.
            reversed_b = b[::-1]
            print(reversed_b)
            index_b = 0
            result = ""
            # 'carry' will be set to 1 if there is an addition of two ones. 
            carry = 0
            print(a[::-1])
            for digit in a[::-1]:
                a_int = int(digit)
                print(f"{a_int}: {type(a_int)}")
                b_int = int(reversed_b[index_b])
                print(f"{b_int}: {type(b_int)}")
                if carry == 0:
                    # If both digits are 0
                    if a_int == 0 and b_int == 0:
                        result = f"{result}0"
                        print("0:0")
                        print(f"{result}")
                    # If both of them are 1
                    elif a_int == 1 and b_int == 1:
                        result = f"{result}0"
                        carry = 1
                        print("1:1")
                        print(f"{result}")
                    # If only one of them is 1
                    else:
                        result = f"{result}1"
                        print("1:0 or 0:1")
                        print(f"{result}")
                elif carry == 1:
                    # If both digits are 0
                    if a_int == 0 and b_int == 0:
                        result = f"{result}1"
                        carry = 0
                        print("0:0 carry:1")
                        print(f"{result}")
                    # If both of them are 1
                    elif a_int == 1 and b_int == 1:
                        result = f"{result}1"
                        carry = 1
                        print("1:1 carry:1")
                        print(f"{result}")
                    # If only one of them is 1
                    else:
                        result = f"{result}0"
                        carry = 1
                        print("1:0 or 0:1 carry:1")
                        print(f"{result}")
                # The index of b increases by 1
                index_b += 1
            # Add the last carry of the addition if there is a carry
            if carry == 1:
                result = f"{result}1"
                carry = 0
            print(f"Result: {result[::-1]}")

        else:
            print("You have to enter just binary numbers. (only ones and zeros)")
            print(functions.check_binary(a, b))