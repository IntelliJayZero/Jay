import re
import modules
import os
import sqlite3
from multiprocessing import Process
# from hash import r

def multican(*remark):
    print('begin'.center(16, '*'))
    for i in remark:
        print(i, end='')
        print('--,--', end='')
    print('end!!!')

def dictionary_like(**d):
    for k, v in d.items():
        print(str(k) + '-->' + str(v))
def raise_error(a):
    if a != True:
        raise ConnectionRefusedError('Not True?')

def process_2(interval):
    print('OUT!!')

def main():
    print('to connect some different type of data, use \',\' between them!!\nBut will add a space!!So use str()')
    print(434, '4jrf<-like this!')

    ll = [32, 're3', 'yao', '5', 65, '22']
    print(ll)
    for ind, cont in enumerate(ll):
        print(ind, '-', cont)
    print('to print a list, use\nfor Index, Element in enumerate(List):\n    print(Index, Element)')

    ll.remove('yao')
    l3 = [3, 6, 12, 4.6, 6.23, 9, 0.1, 11, 6]
    print(str(sorted(l3)) + ' and\n' + str(l3))
    print('sorted(List) will not modify the list, while List.sort() will do it!')
    l3.sort()

    print('random list: Listname = [ramdom._randmethod_ for i in range(times)]')
    d = {'re': 43, 45: 'r43', '432': 88}
    print(d.get('432'))
    d[883] = '883w'
    print(d.keys())
    print(d.items())

    s = 'eci382j久违的文件人家非常e3'
    sed = s.encode()
    print(s + '->' + str(sed))
    print(s[::3])
    qqw = '   wef3 445      '
    print(qqw.strip())

    temp = 'you are %s, age: %d.'
    print(temp)
    tp = ('yeskelang', -1)
    print(temp%tp)

    patt = r'(wen)?(dai)|(30)'
    tt = input('give a string:')
    print(re.search(patt, tt))

    multican(7381, '4324', 'tfr')
    # dictionary_like({'243' : 26, 'cdew' : 'ddu3', 8843 : '32'})
    print('global in a function can modify 全局变量!!global x = 3')

    modules.lay('efd', 222)
    try:
        ee = 3/0
    except ZeroDivisionError as e:
        print(e)
    else:
        print('END')
    finally:
        print('FINAL')
    try:
        raise_error('w')
    except ConnectionRefusedError as e:
        print(str(e) + '!!!')
    finally:
        print('end')
    try:
        assert 4 == 4.0004
    except AssertionError as a:
        print(a)

    with open('ts.txt', 'a+', encoding='utf-8') as fi:
        fi.write('the n\n')
        fi.writelines(str(ll))
    with open('read.txt', 'r', encoding='utf-8') as f:
        line = f.readline()
        i = 1
        while line:
            print(i, line, end='')
            i += 1
            line = f.readline()
        f.seek(0)
        print()
        print(f.readlines())

    w = os.walk(r'D:\文档11\PC\操作系统PPT')
    print(type(w))
    for path, fold, files in w:
        print('path:' + path)
        print('folder:' + str(fold))
        print('filename:' + str(files))
        print('+++++++++++++++++++++')
    status = os.stat('g.go')
    print(str(type(status)) + '\n' + str(status))
    print(os.access('g.go', os.X_OK))

    '''
    c = sqlite3.connect('data.db')
    curs = c.cursor()
    curs.execute('create table user(id int(8) primary key, name varchar(20))')
    curs.close()
    c.close()
    '''

    ppp = Process(target=process_2, args=(1,))
    ppp.start()

if __name__ == '__main__':
    print('1111111111111111111111111111111')
    main()
    print('2222222222222222222222222222222')