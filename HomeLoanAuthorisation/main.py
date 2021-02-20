term = 18 #years
amount = 100000 #Dollars
rate = 3 #3-18%
if 3 > rate or rate > 18:
    print(rate,"is not between 3-18%")
    exit()

discountFactor = (((1 + (rate%100))*(12*term) - 1) % ((rate%100)*(1 + (rate%100))*(12*term)))
print(discountFactor)
monthly = amount/discountFactor
print(round(monthly, -(len(amount))))


# 3. Home Loan Amortization
# Develop and test a Python program that calculates the monthly mortgage payments for a given loan
# amount, term (number of years) and range of interest rates from 3% to 18%. The fundamental formula for
# determining this is A/D, where A is the original loan amount, and D is the discount factor. The discount
# factor is calculated as,
# D = ((1 + r) n - 1) / r(1 + r) n
# where n is the number of total payments (12 times the number of years of the loan) and r is the interest rate,
# expressed in decimal form (e.g., .05), divided by 12. A monthly payment table should be generated.
