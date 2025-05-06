"""Laboratory Exercise 4 - by Dela Rosa, Leant Nathaniel I. """

# 1. Create a programmer defined function that will do the same as strcpy function.
print("\n--strcpy() programmer defined--")

def copyString(str1, str2):
    str1, str2 = str2, str1
    print(f"New string value for string1: {str1}")

print("*" * 25)
print("STRING COPY")
print("*" * 25)

string1 = input("Enter your first word (string 1):  ")
string2 = input("Enter your second word (string 2):  ")
copyString(string1, string2)


# 2. Create a programmers defined function that will do the same as strcmp function.
print("\n--strcmp() programmer defined--")

def compareString(str1, str2):
    if str1 > str2:
        print("positive")
    elif str1 < str2:
        print("negative")
    else:
        print("equal")

print("*" * 25)
print("STRING COMPARE")
print("*" * 25)

string1 = input("Enter your first word (string 1):  ")
string2 = input("Enter your second word (string 2):  ")
compareString(string1, string2)


# 3. Create a programmers defined function that will do the same as strcat function.
print("\n--strcat() programmer defined--")

def connectString(str1, str2):
    new_string = str1 + str2
    print(f"New string value for string1: {new_string}")

print("*" * 25)
print("STRING CONCATENATION")
print("*" * 25)

string1 = input("Enter your first word (string 1):  ")
string2 = input("Enter your second word (string 2):  ")
connectString(string1, string2)


# 4. Create a programmers defined function that will do the same as strlen function.
print("\n--strlen() programmer defined--")

def lengthString(string):
    str_length = 0
    for char in string:
        str_length += 1
    return str_length

print("~ Calculate String Length ~")
str_user = input("Enter your string:  ")
print("The length of your string is:", lengthString(str_user))


# 5. Create a program that will return a reverse string using pointer.
print("\n--reverse_string programmer defined--")

def reverseString(string):
    str_reverse = ""
    for char in string:
        str_reverse = char + str_reverse
    return str_reverse

print("~ Reversed String Display ~")
user_string = input("Enter your string:  ")
print("The original string is: ", user_string)
print("The reversed string is", reverseString(user_string))


