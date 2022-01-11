#include<stdio.h>
#include<stdlib.h>

int main(int argc, char const *argv[])
{
    typedef struct L{
        int data;
        struct L *ne;
    }L, *head;
    head a = (head)malloc(sizeof(L));
    head b = (head)malloc(sizeof(L));
    head c = (head)malloc(sizeof(L));
    a->data = 1;
    b->data = 423;
    c->data = 21;
    a->ne = b;
    b->ne = c;
    c->ne = NULL;
    for(head pp = a; pp != NULL; pp = pp->ne){
        printf("is %d.\n", pp->data);
        printf("location:%p\n", pp);
    }
    free(a);
    free(b);
    free(c);
    system("pause");
    return 0;
}
