import statistics
import random

example_list = []
for x in range(1,31):
    example_list.append(random.randint(1,101))

mn = statistics.mean(example_list)
print('Mean: ', mn)

mn = statistics.median(example_list)
print('Median: ', mn)

mn = statistics.stdev(example_list)
print('Standard deviation: ',mn)

mn = statistics.variance(example_list)
print('Variance: ',mn)