class Solution:
    # Function to check if two arrays are equal or not.
    def checkEqual(self, a, b) -> bool:
        #code here
        if len(a) != len(b):
            return False
        return sorted(a) == sorted(b)
