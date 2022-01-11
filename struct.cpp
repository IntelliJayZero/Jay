#include<iostream>
using namespace std;
int main(int argc, char const *argv[])
{
    typedef struct F{
        int d;
        F *nex;
    }Found, *ff;
    ff aa = (ff)malloc(sizeof(Found));
    aa->d = 43;
    aa->nex = NULL;
    cout << aa->d << " " << aa << endl;
    Found w;
    w.d = 4;
    w.nex = aa;
    cout << w.d << " 3 " << w.nex << endl;
    return 0;
}
