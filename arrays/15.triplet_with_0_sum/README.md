i tried optimal solution using n^2 tc
but gfg didnt accept 


OPTIMAL
-------
class Solution:
    def findTriplets(self, arr):
        n = len(arr)
        arr.sort()
        
        for i in range(n - 2):  # Last 2 elements cannot be starting point
            left = i + 1
            right = n - 1
            while left < right:
                total = arr[i] + arr[left] + arr[right]
                if total == 0:
                    return True
                elif total < 0:
                    left += 1
                else:
                    right -= 1
        return False

