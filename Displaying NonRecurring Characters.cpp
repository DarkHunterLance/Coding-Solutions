#include<iostream>
#include<string.h>
#include<stdio.h>
using namespace std;

int main()
	{
		char str1[100000],str2[100000];
		int tc,count;
		int i,j,len1,len2,flag;
		char alpha[26];
		int freq1[26];
		int freq2[26];
		for(i=0;i<26;i++)
			{
				alpha[i]=(char)(97+i);
				freq1[i]=0;
				freq2[i]=0;
			}
		
		cin>>tc;
		for(count=1;count<=tc;count++)
			{
				flag=-1;
				fflush(stdin);
				cin>>str1;
				fflush(stdin);
				cin>>str2;
				
				len1=strlen(str1);
				len2=strlen(str2);
				
				for(i=0;i<=len1;i++)
					{
						for(j=0;j<26;j++)
							{
								if(str1[i]==alpha[j])
									freq1[j]++;
							}
					}
					
				for(i=0;i<=len2;i++)
					{
						for(j=0;j<26;j++)
							{
								if(str2[i]==alpha[j])
									freq2[j]++;
							}
					}
					
				for(i=0;i<26;i++)
					{
						if( (freq1[i]!=0 && freq2[i]==0) || (freq1[i]==0 && freq2[i]!=0) )
							cout<<alpha[i];
						flag=1;
					}
			/*if(flag!=1)
				cout<<"-1";*/
			cout<<"\n";
			}
			
		return 0;
	}
