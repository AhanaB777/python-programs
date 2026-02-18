"""
“Sliding Window Average & Variance Tracker”
Problem: Given a long list of numbers (floats or ints) representing, say, daily measurements
(temperature, sales, or sensor readings), implement a “sliding window” algorithm: for a
window size k, compute for each window position the average and variance (or standard
deviation) of the numbers in that window. Output a list of tuples (average, variance) for all
valid windows.
Input: A list of numbers (length ≥ k), integer window size k.
Output: A list of tuples: (avg, variance) for each position from start to len(list) – k
+ 1.

"""
l=[1,2,3,3,9,2,1,2,4]
k=5
result = []

for i in range(len(l) - k + 1):
    s = 0
    for j in range(i, i+k):
        s += l[j]
    mean = s / k

    sd_sum = 0
    for j in range(i, i+k):
        sd_sum += (l[j] - mean) ** 2
    var = sd_sum / k

    result.append((round(mean,3), round(var,3)))

print(result)

