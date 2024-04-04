

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

+------+-------+------------------------+
| Item | Price | Special offers         |
+------+-------+------------------------+
| A    | 50    | 3A for 130, 5A for 200 |
| B    | 30    | 2B for 45              |
| C    | 20    |                        |
| D    | 15    |                        |
| E    | 40    | 2E get one B free      |
+------+-------+------------------------+

"""
from collections import Counter
prices = {"A": 50, "B": 30, "C": 20, "D": 15,}
bundles = {"E":[2, {"B":1}]}
discounts = {"A": {5:200, 3:130}, "B": {2:45}, }

def apply_bundles(skus:str):
    bundled = {item:skus[item] for item in skus if item in bundles}
    for item in bundled:
        bundle_quantity = bundles[item][0] # 2 for E
        customer_quantity = skus[item]
        bundles_present = customer_quantity // bundle_quantity
        for bundle_item, bundle_discount in bundles[item][1]: # {"B":1} for E
            skus[bundle_item] -= (bundle_discount * bundles_present) # 1 * number of E pairs
    return skus

def apply_discount(skus:str, full_price:int):
    on_offer = {item:skus[item] for item in skus if item in discounts}
    
    to_discount = {}
    price_normally = {}
    
    for item in on_offer:
        customer_quantity = skus[item]
        for offer_quantity in discounts[item]: # keys 5 and 3 for A
            pass
        offer_quantity = discounts[item][0]
        to_discount[item] = customer_quantity//offer_quantity
        price_normally[item] = customer_quantity%offer_quantity

    for item in to_discount:
        full_price += to_discount[item] * discounts[item][1]
    return full_price, price_normally


def checkout(skus:str)->int:
    full_price = 0

    skus = Counter(skus)
    full_price, skus = apply_bundles(skus)
    full_price, price_normally = apply_discount(skus, full_price)
    
    # skus are updated to only contain excess quantities that didn't fit in offer
    skus = skus | price_normally

    for item in skus: 
        if item in prices:
            full_price += skus[item] * prices[item]
        else:
            # scenario where an invalid value is entered
            return -1
    return full_price
