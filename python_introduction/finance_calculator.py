Monthly_income = int(input("Enter your monthly income: "))
Total_monthly_expenses = int(input("Enter your total monthly expenses: "))
Monthly_Savings = Monthly_income -  Total_monthly_expenses
print(f"Monthly Savings: {Monthly_Savings}. ")
Projected_savings = Monthly_Savings * 12 + (Monthly_Savings * 12 * 0.05)
print(f"Annual Porjected Saviings: {Projected_savings}. ")
