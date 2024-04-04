

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
    checkout = 0

    skus = Counter(skus)
    for item in skus:
        if item in discounts and (skus[item]%discounts[item][0]==0):
            item_group_count = skus[item] / discounts[item][0]
            item_price = item_price
            full_price += item_price
    # scenario where no valid value is entered
    checkout += 0
    return 




