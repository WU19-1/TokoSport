#include<stdio.h>

int arr[5] = {4,8,3,2,1};
int temp[5] = {};

void mergesort(int left, int right){
	// Pengennya sisa sampe satu element, supaya tidak recursive forever, kita kasi kondisi
	if(left == right)
		return;
	
	// tentukan nilai tengahnya
	int mid = (left + right) / 2;
	// lalu kita recursive untuk membagi semua element hingga tersisa 1 element saja
	mergesort(left,mid);
	mergesort(mid + 1, right);
	
	// lakukan sorting
	int lp = left;
	int rp = mid + 1;
	int idx = 0;
	
	// bandingkan arr kiri dengan arr kanan
	while(lp <= mid && rp <= right){
		if(arr[lp] < arr[rp]){
			temp[idx] = arr[lp];
			lp++;
		}else{
			temp[idx] = arr[rp];
			rp++;
		}
		idx++;
	}
	
	// tinggal masukin array sisa antara array kiri atau yang kanan
	while (lp <= mid){
		temp[idx] = arr[lp];
		lp++,idx++;
	}
	while(rp <= right){
		temp[idx] = arr[rp];
		rp++,idx++;
	}
	
	// kita masukkin array yang sudah kita sorting (subproblem) ke dalam array kita yang sebenarnya
	for(int i = left; i <= right; i++){
		arr[i] = temp[i-left];
	}
	
}

int main(){
	mergesort(0,4);
	for(int i = 0; i < 5 ; i++){
		printf("%d\n",arr[i]);
	}
}
