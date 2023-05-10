# report.py
import csv
from pprint import pprint

def read_portfolio(filename):
    '''
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    '''
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for rowno, row in enumerate(rows, start=1):
            fields = dict(zip(headers, row))
            try:
                stock = {
                    'name'   : str(fields['name']),
                    'shares' : int(fields['shares']),
                    'price'   : float(fields['price'])
                }
            except ValueError:
                print(f'Row {rowno}: Bad row: {row}')
            portfolio.append(stock)

    return portfolio

def read_prices(filename):
    '''
    Read a CSV file of price data into a dict mapping names to prices.
    '''
    prices = {}
    with open(filename) as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                pass

    return prices

def make_report(portfolio,prices):
    rows = []
    for stock in portfolio:
        current_price = prices[stock['name']]
        change = current_price - stock['price']
        report = (stock['name'], stock['shares'], current_price, change)
        rows.append(report)

    headers = ('Name', 'Shares', 'Price', 'Change')
    column_number = len(headers)
    column_size = 10
    seperator = '-'
    print(f'{headers[0]:>{column_size}s} {headers[1]:>{column_size}s} {headers[2]:>{column_size}s} {headers[3]:>{column_size}s}')
    print(f'{seperator*column_size:>{column_size}s} ' * column_number)
    for name, shares, price, change in rows:
            price = f'${price:.2f}'
            print(f'{name:>{column_size}s} {shares:>{column_size}d} {price:>{column_size}} {change:>{column_size}.2f}')

# def make_report(report)
#     for r in report:
# #         print(r)

#     for y in repotr

portfolio = read_portfolio('Data/portfoliodate.csv')
prices    = read_prices('Data/prices.csv')

# Calculate the total cost of the portfolio
total_cost = 0.0
for s in portfolio:
    total_cost += s['shares']*s['price']

print('Total cost', total_cost)

# Compute the current value of the portfolio
total_value = 0.0
for s in portfolio:
    total_value += s['shares']*prices[s['name']]

print('Current value', total_value)
print('Gain', total_value - total_cost)

make_report(portfolio, prices)
