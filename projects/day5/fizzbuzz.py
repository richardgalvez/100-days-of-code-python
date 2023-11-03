# Print each number from 1 to 100 in turn and include number 100, printed on separate line

for n in range(1, 101):
    # If the number is divisible by both 3 and 5 e.g. 15, then print "FizzBuzz" instead of the number
    if (n % 3 == 0) and (n % 5 == 0):
        print("FizzBuzz")

    # When the number is divisible by 3, print "Fizz" instead of the number
    elif n % 3 == 0:
        print("Fizz")

    # When the number is divisible by 5, print "Buzz" instead of the number
    elif n % 5 == 0:
        print("Buzz")

    else:
        print(n)