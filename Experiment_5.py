#Program 1 (Recursive Method – Basic)
 def fibonacci_recursive(n):
    if n <= 0:
        return "Invalid input. Enter a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
 n = int(input("Enter the value of n: "))
 print(f"The {n}th Fibonacci number is: {fibonacci_recursive(n)}")


#Program 2 (Iterative Method)
 def fibonacci_iterative(n):
    if n <= 0:
        return "Invalid input. Enter a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    a, b = 0, 1
    for _ in range(2, n):
        a, b = b, a + b
    return b
 n = int(input("Enter the value of n: "))


#Program 3 (Recursive with Error Handling)
 def fibonacci(n):
    if n <= 0:
        return "Invalid input. Please enter a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
 try:
    n = int(input("Enter the position (n) of the Fibonacci number: "))
    result = fibonacci(n)
    print(f"The {n}th Fibonacci number is: {result}")
 except ValueError:
    print("Invalid input. Please enter an integer value.")


 print(f"The {n}th Fibonacci number is: {fibonacci_iterative(n)}")
