class Solution:
    def countTriplet(self, arr):
        # Get the length of the array
        n = len(arr)

        # Set to store unique triplets (a, b, c) such that a + b = c
        # Using a set ensures duplicates are automatically avoided
        triplets = set()

        # Convert the array to a set for fast O(1) lookups when checking if a + b exists
        values = set(arr)

        # Iterate through all unique pairs (i, j) where i < j
        for i in range(n):
            for j in range(i + 1, n):
                a, b = arr[i], arr[j]        # Select pair of numbers
                c = a + b                    # Calculate their sum

                # Check if the sum exists in the array
                if c in values:
                    # Create a sorted triplet to avoid order-based duplicates like (1,2,3) and (2,1,3)
                    triplet = tuple(sorted((a, b, c)))

                    # Add the sorted triplet to the set
                    triplets.add(triplet)

        # Return the total number of unique valid triplets found
        return len(triplets)
