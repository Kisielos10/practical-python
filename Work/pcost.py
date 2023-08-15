# pcost.py
#
# Exercise 1.27

with open('Data/portfolio.csv', 'rt') as file:
    next(file)
    prices = 0
    for line in file:
        numberOfStocks = int(line.split(',')[1])
        prices += float(line.split(',')[2]) * numberOfStocks
print("Total cost",prices)