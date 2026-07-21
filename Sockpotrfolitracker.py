# Stock Portfolio Tracker

stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 150,
    "MSFT": 300
}

total = 0

print("=== Stock Portfolio Tracker ===")

while True:
    stock = input("Enter Stock Name (AAPL/TSLA/GOOG/MSFT) or 'done' to finish: ").upper()

    if stock == "DONE":
        break

    if stock in stocks:
        qty = int(input("Enter Quantity: "))
        value = stocks[stock] * qty
        total += value
        print(f"{stock} Value = ${value}")
    else:
        print("Stock not found!")

print("\nTotal Investment Value = $", total)
