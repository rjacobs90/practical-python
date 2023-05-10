# pcost.py
#
# Exercise 1.27
import csv
import sys

def portfolio_cost(filename):
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)  # skip line
        portfolio = []
        for row in rows:
            holding = (row[0], int(row[1]), float(row[2]))
            portfolio.append(holding)
    return portfolio

filename = 'Data/portfolio.csv'

if len(sys.argv) == 2:
    filename = sys.argv[1]

print(sys.argv)

portfolio = portfolio_cost(filename)
print('Total portfolio:', portfolio)
