"This program helps to find the bill with tip."

print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? Rs"))
tip_percent = int(input("What percent tip would you like to give? 10, 12, 15? "))
total_people = int(input("How many people to split the bill? "))
total_amount = total_bill * (1 + tip_percent / 100)
split_amount = round(total_amount / total_people, 2)
print(f"Each person should pay rupees: {split_amount}")
