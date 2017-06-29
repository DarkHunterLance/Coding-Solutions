#include<iostream>
using namespace std;

int main()
	{
		unsigned long int *arr;
		long int n;
		long int i,j,m,d,sum=0,k=0,count=0;
		
		cin>>n;
		arr= new unsigned long int[n];
		
		for(i=0;i<n;i++)
			{
				cin>>arr[i];
			}
		
		cin>>d>>m;
		
		for(i=0;i<n;i++)
			{
				k=0;
				sum=0;
				for(j=i;j<n;j++)
					{
					sum=sum+arr[j];
					k++;
					if(sum<d)
						continue;
					else
						break;
					}
					
				//cout<<sum<<" : "<<j<<" , "<<i<<"\n";
				if(sum==d && (j-i+1)==m)
					count++;
			}
			
		cout<<count<<"\n";
		
		return 0;	
		
	}
