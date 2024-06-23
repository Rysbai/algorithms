import string


abc = string.ascii_letters.split()


col_num = int(input())

divs = [col_num]

first_i = col_num

while first_i > 26:
    first_i = int(first_i / 26)
    divs.append(first_i)


indexes = []

for num in reversed(divs):
    indexes.append(num % 26)


print(indexes)

