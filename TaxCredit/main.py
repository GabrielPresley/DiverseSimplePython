cost = int(input("House value at time of purchase:"))
income = int(input("Household combined income:"))
lastPrimary = int(input("year of last owned primary residence or years since:"))

if cost <= 800000 and income <= 225000 and (lastPrimary >= 3 or 1000 < lastPrimary <= 2018):
    print("\n\n\nyou may be eligable to recieve The First-Time Home Buyer Tax Credit")
else:
    for i in range(10000):
        print(("NO MONEY 4 U",)*i)

# 2. The First-Time Home Buyer Tax Credit
# Develop and test a Python program that determines if an individual qualifies for a government First-Time
# Home Buyer Tax Credit of $8,000. The credit was only available to those that (a) bought a house that cost
# less than $800,000, (b) had a combined income of under $225,000 and (c) had not owned a primary residence
# in the last three years.
