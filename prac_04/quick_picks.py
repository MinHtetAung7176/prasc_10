MIN_VALUE = 1
MAX_VALUE = 45
LOOP_NUMBER = 6

import random
quick_picks = int(input("How many quick picks? "))

number_list = []
for i in range(quick_picks):
    for j in range(LOOP_NUMBER):
        k = []
        g = random.randint(MAX_VALUE,MIN_VALUE)
        k.append(g)
        number_list.append(k)
    print(number_list[i])

