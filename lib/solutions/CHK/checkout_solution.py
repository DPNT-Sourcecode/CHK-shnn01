

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

def apply_discount(on_offer:dict)->tuple[int, dict]:
    for item in on_offer:
        item_price = item_group_count * discounts[item][0]
            full_price += item_price



def checkout(skus:str)->int:
    full_price = 0

    skus = Counter(skus)
    on_offer = {item:skus[item] for item in skus if item in discounts}
    # discounts can be applied on multiples of the item amount specified in offer
    to_discount = {item:skus[item]/discounts[item][0] for item in on_offer}
    normal_price = {item:skus[item]%discounts[item][0] for item in on_offer}

    # update main skus list to reflect quanti

    for item in skus:

        if item in discounts and (skus[item]%discounts[item][0]==0):
            item_group_count = 
            
        elif item in prices:
            full_price += skus[item] * prices[item]
        else:
            # scenario where an invalid value is entered
            return -1
    return full_price



