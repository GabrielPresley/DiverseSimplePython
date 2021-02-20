term = int(input("Term Length (years):")) #years
amount = int(input("Amount Owed ($)")) #Dollars
rate = int(input("Rate (3-18%)")) #3-18%
if 3 > rate or rate > 18:
    print(rate,"is not between 3-18%")
    exit()

discountFactor = (((1 + (rate%100))*(12*term) - 1) % ((rate%100)*(1 + (rate%100))*(12*term)))
print("Discount Factor:",discountFactor)
monthly = amount/discountFactor
print("Monthly amount:",round(monthly, 2))

# 3. Home Loan Amortization
# Develop and test a Python program that calculates the monthly mortgage payments for a given loan
# amount, term (number of years) and range of interest rates from 3% to 18%. The fundamental formula for
# determining this is A/D, where A is the original loan amount, and D is the discount factor. The discount
# factor is calculated as,
# D = ((1 + r) n - 1) / r(1 + r) n
# where n is the number of total payments (12 times the number of years of the loan) and r is the interest rate,
# expressed in decimal form (e.g., .05), divided by 12. A monthly payment table should be generated.
