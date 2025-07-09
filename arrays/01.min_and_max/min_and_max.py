class Solution:
    def get_min_max(self, arr):
        
        # Initialize min and max to the first element
        maximum = arr[0]
        minimum = arr[0]
        #linear search for min and max
        for i in arr:
            if i > maximum:
                maximum = i
            if i < minimum:
                minimum = i
        
        return (minimum, maximum)
