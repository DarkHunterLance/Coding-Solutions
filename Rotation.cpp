#include<iostream>
#include<string.h>
using namespace std;

int main()
	{
		char str[100000];
		int tc,count;
		long int i,len;
		char temp;
		
		cin>>tc;
		for(count=1;count<=tc;count++)
			{
				fflush(stdin);
				std::cin.getline(str,100000);
				len=strlen(str);
				
				for(i=0;i<=len/2;i++)
					{
						while(str[i]!=' ' && str[len-1-i]!=' ')
							{
								temp=str[i];
								str[i]=str[len-1-i];
								str[len-1-i]=temp;
								i++;
							}
						break;
					}
				cout<<str<<"\n";
			}
		return 0;
	}
