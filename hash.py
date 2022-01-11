import random
r = int(input('the number range:'))
h = int(input('hash function:'))
t = int(input('how many times:'))
s = list()
for i in range(h):
    s.append(0)
for i in range(t):
    n = random.randint(0, r)
    d = n%h
    s[d] += 1
for i in range(h):
    print('{}:->{}'.format(i, s[i]))