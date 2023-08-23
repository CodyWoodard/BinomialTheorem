"""Created by Cody Woodard"""


def factorial(num):
    result = 1
    if num == 0:
        return 1
    if num < 0:
        return "Enter a non-negative number"
    for i in range(1, num + 1):
        result *= i
    return result


def choose(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))


def main():
    n = int(input("Enter a number to compute it's factorial"))
    k = int(input("Choose a number for k"))
    print(k)

    print(factorial(n))
    print(choose(n, k))
    print('You can do this.')



if __name__ == "__main__":
    main()
