nm = input().split()
n = int(nm[0])
m = int(nm[1])

row_sum = [0 for _ in range(n)]
col_sum = [0 for _ in range(m)]

for i in range(n):

    row = input().split()

    r = 0
    for j in range(m):
        r += int(row[j])
        col_sum[j] += int(row[j])
    row_sum[i] = r

pre_row = [0]*n
pre_col = [0]*m

s = 0
for i in range(n):
    s += row_sum[i]
    pre_row[i] = s

s = 0
for j in range(m):
    s += col_sum[j]
    pre_col[j] = s

diff = 100000
total = pre_row[-1]
for i in range(n):
    diff = min(diff, abs(2*pre_row[i] - total))

for j in range(m):
    diff = min(diff, abs(2*pre_col[j] - total))

print(diff)