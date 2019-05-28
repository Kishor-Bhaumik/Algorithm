import numpy as np 

def array(s):
	return np.random.randint(0,50,s)


def mergesort(A,l,r):
	if(l<r):
		m=l+r//2
		mergesort(A,l,m)
		mergesort(A,m+1,r)
		merge(A,l,m,r)
def show_array(A,s):
	for i in range(0,s):
		print(A[i])

def merge(A,l,m,r):

	n1=m-l+1
	n2=r-m

	L=np.empty(n1 ,dtype=object)
	R=np.empty(n2 ,dtype=object)

	for i in range(0,n1):
		L[i]=A[l+i]
	for j in range(0,n2):
		R[j]=A[m+j+1]


    i=0
    j=0
    k=l
	while(i<n1 & j<n2):
		if(L[i]<R[j]):
			A[k]=L[i]
			i++
		else:
			A[k]=R[j]
			j++
		k++
	while(i<n1):
		A[k]=L[i]
		i++
		k++
	while(j<n2):
		A[k]=R[j]
		j++
		k++



size=eval(input("enter the size of the array: "))
sz=array(size)
A=array(sz)
mergesort(A,0,sz-1)




