import csv
from pprint import pprint

def read_prices(filename):
    prices = {}
    with open(filename, 'r') as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                stockname = row[0]
                price = float(row[1])
                prices[stockname] = price
            except IndexError:
                pass # ignore blank line
        pprint(prices)

filename = 'Data/prices.csv'

read_prices(filename)
