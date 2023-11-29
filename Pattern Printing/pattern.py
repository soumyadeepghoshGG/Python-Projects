def main():
    pattern_number = int(input("Enter the pattern number (1 to 22): "))
    if 1 <= pattern_number <= 22:
        pattern_function = globals().get(f"pattern_{pattern_number}")
        if pattern_function:
            pattern_function()
        else:
            print("Pattern not found.")
    else:
        print("Pattern number out of range.")


############# PATTERN 1 #############
def pattern_1():
    n = int(input("Enter the number of lines: "))
    for _ in range(n):
        for _ in range(n):
            print("*", end="")
        print()


############# PATTERN 2 #############
def pattern_2():
    n = int(input("Enter the number of lines: "))
    for i in range(1,n+1):
        for j in range(1,i+1):
            print("*", end="")
        print()


############# PATTERN 3 #############
def pattern_3():
    n = int(input("Enter the number of lines: "))
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j, end="")
        print()


############# PATTERN 4 #############
def pattern_4():
    n = int(input("Enter the number of lines: "))
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(i, end="")
        print()


############# PATTERN 5 #############
def pattern_5():
    n = int(input("Enter the number of lines: "))
    for i in range(n,0,-1):
        for j in range(i,0,-1):
            print("*", end="")
        print()


############# PATTERN 6 #############
def pattern_6():
    n = int(input("Enter the number of lines: "))
    for i in range(n,0,-1):
        for j in range(1,i+1):
            print(j, end="")
        print()


############# PATTERN 7 #############
def pattern_7():
    n = int(input("Enter the number of lines: "))
    for i in range(1, n+1):
        print(" " * (n - i), "*" * (2*i - 1))


############# PATTERN 8 #############
def pattern_8():
    n = int(input("Enter the number of lines: "))
    for i in range(n, 0, -1):
        print(" " * (n - i), "*" * (2*i - 1))


############# PATTERN 9 #############
def pattern_9():
    n = int(input("Enter the number of lines: "))
    if n % 2 == 0:
        mid = n // 2
        for i in range (1, mid+1):
            print(" " * (mid - i), "*" * (2*i - 1))
        for i in range(mid, 0, -1):
            print(" " * (mid - i), "*" * (2*i - 1))
    else:
        mid = n // 2 + 1
        for i in range (1, mid+1):
            print(" " * (mid - i), "*" * (2*i - 1))
        for i in range(mid-1, 0, -1):
            print(" " * (mid - i), "*" * (2*i - 1))


############# PATTERN 10 ############
def pattern_10():
    n = int(input("Enter the number of lines: "))
    if n % 2 == 0:
        mid = n // 2
        for i in range (1, mid+1):
            print("*" * i)
        for i in range(mid, 0, -1):
            print("*" * i)
    else:
        mid = n // 2 + 1
        for i in range (1, mid+1):
            print("*" * i)
        for i in range(mid-1, 0, -1):
            print("*" * i)


############# PATTERN 11 ############
def pattern_11():
    n = int(input("Enter the number of lines: "))
    for i in range(1, n+1):
        counter = 1
        for j in range(i):
            if (i % 2 == 1 and counter % 2 == 1) or (i % 2 == 0 and counter % 2 == 0):
                print(1, end="")
            elif (i % 2 == 0 and counter % 2 == 1) or (i % 2 == 1 and counter % 2 == 0):
                print(0, end="")
            counter += 1
        print()


############# PATTERN 12 ############
def pattern_12():
    n = int(input("Enter the number of lines: "))
    space = 2*n - 2
    for i in range(1, n+1):
        a = 1
        for j in range(i):
            print(a,end="")
            a += 1
        print(" " * space, end="")
        space -= 2
        a -= 1
        for j in range(i):
            print(a,end="")
            a -= 1
        print()


############# PATTERN 13 ############
def pattern_13():
    n = int(input("Enter the number of lines: "))
    count = 1
    for i in range(1, n+1):
        for j in range(i):
            print(str(count),' ', end="")
            count += 1
        print()

      
############# PATTERN 14 ############
def pattern_14():
    n = int(input("Enter the number of lines: "))
    for i in range(1, n+1):
        temp = 'A'
        printer = ord(temp)
        for j in range(i):
            print(chr(printer), end="")
            printer += 1
        print()


############# PATTERN 15 ############
def pattern_15():
    n = int(input("Enter the number of lines: "))
    for i in range(n, 0, -1):
        temp = 'A'
        printer = ord(temp)
        for j in range(i):
            print(chr(printer), end="")
            printer += 1
        print()


############# PATTERN 16 ############
def pattern_16():
    n = int(input("Enter the number of lines: "))
    temp = 'A'
    printer = ord(temp)
    for i in range(0, n):
        print(chr(printer+i) * (i+1))


############# PATTERN 17 ############
def pattern_17():
    n = int(input("Enter the number of lines: "))
    for i in range(1, n+1):
        # Spaces
        for j in range(1, n-i+1):
            print(" ", end="")
        # Characters
        temp = 'A'
        printer = ord(temp)
        for j in range(1, (2*i - 1)+1):
            mid = (2*i - 1)//2
            print(chr(printer), end="")
            if j <= mid:
                printer += 1
            else:
                printer -= 1
        print()


############# PATTERN 18 ############
def pattern_18():
    n = int(input("Enter the number of lines: "))
    temp = 'A' 
    char = ord(temp) + (n - 1) 
    for i in range(1, n+1):
        printer = char
        for j in range(i):
            print(chr(printer), end="")
            printer += 1
        char -= 1
        print()


############# PATTERN 19 ############
def pattern_19():
    n = int(input("Enter an even number: "))
    mid = n//2
    space = 0
    # Upper Half
    for i in range(mid, 0, -1):
        print("*" * i, " " * space, "*" * i, sep="")
        space += 2
    # Lower Half
    for i in range(1, mid+1):
        space -= 2
        print("*" * i, " " * space, "*" * i, sep="")


############# PATTERN 20 ############
def pattern_20():
    n = int(input("Enter an odd number: "))
    mid = n//2 + 1
    space = n - 1
    # Upper Half
    for i in range(1, mid+1):
        print("*" * i, " " * space, "*" * i, sep="")
        space -= 2
    space += 2
    # Lower Half
    for i in range(mid-1, 0, -1):
        space += 2
        print("*" * i, " " * space, "*" * i, sep="")


############# PATTERN 21 ############
def pattern_21():
    n = int(input("Enter an even number: "))
    space = n - 2
    # Upper Half
    for i in range(1, n + 1):
        if i == 1 or i == n:
            print("*" * n)
        else:
            print("*", " " * space, "*", sep="")


############# PATTERN 22 ############
def pattern_22():
    matrix_dimension = int(input("Enter an odd number: "))
    n = matrix_dimension - 1    # Since we calc dist from origin (0,0)
    for x in range(matrix_dimension):
        for y in range(matrix_dimension):
            arr = [x-0, n-x, y-0, n-y]
            arr.sort()
            print(abs(arr[0] - (matrix_dimension//2 + 1)),end="")
        print()


if __name__ == "__main__":
    main()

