

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
            # caveat: this puts the condition that the discount will only be applied if the ordered quantity is a perfect multiple of 
            # of the quantity specified in the discount. 
            item_group_count = skus[item] / discounts[item][0]
            item_price = item_group_count * discounts[item][0]
            full_price += item_price
        elif item in prices:
            full_price += skus[item] prices[item]
    # scenario where no valid value is entered
    checkout += 0
    return 





