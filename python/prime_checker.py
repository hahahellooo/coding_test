""" prime_checker.py """

question_num = 5


def prime_checker(num: int):
  if num > 1:
    is_divisible = False
    for i in range(2, num):
      if num % i == 0:
        is_divisible = True
        print(f"{num} is divisible by {i}")
        break
    if is_divisible:
      print(f"{num} is not a prime number")
    else:
      print(f"{num} is a prime number")
  else:
    print(f"{num} is not a prime number")


prime_checker(question_num)
