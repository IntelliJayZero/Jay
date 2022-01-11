import random
import time

def result(six):
    if sorted(six) == [1, 2, 3, 4, 5, 6]:
        print('对堂')
        return 123456
    elif sorted(six) == [1, 1, 4, 4, 4, 4]:
        print('哎哟，不错哦！')
        return 444411
    elif six.count(1) == 6 or six.count(2) == 6 or six.count(3) == 6 or six.count(4) == 6 or six.count(5) == 6 or six.count(6) == 6:
        print('666!')
        return 6
    elif six.count(1) == 5 or six.count(2) == 5 or six.count(3) == 5 or six.count(4) == 5 or six.count(5) == 5 or six.count(6) == 5:
        print('五子登科')
        return 5
    elif six.count(4) == 4:
        print('状元')
        return 4444
    elif six.count(1) == 4 or six.count(2) == 4 or six.count(3) == 4 or six.count(5) == 4 or six.count(6) == 4:
        print('四进')
    elif six.count(4) == 3:
        print('三红')
    elif six.count(4) == 2:
        print('二举')
    elif six.count(4) == 1:
        print('一秀')
    else:
        print('呵呵！')

def one():
    random.seed(random.getrandbits(64))
    return random.randint(1, 6)

def play():
    the_six = list()
    for i in range(6):
        the_six.append(0)
    random.seed(random.getrandbits(32))
    a = random.randint(8, 20)
    b = random.randint(8, 20)
    c = random.randint(8, 20)
    d = random.randint(8, 20)
    e = random.randint(8, 20)
    f = random.randint(8, 20)
    for i in range(max(a, b, c, d, e, f)):
        if a > 0:
            the_six[0] = one()
        a -= 1
        if b > 0:
            the_six[1] = one()
        b -= 1
        if c > 0:
            the_six[2] = one()
        c -= 1
        if d > 0:
            the_six[3] = one()
        d -= 1
        if e > 0:
            the_six[4] = one()
        e -= 1
        if f > 0:
            the_six[5] = one()
        f -= 1
        time.sleep(0.2)
        print('{}\r'.format(the_six), end='')
        # print('left:{} {} {} {} {} {}\n'.format(a, b, c, d, e, f))
    print()
    return the_six

def dash(n):
    t = 0
    p = list()
    for i in range(6):
        p.append(0)
    flag = False
    while not flag:
        t += 1
        for i in range(6):
            p[i] = one()
        print(p, end='\t')
        if result(p) == n:
            flag = True
        time.sleep(0.05)
    print('Used {} times!'.format(t))

l = [444411, 123456, 6, 5, 4444]
x = input('来博饼啊！\n')
while x != 'e':
    result(play())
    x = input('写下博饼前想说的话：\n')
y = int(input('想博到什么呢？（注：状元插金花444411，对堂123456，六子6，五子登科5，还是仅仅一个普通状元4444）\n'))
if y in l:
    dash(y)