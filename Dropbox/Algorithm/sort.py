import numpy as np 

def populate_arry(S):
	return np.random.randint(0,20,S)

def insertion_sort(A,S):

	for i in range(1,S):

		value=A[i]
		hole=i

		while((hole>0) & (A[hole-1]>value)):
			A[hole]=A[hole-1]
			hole=hole-1

		A[hole]=value
	return A

def bin_Search(A,s,k):

	start=0
	end=s-1

	while(start<=end):

		mid=((start+end)//2)

		if (A[mid]==k):
		    return mid
			
	
		elif(A[mid]>k):
			end=mid-1
		elif(A[mid]<k):
			start=mid+1
		
	return -1
	

    

	           
	    	




		
B=populate_arry(10)
C=insertion_sort(B,10)
print(C)
print(type(C))
key=eval(input("enter the value to searh:"))

D=bin_Search(C,10,key)

if(D==-1): 
	print("couldn't be found")
else:
	print(key, "is found at ",D+1," position int the array")

print(" ")




