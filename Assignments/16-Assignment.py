"""
Assignment
Write a Python program that can do the following:
- You have $50
- You buy an item that is $15, that has a 3% tax
- Using the print()  Print how much money you have left, after purchasing the item.
"""

wallet = 50

item_price = 15
tax_rate = 0.03

wallet  -=  item_price + (item_price * tax_rate)

print(wallet)