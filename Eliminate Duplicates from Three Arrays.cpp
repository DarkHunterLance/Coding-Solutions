#include<iostream>
using namespace std;

void sort(long long int arr[],long int n)
	{
		long int i,j;
		long long int tmp;
		for(i=0;i<n;i++)
			{
				for(j=0;j<n-1-i;j++)
					{
						if(arr[j+1]<arr[j])
							{
								tmp=arr[j];
								arr[j]=arr[j+1];
								arr[j+1]=tmp;		
							}
					}
			}
	}

int main()
	{
		int tc,count;
		long int n1,n2,n3,n,i,j,k;
		long long int *arr,*temp;
		
		cin>>tc;
		for(count=1;count<=tc;count++)
			{
				k=0;
				j=-1;
				cin>>n1>>n2>>n3;
				n=n1+n2+n3;
				arr=new long long int[n];
				temp=new long long int[n];
				for(i=0;i<n1;i++)
					cin>>arr[k++];
				for(i=0;i<n2;i++)
					cin>>arr[k++];
				for(i=0;i<n3;i++)
					cin>>arr[k++];
				
				sort(arr,n);
				
				for(i=0;i<n;i++)
					{
						if(arr[i]==arr[i+1])
							{
								if(j==-1)
									j=0;
								temp[j++]=arr[i];
								while(arr[i]==arr[i+1])
									i++;
							}
					}
				if(j==-1)
					cout<<"-1";
				else
					{
					for(i=0;i<j;i++)
						cout<<temp[i]<<" ";
					}
				cout<<"\n";
			}
		return 0;
	}
