#Write your code below this row 👇

sum_even = 0
for number in range(101):
  if number % 2 == 0:
    sum_even += number
print(sum_even)

total = 0
for number in range(2, 101, 2):
  total += number
print(total)