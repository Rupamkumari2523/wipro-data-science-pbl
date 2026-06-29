# Write a program to check if a given number is Positive, Negative, or Zero.
number = float(input("Enter a number: "))

if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")



# Write a program to check if a given number is odd or even.
number = int(input("Enter a number: "))

if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")


# Given two non-negative values, print true if they have the same last digit, otherwise print false.

# lastDigit(7, 17) → true
# lastDigit(6, 17) → false
# lastDigit(3, 113) → true

def lastDigit(a, b):
    return a % 10 == b % 10

print(lastDigit(7, 17))   # → true
print(lastDigit(6, 17))   # → false
print(lastDigit(3, 113))  # → true


# Write a program to print numbers from 1 to 10 in a single row with one tab space.
for i in range(1, 11):
    print(i, end="\t")


# Write a program to print even numbers between 23 and 57. Each number should be printed on a separate row.
for i in range(24, 58, 2):
    print(i)

# Write a program to print prime numbers between 10 and 99.
for num in range(10, 100):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)


# Write a program to print the sum of all the digits of a given number.
number = int(input("Enter a number: "))
sum_of_digits = 0

while number > 0:
    digit = number % 10
    sum_of_digits += digit
    number //= 10

print("The sum of all the digits is:", sum_of_digits)


# Write a program to reverse a given number and print it.

# Example 1: I/P: 1234 → O/P: 4321
# Example 2: I/P: 1004 → O/P: 4001

number = int(input("Enter a number: "))
reverse = 0

while number > 0:
    digit = number % 10
    reverse = reverse * 10 + digit
    number //= 10

print("The reversed number is:", reverse)

# Write a program to find if the given number is a palindrome or not.
# Example 1: I/P: 110011 → O/P: 110011 is a palindrome.
# Example 2: I/P: 1234 → O/P: 1234 is not a palindrome.
number = int(input("Enter a number: "))
original_number = number
reverse = 0

while number > 0:
    digit = number % 10
    reverse = reverse * 10 + digit
    number //= 10

if original_number == reverse:
    print(f"{original_number} is a palindrome.")
else:
    print(f"{original_number} is not a palindrome.")

