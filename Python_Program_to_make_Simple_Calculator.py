# Function to Add two numbers.
def Addition(num1,num2):
    return num1 + num2
# Function to Subtract two numbers. 
def Subtraction(num1,num2):
    return num1 - num2
# Function to Multiply two numbers.
def Multiply(num1,num2):
    return num1 * num2
# Function to Divide two Numbers.
def Divide(num1,num2):
    return(num1 / num2)
print("You can perform the varies operations.\n" \
          "1).Addition\n"\
          "2).Subtraction\n"\
          "3).Multiply\n"\
          "4).Division\n")
# Take input from User.
result = int(input("You have to Choose the 1 Operations :1,2,3,4 : "))
number_1 =int(input("Enter Number_1 :"))
number_2 =int(input("Enter Number_2 :"))
if result ==1:
    print( number_1,"+",number_2, "=",
          Addition(number_1,number_2))
elif result ==2:
    print( number_1,"-",number_2, "=",
          Subtraction(number_1,number_2))
elif result==3:
    print( number_1,"*",number_2, "=",
          Multiply(number_1,number_2))
elif result==4:
    print( number_1,"/",number_2, "=",
          Divide(number_1,number_2))
else:
    print("Invalid Operation")