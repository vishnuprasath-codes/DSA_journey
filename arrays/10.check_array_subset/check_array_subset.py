class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        # Sort both arrays in ascending order
        a.sort()
        b.sort()

        i = 0
        j = 0

        # Traverse both arrays using two pointers
        while i < len(a) and j < len(b):
            if a[i] < b[j]:
                # Element in arr1 is smaller, move to the next element in a
                i += 1
            elif a[i] == b[j]:
                # Element found in both arrays, move to the next element in both arrays
                i += 1
                j += 1
            else:
                # Element in arr2 not found in a, not a subset
                return False

        # If we have traversed all elements in b, it is a subset
        return j == len(b)
    
