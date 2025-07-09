class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction. 
    def rotateArr(self, arr, d):
        # Step 1: Get the length of the array
        n = len(arr)
        
        # Step 2: Handle the case where d > n
        d %= n  # Rotating by d is same as d % n

        # Step 3: Define a helper function to reverse elements in the array
        def reverse(start, end):
            # Keep swapping the start and end elements until they meet
            while start < end:
                arr[start], arr[end] = arr[end], arr[start]
                start += 1
                end -= 1

        # Step 4: Reverse the first 'd' elements (from index 0 to d-1)
        reverse(0, d - 1)

        # Step 5: Reverse the remaining 'n-d' elements (from index d to n-1)
        reverse(d, n - 1)

        # Step 6: Reverse the whole array (from index 0 to n-1)
        reverse(0, n - 1)

        # Final result: array is now rotated by d elements to the left

        
