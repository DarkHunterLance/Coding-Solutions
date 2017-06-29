#include<iostream>
#include<string.h>
using namespace std;

int main()
	{
		char str[200];
		int i,len;
		
		int tc,count;
		cin>>tc;
		for(count=1;count<=tc;count++)
			{
				fflush(stdin);
				std::cin.getline(str,200);
				len=strlen(str);
				
				for(i=0;i<len/2;i++)
					{
						if(i%2==0)
							cout<<str[i];
					}
				cout<<"\n";
			}
		return 0;
	}
