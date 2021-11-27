#include<iostream>
using namespace std; 
int mat[10][10],row,column;
void print()
{
	for(int i=0;i<row;i++)
	{
		cout<<endl;
		for(int j=0;j<column;j++)
		{
			cout<<mat[i][j]<<"\t";
		}
	}
}
int first(int r)
{
	int i;
	for(i=0;i<column;i++)
	{
		if(mat[r][i]!=0)
		    break;
	}
	return i;
}
void ord()
{
	int i,j,temp,ch=1;
	while(ch)
	{   
	    ch=0;
		for(i=0;i<row-1;i++)
	    {
		    if(first(i)>first(i+1))
		    {
			    for(j=0;j<column;j++)
			    {
			    	temp=mat[i][j];
			    	mat[i][j]=mat[i+1][j];
			    	mat[i+1][j]=temp;
				}
				ch=1;
		    }
	    }
    }
}
void Echelon()
{
	int m2[10][10],i,j,f,m,n,ch=1;
	while(ch)
	{
		ch=0;
		ord();
		for(i=0;i<row-1;i++)
		{
			if(first(i)==first(i+1) && first(i)!=column)
			{
				f=first(i);
				for(m=0;m<row;m++)
		        {   
			        for(n=0;n<column;n++)
			        {
				        m2[m][n]=mat[m][n];
			        }
		        }
				for(j=f;j<column;j++)
				{
					mat[i+1][j]=(m2[i][f]*m2[i+1][j])-(m2[i+1][f]*m2[i][j]);
				}
				ch=1;
			}
		}
	}
}
int mod(int x)
{
	if(x>0)
	    return x;
	else
	    return (-1)*x;
}
int gcd(int arr[10],int num)
{
	int a,b,a1,a2,r,sub[10],rem,x,y;
	if(num==1)
	    return arr[0];
	else
	{    
		a1=arr[0];
		a2=arr[1];
		if(a1==0 && a2==0)
	        sub[0]=0;
	    else if((a1==0 && a2!=0)||(a1!=0 && a2==0))
	    {
	    	if(a1!=0)
	    	    sub[0]=a1;
	    	else
	    	    sub[0]=a2;
		}
	    else
	    {
		    a=mod(a1);
		    b=mod(a2);
		    if(a>b)
		    {
		    	x=a;
		    	y=b;
			}
			else
			{
				x=b;
				y=a;
			}
			rem=x%y;
			while(rem!=0)
		    {
		    	x=y;
				y=rem;
		    	rem=x%y;
		    }
		    sub[0]=y;
        }
		for(int i=1;i<num-1;i++)
        {
    	    sub[i]=arr[i+1];
	    }
	    return gcd(sub,num-1);
    }
}
void Simplify()
{
	int rw[10],p;
	for(int i=0;i<row;i++)
	{
		for(int j=0;j<column;j++)
		{
			rw[j]=mat[i][j];
		}
		p=gcd(rw,column);
		for(int j=0;j<column;j++)
		{
			if(first(i)!=column)
			{
			    mat[i][j]/=p;
		    }
		}
	}
}
int main()
{
	int a,b;
	cout<<"Enter the number of rows in the Matrix:";
	cin>>row;
	cout<<"Enter the number of columns in the Matrix:";
	cin>>column;
	cout<<"Enter the Matrix elements row-wise:";
	for(a=0;a<row;a++)
	{
		for(b=0;b<column;b++)
		{
			cin>>mat[a][b];
		}
	}
	cout<<"\nThe Given Matrix is:";
	print();
	Echelon();
	Simplify();
	cout<<"\n\nAn Equivalent simplified Row-Echelon form of the given Matrix is:";
	print();
	return 0;
}
