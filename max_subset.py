import random

# given an array A, find 2 indices i,j so A[i]+A[i+1]+...+A[j] is the largest following subset

seq = random.sample(range(-50, 50), 20)
print(seq)

out_sum = max(seq[0], 0)
out_arr = []
if out_sum > 0:
    out_arr.append(seq[0])

for i in range(1, len(seq)):
    curr_sum = max(out_sum + seq[i], 0)
    if curr_sum > 0:
        out_sum = curr_sum
        out_arr.append(seq[i])
    else:
        out_sum = 0
        out_arr = []

print(out_arr)
print(out_sum)