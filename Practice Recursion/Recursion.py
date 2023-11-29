import math 


def main():
    print("Options you have!!!")
    print("\t1. Calculate Factorial of a Number\n\t2. Calculate sum of digits\n\t3. Check Palindrome Number\n\t4. Check Armstrong Number\n\t5. Generate a Fibonacci Series")
    foo = int(input("Enter Choice: "))

    match foo:
        case 1: 
            n = int(input("Enter a number to find it's factorial: "))
            print(f"Factorial of the number = {fact(n)}")
        case 2: 
            n = int(input("Enter a number to find sum of it's digits: "))
            print(f"Sum of the digits of the number: {sum_of_digits(n)}")
        case 3: 
            n = input("Enter a number or a text for Palindrome check: ")
            print(is_palindrome_number(n))
        case 4: 
            n = int(input("Enter a number for Armstrong Check: "))
            print(armstrong(n))
        case 5:
            n = int(input("Enter a length of Fibonacci series to print: "))
            print(fibonacci(n))
        case _:
            print("Wrong choice!")


# Factorial of a number
def fact(n):
    if n==0:
        return 1
    elif n==1:
        return 1
    else:
        return n * fact(n-1)


# Sum of digits
def sum_of_digits(n):
    return n if n < 10 else n % 10 + sum_of_digits(n // 10)


# Palindrome Check
def is_palindrome_number(s):
    return _is_palindrome_number_helper(s)
def _is_palindrome_number_helper(s):
    if len(s) <= 1:
        return "Palindrome!"
    elif s[0] == s[-1]:
        return _is_palindrome_number_helper(s[1:-1])
    else:
        return "Not Palindrome!"


# Armstrong check
def armstrong(n):
    bar = n
    length = len(str(n))
    def armstrong_helper(n, length):
        return n if n < 10 else pow(n % 10, length) + armstrong_helper(n//10, length)
    if armstrong_helper(n, length) == bar:
        return "Armstrong Number"
    else:
        return "Not Armstrong Number"
    

# Generate a Fibonacci Series
def fibonacci(n):
    if n == 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib = fibonacci(n - 1)
        fib.append(fib[-1] + fib[-2])
        return fib


if __name__ == '__main__':
    main()