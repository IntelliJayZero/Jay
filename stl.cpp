#include<iostream>
#include<vector>
#include<queue>
#include<stack>
#include<deque>
#include<list>
#include<map>
#include<set>

using namespace std;
int main(int argc, char const *argv[])
{
    int i;
    vector<double> d(7);
    vector<double>::iterator it;
    cout << "capacity:" << d.capacity() << " max:" << d.max_size() << endl;
    d[0] = 3.141592653589793238462643383279;
    d[3] = 4.99;
    d.push_back(0.039);
    d.push_back(9);
    d.push_back(231.4372);
    it = d.begin() + 4;
    d.insert(it, 3.5421);
    it = d.end() - 2;
    d.erase(it);
    for (i = 0, it = d.begin(); it != d.end(); it++) {
        cout << "vector[" << i << "]:" << *it << endl;
        i++;
    }

    deque<int> q(3, 213);
    q.push_back(110);
    q.pop_front();
    q.push_front(58);
    q.push_back(2);
    q.back() = 8342;
    for (i = 0; i < q.size(); i++) {
        cout << "dequeue[" << i << "]:" << q[i] << endl;
    }
    cout << "front position:" << &q.front() << endl;

    list<string> l(4, "null");
    list<string>::iterator liz;
    l.push_back("deng");
    l.push_back("chen he");
    l.push_front("xie");
    l.pop_back();
    for (i = 0, liz = l.begin(); liz != l.end(); i++, liz++) {
        cout << "list[" << i << "]:" << *liz << endl;
    }
    //cannot use index to casually get element like before!

    set<int> s;
    set<int>::iterator sb;
    s.insert(6);
    s.insert(4);
    s.insert(6);
    s.insert(7);
    s.insert(1);
    for (i = 0, sb = s.begin(); sb != s.end(); i++, sb++) {
        cout << "set[" << i << "]:" << *sb << endl;
    }
    //cannot use index to casually get element like before!
    cout << *s.find(6) << endl;

    multiset<int> m;
    multiset<int>::iterator mm;
    m.insert(1);
    m.insert(3);
    m.insert(2);
    m.insert(3);
    m.insert(4);
    for (i = 0, mm = m.begin(); mm != m.end(); i++, mm++) {
        cout << "multiset[" << i << "]:" << *mm << endl;
    }

    map<int, string> ma;
    pair<int, string> jay(8, "Jay");
    pair<int, string> me(0, "Zero");
    ma.insert(jay);
    ma.insert(me);
    for (i = 0; i < ma.size(); i++) {
        cout << "map[" << i << "]:" << ma[i] << endl;
    }
    return 0;
}