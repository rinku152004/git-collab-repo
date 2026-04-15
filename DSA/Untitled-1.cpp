#include<iostream>
using namespace std;
void countSort(int arr[], int n){
    int mx=arr[0];
    for(int i=0;i<n;i++){
        mx=max(mx,arr[i]);
    }
    int count[10]={0};
    for(int i=0;i<n;i++){
        count[arr[i]]++;
    }
    for(int i=1;i<=mx;i++){
        count[i]+=count[i-1];
    }
    int output[n];
    for(int i=n-1;i>=0;i--){
        output[--count[arr[i]]]=arr[i];
    }
    for(int i=0;i<n;i++){
        arr[i]=output[i];
    }
}
int main(){
    int arr[]={0,2,5,1,0,2,3,1,4,5};
    countSort(arr,10);
    for(int i=0;i<10;i++){
        cout<<arr[i]<<" ";
    }
    return 0;
}
