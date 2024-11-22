#include<stdio.h>
    int binary(int arr[],int size,int left ,int right ,int targ){
        while(left<right){
            if(arr[mid]==targ){
                return 1;
            }
            if(arr[right]<arr[mid]){
                right=mid-1;

            }else{
                left=left+1;
            }
        }
    }
    int main(){
        int arr[5]={1,2,3,4,5};
        int left=0,right=5-1,mid=0,targ=3;
        int ret=binary(arr,5-1,left,right,mid,targ);
        if(ret==1){
            printf("element is find");

        }else{
            printf("element is not finded");
        }
    }