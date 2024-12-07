''' Stock Transaction Program
Last month, Joe purchased some stock in Acme Software, Inc. Here are the details of the purchase:
• The number of shares that Joe purchased was 2,000.
• When Joe purchased the stock, he paid $40.00 per share.
• Joe paid his stockbroker a commission that amounted to 3 percent of the amount he paid
for the stock.
Two weeks later, Joe sold the stock. Here are the details of the sale:
• The number of shares that Joe sold was 2,000.
• He sold the stock for $42.75 per share.
• He paid his stockbroker another commission that amounted to 3 percent of the amount he received for the stock.
Write a program that displays the following information:
• The amount of money Joe paid for the stock.
• The amount of commission Joe paid his broker when he bought the stock.
• The amount for which Joe sold the stock.
• The amount of commission Joe paid his broker when he sold the stock.
• Display the amount of money that Joe had left when he sold the stock and paid his
broker (both times). If this amount is positive, then Joe made a profit. If the amount is negative, then Joe lost money.   '''


# Purchase details
shares_purchased = 2000
purchase_price_per_share = 40.00
purchase_commission_rate = 0.03  # 3%

# Sale details
shares_sold = 2000
sale_price_per_share = 42.75
sale_commission_rate = 0.03  # 3%

# Calculate purchase amounts
amount_paid_for_stock = shares_purchased * purchase_price_per_share
purchase_commission = amount_paid_for_stock * purchase_commission_rate

# Calculate sale amounts
amount_received_from_sale = shares_sold * sale_price_per_share
sale_commission = amount_received_from_sale * sale_commission_rate

# Calculate net profit or loss
total_commission_paid = purchase_commission + sale_commission
net_amount = amount_received_from_sale - sale_commission - amount_paid_for_stock - purchase_commission

# Display results
print(f"Amount paid for the stock: ${amount_paid_for_stock:.2f}")
print(f"Commission paid to broker when buying: ${purchase_commission:.2f}")
print(f"Amount received from selling the stock: ${amount_received_from_sale:.2f}")
print(f"Commission paid to broker when selling: ${sale_commission:.2f}")
print(f"Net amount after selling and paying commissions: ${net_amount:.2f}")

if net_amount > 0:
    print("Joe made a profit.")
else:
    print("Joe incurred a loss.")
