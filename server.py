"""Created by Cody Woodard"""

# This function is taking the user input and arithmetically manipulating it, resulting in the factorial of said number.
# if user input is 0, then 1 is assigned instead because 0! = 1.
# If user input is less than 0 the message "Enter a non-negative number" is printed,
# because The factorials of negative integers cannot be computed,
# since for n = 0, the recurrence relation, Thus (n-1)! = n!/n and you can't divide by 0.
# (I am sure there is a better way to code error handling in Python, and I will update this soon.)
# The for loop on line 20 is simple, I am multiplying the current value of i with the result variable,
# result is then updated to the new value ie: 1 * 2 = 2, result now = 2, then 2 * 3 = 6, result = 6 and so on until
# the loop as iterated through the size of the user input.


def factorial(num):
    result = 1
    if num == 0:
        return 1
    if num < 0:
        return "Enter a non-negative number"
    for i in range(1, num + 1):
        result *= i
    return result

# Choose function takes both user inputs n & k, and sends them in as arguments to the factorial function created above.
# this is the "choose" equation in combinatorics. Where 4C2, "4 choose 2", means I have 4 objects/items/people etc.
# and I want to "choose" 2 from that set of 4 where order doesn't matter.
# Here is the formula for 4C2: nCk = n!/k!(n-k)!, where n is the total number of items (in this case 4)
# and k is the number of items you are choosing.
# 4C2 = 4!/2!(4-2)! = 6.


def choose(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))


def main():

    # I know this needs error handling, I will figure out a solution either today or tomorrow.
    n = int(input("Enter a number to compute it's factorial "))
    k = int(input("Choose a number for k "))


    print(factorial(n))
    print(choose(n, k))
    print('You can do this.')


if __name__ == "__main__":
    main()
