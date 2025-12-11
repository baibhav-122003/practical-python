# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
running_month = 0
extra_payment_start_month = int(input('Enter extra payment start month'))
extra_payment_end_month = int(input('Enter extra payment end month'))
extra_payment = int(input('Enter extra amount'))

while principal > 0:
    running_month = running_month + 1
    monthly_pay = payment

    if running_month >= extra_payment_start_month and running_month <= extra_payment_end_month: 
        monthly_pay = monthly_pay + extra_payment

    amount = principal * (1+rate/12)  
    if amount > monthly_pay:
        principal = amount - monthly_pay
        total_paid = total_paid + monthly_pay
    else:
        principal = 0
        total_paid = total_paid + amount
    
    print(running_month, round(total_paid, 2), round(principal, 2))

print('Total paid', round(total_paid, 2))
print('Months', running_month) 
