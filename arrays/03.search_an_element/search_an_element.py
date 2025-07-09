class Solution:
    def search(self,arr, x):
        #linear search using for loop
        for i in arr:
            if i==x:
                return arr.index(i)
        # return -1 when the search element x is not found
        return -1
