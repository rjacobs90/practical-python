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
        for row in rows:
            fields = row
            try:
                name = fields[0]
                shares = int(fields[1])
                price = float(fields[2])
                cost = shares * price
                total_cost += cost
            except ValueError:
                print(f"ERROR: Skipping line '{row}' due to missing or invalid fields")
    return total_cost

filename = 'Data/portfolio.csv'

if len(sys.argv) == 2:
    filename = sys.argv[1]

print(sys.argv)

cost = portfolio_cost(filename)
print('Total cost:', cost)
