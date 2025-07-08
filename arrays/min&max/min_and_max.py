class Solution:
    def get_min_max(self, arr):
        max=arr[0]
        min=arr[0]
        for i in arr:
	        if max<i:
	            max=i
            if min>i:
	            min=i
        return(min,max)
