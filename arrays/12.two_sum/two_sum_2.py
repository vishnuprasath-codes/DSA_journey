class Solution:
	def twoSum(self, arr, target):
		# code here
        seen = {}  # hashmap to store number and its index

        for i in range(len(arr)):
            complement = target - arr[i]

            if complement in seen:
                # Found the pair, return their indices
                return [seen[complement], i]

            # Store the current number with its index
            seen[arr[i]] = i

        # If no such pair exists
        return [-1, -1]  # or you can raise an exception

