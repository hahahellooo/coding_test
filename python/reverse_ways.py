""" reverse_ways.py """

v = "Hello World"

# list reverse
# v = list(v)
# v.reverse()
# print(''.join(v))

# all type of reverse
# reverse_v = reversed(v)
# print("".join(reverse_v))

# for loop
answer = []
# for i in range(len(v)-1, -1, -1):
#   answer.append(v[i])
# print(''.join(answer))

# while loop
v = list(v)
while len(v) > 0:
  answer.append(v.pop())
print(''.join(answer))
