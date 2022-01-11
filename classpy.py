from multiprocessing import process
import threading
class dai:
    '''daizong'''
    d = 'daiboss'
    time = 1
    # protected
    _scc = [3, 'd', '7']
    # private
    __si = 99
    def __init__(self, n, a, b) -> None:
        print('I\'m ' + str(n) + ' and ' + dai.d)
        print('I am coming the ' + str(dai.time) + ' time(s)!HA')
        dai.time += 1
        self._aa = a
        self.__bb = b
    def xiaozhang(self, e):
        print('lao zhang xiao dai, lao dai xiao zhang!' + str(e))
        print(self)
    def info(self):
        print('a:' + str(self._aa) + ', b: ' + str(self.__bb))
    @property
    # 不含参数的返回
    def t(self):
        print(dai._scc)
        return 'yes'

class he(dai):
    def __init__(self, n, a, b) -> None:
        print('I\'m extend class!')
        super().__init__(n, a, b)
    def i(self):
        print('info')

def process_threading():
    print('running!' + threading.current_thread().name)

if __name__ == '__main__':
    w = dai('scf', 14, 'class 3')
    w.xiaozhang('ssd')
    print(w._scc)
    print('用实例名._类名__私有变量来访问！！')
    print(w._dai__si)
    acs = dai('dcdve', 2, 'class 0')
    print(acs.t)
    acs.info()
    t = he(445, 5.4, '34')
    tt = [threading.Thread(target=process_threading) for i in range(6)]
    for i in tt:
        i.start()
