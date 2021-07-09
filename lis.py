import random

# given an array A, find longest increasing subsequence in A

seq = random.sample(range(100), 20)
print("seq = ", seq)

L = [1]
P = [-1]

for i in range(1, len(seq)):
    Lj_calculation = [-1] * len(seq)
    cont = False
    for j in range(i):
        if seq[i] > seq[j]:
            Lj_calculation[j] = L[j]
            cont = True
    if cont:
        max_index = Lj_calculation.index(max(Lj_calculation))
        L.append(Lj_calculation[max_index] + 1)
        P.append(seq[max_index])
    else:
        L.append(1)
        P.append(-1)

seq_length = max(L)
print("lis length = ", seq_length)
out_arr = []
prev_ind = L.index(seq_length)
prev = seq[prev_ind]
out_arr.append(prev)
for i in range(seq_length - 1):
    prev = P[prev_ind]
    out_arr.append(prev)
    prev_ind = seq.index(prev)

out_arr = out_arr[::-1]
print("lis = ", out_arr)
