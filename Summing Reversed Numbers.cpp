#include<iostream>
using namespace std;

long long int rev(long long int n)
	{
		int r;
		long long int s=0;
		while(n>0)
			{
				r=n%10;
				s=(s*10)+r;
				n=n/10;
			}
		return s;
	}

int main()
	{
		long long int n1,n2,sum;
		int tc,count;
		
		cin>>tc;
		for(count=1;count<=tc;count++)
			{
				fflush(stdin);
				sum=0;
				cin>>n1>>n2;
				
				sum=rev(rev(n1)+rev(n2));
				cout<<sum<<"\n";
			}
		return 0;
	}
