#include<stdio.h>
using namespace std;
int main(){
    int n;
    int square[101];
    int result[1000];
    int r=0;
    square[0] = 1;
    square[1] = 5;
    int l = 2;
    scanf("%d", &n);
    while(n){
        if (n<=l){
            result[r] = square[n-1];
            r++;
        }
        else{
            while(l <= n){
                square[l] = square[l-1]+(l+1)*(l+1);
                l++;
            }
            result[r] = square[n-1];
            r++;
        }
        scanf("%d", &n);
    }
    for(int i=0; i<r; i++){
        printf("%d\n", result[i]);
    }
    return 0;
}

