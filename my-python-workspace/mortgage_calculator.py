loan=int(input('Enter the amount of Loan'))
rate=float(input('enter the rate for which you want to give loan'))
"""here nper represents the number of month the lender require to pay back the loan"""
nper=float(input('enter the no of periods'))

"""Our objective is to calculate the amount of money the lender will provide each month"""

monthly_rate=(rate/100/12)
#amount_to_be_given_per_month=loan*(((monthly_rate*(1+monthly_rate))**nper)/((1+monthly_rate)**nper)-1)
amount_to_be_given_per_month=(monthly_rate / (1 - (1 + monthly_rate)**(-nper))) * loan
print(amount_to_be_given_per_month)