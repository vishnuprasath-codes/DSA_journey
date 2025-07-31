i solved in optimal using n^2 tc
But not able to submit on gfg

OPTIMAL
-------

class Solution:
    def countTriplet(self, arr):
        n = len(arr)
        triplets = set()
        values = set(arr)       
        for i in range(n):
            for j in range(i + 1, n):
                a, b = arr[i], arr[j]
                c = a + b
                if c in values:
                    triplet = tuple(sorted((a, b, c)))  
                    triplets.add(triplet)
        return len(triplets)    
