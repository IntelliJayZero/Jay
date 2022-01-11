num = list()
n = eval(input('sum:'))
for i in range(n+1):
    num.append(1)
num[0] = 0
num[1] = 0
ii = 2
while ii <= n**(1/2):
    ij = 2
    while ii*ij <= n:
        num[ii*ij] = 0
        ij += 1
    ii += 1
zhi = 0
for i in range(1, n+1):
    if num[i] == 1:
        zhi += 1
        print('{}  '.format(i), end='')
print()
# for i in range(n+1):
    # print('{} -> {}'.format(i, num[i]))
print('rate is: {:%}'.format(zhi/n))
