import statistics
import random

example_list = []
for x in range(1,31):
    example_list.append(random.randint(1,101))

mn = statistics.mean(example_list)
print(mn)