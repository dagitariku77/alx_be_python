# finance_calculator.py

# Get user input for financial details
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = monthly_income - monthly_expenses

# Assume a fixed interest rate of 5% annually
interest_rate = 0.05

# Calculate the projected savings after one year, including interest
annual_savings = monthly_savings * 12
projected_savings = annual_savings + (annual_savings * interest_rate)

# Output the results
print(f"Your monthly savings are ${monthly_savings:.2f}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings:.2f}.")
