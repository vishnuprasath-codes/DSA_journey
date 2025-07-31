class Solution:
    def findTriplets(self, arr):
        # Get the number of elements in the array
        n = len(arr)
        
        # Sort the array to make it easier to find combinations
        arr.sort()
        
        # Iterate over the array to fix the first element of the triplet
        for i in range(n - 2):  # Last two elements can't be the first element of a triplet
            # Iterate for the second element of the triplet
            for j in range(i + 1, n - 1):
                # Iterate for the third element of the triplet
                for k in range(j + 1, n):
                    # Check if the sum of the three elements is zero
                    if arr[i] + arr[j] + arr[k] == 0:
                        # If found, return True as at least one such triplet exists
                        return True
        
        # If no such triplet found, return False
        return False

