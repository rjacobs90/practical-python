# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
total_paid = 0.0
months = 1
monthly_payment = 2684.11 # stop the $1000 extra after 12 months
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:

    payment = monthly_payment
    # if months <= 12:
    #     payment = 2684.11 + extra_payment # adding $1000 for 12 months
    if 61 <= months <= 108:
        payment = monthly_payment + extra_payment # adding $1000
    principal = principal * (1+rate/12) - payment
    total_paid += payment
    print( 'month=', months, 'total paid=', round(total_paid, 2), 'principal=', round(principal, 2)) #debugging
    if principal < 2648.11:
         payment = principal * (1+rate/12)
         principal = principal * (1+rate/12) - payment
    months = months + 1
    print( 'month=', months, 'total paid=', round(total_paid, 2), 'principal=', round(principal, 2)) #debugging

payback = round(principal * (1+rate),2)

# print('Total paid', round(total_paid + payback, 2))
print('Number of months:', months)
