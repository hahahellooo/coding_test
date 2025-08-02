""" hangman.py """
question = list("batman")
lst = []
for i in range(len(question)):
  lst.append("_")
print(f"Here is the word {lst}")

num_of_try = 10
while num_of_try > 0:
  char = input("Guess a char?")
  for i,e in enumerate(question):
    if e == char:
      lst[i] = char
  print(lst)

  if "_" not in lst:
    print("You win")
    break

  num_of_try -= 1

if num_of_try == 0:
  print("You lost")
