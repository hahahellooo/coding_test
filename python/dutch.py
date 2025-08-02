""" dutch.py """

num_of_ppl = 3
food_prices = [10, 20, 15, 17, 50]

def going_dutch(num_of_ppl: list, food_prices: int):
  total = 0
  for price in food_prices:
    total += price

  return round((total / num_of_ppl), 1)

bill = going_dutch(num_of_ppl, food_prices)
print(bill)
