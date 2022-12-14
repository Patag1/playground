from cs50 import get_int

scores = []
n = get_int('N° of scores: ')
for i in range(n):
    scores.append(get_int('Score: '))
    # scores += [get_int('Score: ')]

avg = sum(scores) / len(scores)
print(f'Average: {avg}')