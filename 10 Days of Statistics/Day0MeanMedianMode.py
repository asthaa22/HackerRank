'''
Created on Dec 3, 2020
@author: asthaa
'''

import statistics
numbers_of_elem = int(input())
numbers = list(map(int,input().split()))

print(statistics.mean(numbers))
print(statistics.median(numbers))
print(max(sorted(numbers), key=numbers.count))
