i solved in optimal using n^2 tc
But not able to submit on gfg

OPTIMAL
-------

class Solution:
    def countTriplet(self, arr):
        n = len(arr)
        triplets = set()        # Set to store unique triplets
        values = set(arr)       # For O(1) lookups

        for i in range(n):
            for j in range(i + 1, n):
                a, b = arr[i], arr[j]
                c = a + b
                if c in values:
                    triplet = tuple(sorted((a, b, c)))  # sort to ensure (1,2,3) and (2,1,3) are treated the same
                    triplets.add(triplet)

        return len(triplets)    # Return the number of unique triplets
