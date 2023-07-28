print("Welcome to the tip calculator!")

bill_total = float(input("What was the total bill? $"))
bill_split = float(input("How many people will split the bill? "))
tip_percentage = float(input("What percentage tip would you like to give: 10, 12, or 15? ")) * 0.01

tip_calc = round((((bill_total * tip_percentage) + bill_total) / bill_split), 2)
amount_to_pay = str(tip_calc)

print("Each person should pay: $" + amount_to_pay)