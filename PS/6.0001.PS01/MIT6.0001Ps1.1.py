#PS01.1
# Asking the user to enter their annual salary
annual_salary =float(input("Please enter your annual salary: "))
monthly_salary = annual_salary / 12 
# Asking the user to enter the portion saved from their salary
portion_saved =float(input("Enter the percentage you want to save each month: "))
# Asking the user to enter the total cost of their home
total_cost =float(input("Please enter the total cost of your dream house: "))
# Asking the user to enter their semi annual raise
semi_annual_rasie =float(input("Please enter your semi annual raise: "))
#  Calculation the down payment for the house
portion_down_payment = .25 * total_cost
# declaring current_savings and months variables
current_savings = 0
months =0
# Calculating my savings: portion saved+roi from the previous month
# adding the semi annual raise each six months
while(current_savings < portion_down_payment):
    current_savings = (current_savings *(1+.04/12) + monthly_salary * portion_saved)
    months += 1
    if months % 6 ==0:
        monthly_salary = monthly_salary * (1+semi_annual_rasie)

print ("the number of months needed to get the down payment is:{} months".format(months))
 
