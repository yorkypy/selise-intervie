
#Brute Force
def countNegativeNumber(M,n,m):
    count=0
    for i in range(n):
        for j in range(m):
            if M[i][j]<0:
                count+=1
    return count


#Optimal Solution
def countNegativeNumber1(M,n,m):
    count=0
    i=0
    j=m-1
    while j>=0 and i<n:
        if M[i][j]<0:
            count+=(j+1)
            i+=1
        else:
            j-=1
    return count-1



def getLastNegativeIndex(array, start, end, n): 
	# Base case 
	if (start == end): 
		return start 
		
	# Get the mid for binary search 
	mid=start+(end-start)//2
	
	# If current element is negative 
	if (array[mid]<0): 
		# If it is the rightmost negative element in the current row 
		if (mid+1<n and array[mid+1]>=0): 
			return mid 
		# Check in the right half of the array 
		return getLastNegativeIndex(array, mid + 1, end, n) 
	else: 		
		# Check in the left half of the array 
		return getLastNegativeIndex(array, start, mid - 1, n) 

# Function to return the count of 
# negative numbers in the given matrix 
def countNegative(M, n, m): 
	
	# Initialize result 
	count = 0
	
	# To store the index of the rightmost negative 
	# element in the row under consideration 
	nextEnd = m - 1
	
	# Iterate over all rows of the matrix 
	for i in range(n): 
		
		# If the first element of the current row 
		# is positive then there will be no negatives 
		# in the matrix below or after it 
		if (M[i][0] >= 0): 
			break
		
		# Run binary search only until the index of last 
		# negative Integer in the above row 
		nextEnd = getLastNegativeIndex(M[i], 0, nextEnd, 4) 
		count += nextEnd + 1
	return count 

# Driver code 

M = [[-3, -2, -1, 1],[-2, 2, 3, 4],[ 4, 5, 7, 8]] 
r = 3
c = 4
print(countNegative(M, r, c)) 



#Driver Code
if __name__ == "__main__":
    print(countNegativeNumber([[1,2,-2,-3],[-2,-3,-9,3],[-2,3,2,3]],3,4))
    print(countNegativeNumber1([[1,2,-2,-3],[-2,-3,-9,3],[-2,3,2,3],[-9,3,9,-2]],4,4))
