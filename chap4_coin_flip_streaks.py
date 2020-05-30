import random

sample_size = 10000  # use small sample_size and print stmts to check
numberOfStreaks = 0
streak_length = 6
curStreak = 0
results = []

for experimentNumber in range(sample_size):
    # Code that creates a list of 10000 'heads' or 'tails' values.
    results.append('H' if random.randint(0,1) else 'T')

#print(results)    
#print('i, item, results[i], curStreak, numberOfStreaks')

# Code that checks if there is a streak of 6 heads or tails in a row.
for i, item in enumerate(results):
    if i == len(results) - 1:
        break
    if item == results[i + 1]:
        curStreak += 1
    else:
        curStreak = 0

    if curStreak >= streak_length - 1:
        numberOfStreaks += 1
    #print(i, item, results[i+1], curStreak, numberOfStreaks)

print(f'Chance of streak: { round((numberOfStreaks / sample_size)*100)}%')
