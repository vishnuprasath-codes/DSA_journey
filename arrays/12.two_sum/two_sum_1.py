class Solution:
	def twoSum(self, arr, target):
		# code here
		
        # Step 1: Sort the array to apply the two-pointer technique
        arr.sort()
        n = len(arr)

        # Step 2: Initialize two pointers
        start = 0          # Points to the beginning of the array
        end = n - 1        # Points to the end of the array

        # Step 3: Traverse the array using two pointers
        while start < end:
            sum = arr[start] + arr[end]  # Calculate the sum of two elements

            if sum == target:
                # If the sum matches the target, return True
                return True
            elif sum < target:
                # If the sum is less than the target, move start forward to increase sum
                start += 1
            elif sum > target:
                # If the sum is greater than the target, move end backward to decrease sum
                end -= 1

        # Step 4: If no such pair is found, return False
        return False

