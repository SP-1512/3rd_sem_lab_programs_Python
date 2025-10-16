#Program 1 (Using max() Function)
 numbers = [12, 45, 23, 67, 89, 34]
 largest = max(numbers)
 print("The largest number is:", largest)

#Program 2 (Using a Loop for Comparison)
 numbers = [15, 2, 78, 34, 56, 90, 11]
 largest = numbers[0]
 for num in numbers:
    if num > largest:
        largest = num
 print("The largest number is:", largest)

#Program 3 (User Input with Error Handling)
def find_largest():
    try:
        numbers = list(map(int, input("Enter numbers separated by space: ").split()))
        if not numbers:
            print("The list is empty. Please enter valid numbers.")
            return
        largest = max(numbers)
        print("The largest number is:", largest)
    except ValueError:
        print("Invalid input. Please enter only integers separated by spaces.")
 find_largest()
