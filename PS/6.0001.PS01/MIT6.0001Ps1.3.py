#PS01.1
# Asking the user to enter their annual salary
annual_salary =float(input("Please enter your annual salary: "))
base_monthly_salary = annual_salary / 12 
semi_annual_rasie=.07
total_cost = 1000000
portion_down_payment = .25 * total_cost
#Using bisection search to get the percentage of savings
months =36
epsilon = 100
num_guess=0
low = 0
high = 10000
portion_saved=(high+low)//2
i=0
current_savings =0
while abs(current_savings - portion_down_payment) > epsilon:
    current_savings=0
    monthly_salary=base_monthly_salary
    for i in range (1,37):
        current_savings = (current_savings *(1+.04/12) + monthly_salary * portion_saved/10000)
        if i % 6 ==0:
            monthly_salary = monthly_salary * 1.07
    num_guess += 1
    if current_savings > portion_down_payment:
        high = portion_saved
    else:
        low = portion_saved
    portion_saved = int(round(high + low) / 2)
ans = portion_saved / 10000
print ("the eprcentage is:{} percent".format(ans))
print ("the number of guesses is", num_guess) 
 
