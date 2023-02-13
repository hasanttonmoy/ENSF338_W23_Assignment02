import sys
sys.setrecursionlimit(20000)

def func1(arr, low, high):
    if low < high:
        pi = func2(arr, low, high)
        func1(arr, low, pi-1)
        func1(arr, pi + 1, high)

def func2(array, start, end):
    mid = (start + end) // 2
    array[mid], array[start] = array[start], array[mid]
    p = array[start]
    low = start + 1
    high = end
    while True:
        while low <= high and array[high] >= p:
            high = high - 1
        while low <= high and array[low] <= p:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    return high

import json
import time
import matplotlib.pyplot as plt

sys.setrecursionlimit(20000)

with open('ex2.json', 'r') as f:
    inputs = json.load(f)

execution_times = []

for arr in inputs:
    start_time = time.time()
    func1(arr, 0, len(arr)-1)
    end_time = time.time()
    execution_times.append(end_time - start_time)

plt.plot(range(len(inputs)), execution_times)
plt.xlabel('Input Number')
plt.ylabel('Time (s)')
plt.show()
plt.savefig('ex2_plot.png')
