class Solution:
    def frequencyCount(self, arr):
        #  code here
        n=len(arr)
        freq=[0]*n # array to store count of each elements
        
        for i in arr: #iterating the array
            
            freq[i-1]=freq[i-1]+1 #store the freq of i at the place of freq[i+1]+1
                
        return freq
