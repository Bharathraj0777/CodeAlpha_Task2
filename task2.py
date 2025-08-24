stock_prices = {"AAPL": 180, "TSLA": 250}

portfolio = {}

print("Welcome to Stock Portfolio Tracker")
print("Available stocks:", stock_prices)

while True:
    stock = input("\nEnter stock symbol (or 'done' to finish): ").upper()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print("Stock not available. Choose from AAPL or TSLA.")
        continue

    try:
        qty = int(input(f"Enter quantity for {stock}: "))
    except ValueError:
        print("Invalid number. Try again.")
        continue

    portfolio[stock] = portfolio.get(stock, 0) + qty

total = 0
print("\nPortfolio Summary:")
for stock, qty in portfolio.items():
    value = stock_prices[stock] * qty
    total += value
    print(f"{stock}: {qty} x ${stock_prices[stock]} = ${value}")

print(f"\nTotal Investment Value = ${total}")
