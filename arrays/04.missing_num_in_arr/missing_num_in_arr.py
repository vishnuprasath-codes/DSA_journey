class Solution:
    def missingNum(self, arr):
        
        n=len(arr)+1 #1 element is missed
        sumarr=sum(arr) # sum of the array elements
        exarr=n*(n+1)//2 #sum of natural numbers till the size of the array,included with missed number
        return exarr-sumarr
