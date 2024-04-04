

# noinspection PyUnusedLocal
# skus = unicode string
"""
Our price table and offers: 
+------+-------+----------------+
| Item | Price | Special offers |
+------+-------+----------------+
| A    | 50    | 3A for 130     |
| B    | 30    | 2B for 45      |
| C    | 20    |                |
| D    | 15    |                |
+------+-------+----------------+

"""
from collections import Counter
prices = {"A": 50, "B": 30, "C": 20, "D": 15,}
discounts = {"A": (3, 130), "B": (2, 45), }

def checkout(skus:str)->int:
    full_price = 0

    skus = Counter(skus)
    on_offer = {item:skus[item] for item in skus if item in discounts}
    
    to_discount = {}
    normal_price = {}
    
    for item in on_offer:
        offer_quantity = discounts[item][0]
        customer_quantity = skus[item]
        to_discount[item] = customer_quantity//offer_quantity
        normal_price[item] = customer_quantity%offer_quantity

    for item in to_discount:
        full_price += to_discount[item] * discounts[item][0]
    
    # skus are updated to only contain excess quantities that didn't fit in offer
    skus = skus | normal_price

    for item in skus: 
        if item in prices:
            full_price += skus[item] * prices[item]
        else:
            # scenario where an invalid value is entered
            return -1
    return full_price



