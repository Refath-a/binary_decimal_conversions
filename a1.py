'''
Name: Refath Ahmed
Student #: 501085287
This program asks the user if they want to convert from binary to decimal or from decimal to binary. The user gets the
choice to choose the conversion the would like to perform.
'''
# This function asks the user which conversion they want to perform
# An while loop runs until the user inputs the correct command for the choice of the conversion
def conversion_choice():
    # Asks the user if they want to convert from binary to decimal or from decimal to binary
    # input 'decimal' converts to decimal and input 'binary' converts to binary
    choice = str(input("Enter 'decimal' for binary to decimal or 'binary' for decimal to binary: "))
    # Loop will continue to run until the user inputs the value 'decimal' or 'binary'
    # The loop will continue to print an invalid message as long as the input is not 'decimal' or 'binary'
    while True:
        if choice.lower() == 'decimal' or choice.lower() == 'binary': # the input is not case-sensitive due to the .lower() method
            break  # breaks out of the while loop if input is 'decimal' or 'binary'
        else:
            print("Your input is not valid!")  # if input is not 'decimal' or 'binary' then invalid message will print and loop will run all over again
            choice = str(input("Please enter 'decimal' for binary to decimal or 'binary' for decimal to binary: "))  # asks for choice again
    return choice.lower()
# This function checks to see if the user input is a valid decimal number
# The output to user will depend on input in function conversion_choice
def valid_input_decimal():
    valid = False  # boolean to determine if the value is valid
    # All the accepted values for a decimal number
    decimal_numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    # while loop runs while the input is an invalid number that is not contained within the decimal_numbers list
    while valid == False:
        valid = True  # set to true to break out of loop if number is valid
        num = input("Enter a decimal number: ")
        for i in num:
            if i not in decimal_numbers:  # checks every character in the string to see if any character is not in the decimal_numbers list
                print("Your input is not valid!")  # prints an invalid input message
                valid = False  # valid is set to False so the while loop runs again until a valid number is inputted
                break
    return num
# This function checks to see if the user input is a valid binary number
# The output to user will depend on input in function conversion_choice
def valid_input_binary():
    valid = False # boolean to determine if the value is valid
    # All the accepted values for a binary number
    binary_numbers = ['0', '1']
    # while loop runs while the input is an invalid number that is not contained within the binary_numbers list
    while valid == False:
        valid = True  # set to true to break out of loop if number is valid
        num = input("Enter a binary number: ")
        for i in num:
            if i not in binary_numbers:  # checks every character in the string to see if any character is not in the decimal_numbers list
                print("Your input is not valid!") # prints an invalid input message
                valid = False  # valid is set to False so the while loop runs again until a valid number is inputted
                break
    return num
# This function uses the input num which is obtained from the valid_input_binary function
# The function will output the conversion from binary to decimal
def binary_conversion(num):
    num_list = []  # empty list to store each binary number converted to powers of 2
    decimal = 0  # stores the conversion from binary to decimal
    for i in num:  # for every number in num it is added to the num_list
        num_list.append(int(i))
    num_list.reverse()  # the list is reversed as the conversion starts from the right to the left in powers of 2
    for i in range(len(num_list)):  # for every binary num on the list
        decimal += (num_list[i] * (2 ** i))  # each binary number is multiplied to 2 to the power of its position from the right
    print(f'The conversion to decimal is {decimal}')  # the conversion is then printed
# This function uses the input num which is obtained from the valid_input_decimal function
# The function will output the conversion from decimal to binary
def decimal_conversion(num):
    remainder_list = []  # stores all the remainders after each iteration of dividing the decimal number by 2
    quotient = int(num)  # the quotient is the num that was found in the valid_input_decimal function
    binary = ''  # stores the binary number after the conversion
    while quotient != 0:  # as long as the quotient is not 0 the loop will run
        remainder_list.append(quotient % 2)  # appends every iteration of the remainder from the quotient to the remainder_list
        quotient //= 2  # quotient after the number is divided by 2 after every iteration
    remainder_list.reverse()  # reverse the list as it is read from LSB to MSB or from down to up
    for i in remainder_list:  # add all the binary numbers in the list to the binary variable
        binary += str(i)
    print(f'The conversion to binary is {binary}')  # the binary number is then printed to the user


if __name__ == "__main__":
    choice = conversion_choice()
    if choice == "decimal":  # if the choice is 'decimal' in the conversion function
        binary_conversion(valid_input_binary())  # Then the number is converted to binary
    elif choice == "binary":  # if the choice is 'decimal' in the conversion function
        decimal_conversion(valid_input_decimal())  # Then the number is converted to binary


