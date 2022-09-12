# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
number_of_months = 0
extra_payment_start_month = int(input("At what month should the extra payments begin? - "))
extra_payment_end_month = int(input("At what month should the extra payments end? - "))
extra_payment = float(input("How much extra payment would you like to add? - "))

while principal > 0:
    
        
    if number_of_months >= extra_payment_start_month and number_of_months <= extra_payment_end_month:
        principal = principal * (1+rate/12) - (payment + extra_payment)
        total_paid = total_paid + payment + extra_payment
    else:
        if principal - payment > 0:
            principal = principal * (1+rate/12) - payment
            total_paid = total_paid + payment
        else:
            principal = principal - principal
            total_paid = total_paid + principal
    number_of_months += 1
    print(number_of_months, " ", round(total_paid, 2), " ", round(principal, 2))

print("Total paid: ", round(total_paid, 2))
print("Months: ", number_of_months)

