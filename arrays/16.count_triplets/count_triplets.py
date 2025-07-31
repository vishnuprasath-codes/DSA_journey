class Solution:
    def countTriplet(self, arr):
        # Initialize a counter to keep track of valid triplets
        count = 0
        n = len(arr)  # Get the length of the array

        # Iterate through all possible triplets using three nested loops
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    # Check if any two elements' sum is equal to the third
                    if ((arr[i] + arr[j] == arr[k]) or 
                        (arr[i] + arr[k] == arr[j]) or 
                        (arr[j] + arr[k] == arr[i])):
                        count += 1  # Valid triplet found, increment count

        # Return the total count of such triplets
        return count
