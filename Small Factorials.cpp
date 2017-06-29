#include<iostream>
using namespace std;

unsigned long long int fact(unsigned long int n)
	{
		static unsigned long long int f=1;
		if(n==0 || n==1)
			return 1;
		else
			f=n*fact(n-1);
		return f;
	}

int main()
	{
		unsigned long int n;
		int tc,count;
		unsigned long long int *arr;
		
		cin>>tc;
		arr= new unsigned long long int[tc];
		for(count=1;count<=tc;count++)
			{
				cin>>n;
				arr[count-1]=fact(n);
			}
		for(int i=0;i<tc;i++)
			cout<<arr[i]<<"\n";
		return 0;
	}
