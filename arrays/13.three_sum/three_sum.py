#BETTER SOLUTION
class Solution:
    # Function to find if there exists a triplet in the array arr[] which sums up to target.
    def hasTripletSum(self, arr, target):
        # Your Code Here
        n=len(arr)
        for i in range(n-2):#ensure that we always have at least 2 more elements after i
            st=set() #set to store j
            for j in range(i+1,n):
                second=target-arr[i]-arr[j]
                if second in st:
                    return True
                st.add(arr[j])
        return False

#OPTIMAL SOLUTION
