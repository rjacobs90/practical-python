# pcost.py
#
# Exercise 1.27
import csv
import sys

def portfolio_cost(filename):
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)  # skip line
        total_cost = 0
        for rowno, row in enumerate(rows, start=1):
            fields = dict(zip(headers, row))
            try:
                shares = int(fields['shares'])
                price = float(fields['price'])
                cost = shares * price
                total_cost += cost
            except ValueError:
                print(f'Row {rowno}: Bad row: {row}')
    return total_cost

filename = 'Data/portfoliodate.csv'

if len(sys.argv) == 2:
    filename = sys.argv[1]

print(sys.argv)

cost = portfolio_cost(filename)
print('Total cost:', cost)
