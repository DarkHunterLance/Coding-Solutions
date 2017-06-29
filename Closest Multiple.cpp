#include<iostream>
using namespace std;

int main()
	{
		long long int x,n,i;
		int tc,count;
		
		cin>>tc;
		for(count=1;count<=tc;count++)
			{
				cin>>n>>x;
				if(n<x)
					{
					cout<<x<<"\n";
					continue;
					}
				if(n%x==0)
					{
					cout<<n<<"\n";
					continue;
					}
				else
					{
					for(i=1;;i++)
						{
						if((n-i)%x==0 && (n+i)%x!=0 )
							{
								cout<<(n-i)<<"\n";
								break;
							}
						else if((n+i)%x==0 && (n-i)%x!=0)
							{
								cout<<(n+i)<<"\n";
								break;
							}
						else if((n-i)%x==0 && (n+i)%x==0)
							{
								cout<<(n+i)<<"\n";
								break;
							}
						}
					}
			}
			
		return 0;
	}
