#Peerapat Taenprayut 673380288-6 sec 1
#Declare and print variables
age = 20
GPA = 3.49
fav_color = "Dark Blue"
is_student = True

print("age : ",age)
print("GPA : ",GPA)
print("Favorite Color : ",fav_color)
print("Is Student : ",is_student)

#Perform simple arithmetic
num1 = 21
num2 = 3

print("\nSum : ", num1 + num2)
print("Difference : ", num1 - num2)
print("Division : ",(num1 / num2))
print("Product : ", num1 * num2)

#String concatenation and f-strings
first_name = "Peerapat"
last_name = "Taenprayut"
full_name = first_name + " " + last_name

print(f"\nHello, {full_name}!")

#User input and type conversion
user_fav_num = input("\nPlease input your favorite number! : ")
print(f"type of the input : {type(user_fav_num)}")

if user_fav_num.isdigit():
    converted_input = int(user_fav_num)
    result = converted_input + 5
    print(f"Result : {result}")
else:
    print("The string is not numeric.")