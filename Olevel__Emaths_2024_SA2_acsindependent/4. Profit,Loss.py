import math

'''
cost = 24
profit = 45/100
price_target = cost*profit + cost
print(price_target)

loss = 80/100
list_price = price_target/loss
print(list_price)
'''

def shorts_price(cost):
    profit = 45/100
    price_target = (cost * profit) + cost
    print(f"4. Price target = {price_target}")

    discount = 80/100
    list_price = round(price_target/discount, 2)
    print(f"4. listed_price = {list_price}")

    return list_price

shorts_price(24)

