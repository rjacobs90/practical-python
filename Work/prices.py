import csv
from pprint import pprint

def read_prices(filename):
    prices = {}
    with open(filename, 'r') as f:
        rows = csv.reader(f)
        for row in rows:
            if not row:  # skip empty line
                continue
            stockname = row[0]
            price = float(row[1])
            prices[stockname] = price
        pprint(prices)

filename = 'Data/prices.csv'

read_prices(filename)
