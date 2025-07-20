# A BUDGET MANAGER PROGRAM
# Start with a welcome message
# Ask for user income (salary)
# Aak for user's income (business)
# Calculate total income
# Ask for user's to input transport expenses
# Ask for food expenses
# Calculate total expenses
#Summary

username = input("What's your name?: ")
print(f"Welcome {username} to Budget Manager!")

salary = float(input("What's your monthly income (salary)? :"))
business = float(input("What's your monthly business income?: "))

total_income = salary + business
print(f"Total Monthly income: ${total_income:.2f}")

transport = float(input("What's your transport expenses for the month?: "))
food = float(input("What's your food expenses for the month?: "))
total_expenses = transport + food
print(f"total expenses for the month: ${total_expenses:.2f}")

monthly_savings = total_income - total_expenses
print(f"Total Monthly Savings: ${monthly_savings:.2f}")