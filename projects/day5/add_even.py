target = int(input())
if target > 1000:
    print("Error: Input too large. Please run again and input a number not greater than 1000.")

else:
# Calculate the sum of all even numbers from 1 to x with range function.
    total = 0
    for even_numbers in range(0, target + 1, 2):
        total += even_numbers
    
    print(total)