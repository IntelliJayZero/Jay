#include<iostream>
#include<string>
using namespace std;
class J {
    string name;
    int rank;
    int win;
    public:
        J(string name, int rank, int win) {
            this->name = name;
            this->rank = rank;
            this->win = win;
        }
        ~J() {
            cout << "END" << endl;
        }
        void info() {
            cout << "name:" << name << " rank:" << rank << " win:" << win << endl;
        }
};
typedef struct {
    string call;
    double ti;
}stu, *st;
int main(int argc, char const *argv[])
{
    J sa("edv", 0, 5);
    sa.info();
    return 0;
}
