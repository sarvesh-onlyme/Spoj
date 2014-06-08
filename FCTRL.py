#include<stdio.h>
using namespace std;

int main(){
    int c, k, r;
    scanf("%d", &c);
    int print[c];
    for(int i=0; i<c; i++){
        scanf("%d", &k);
        r = 0;
        while(k){
            k = k/5;
            r +=k;
        }
        print[i] = r;
    }
    for(int i=0; i<c; i++){
        printf("%d\n", print[i]);
    }
    return 0;
}

