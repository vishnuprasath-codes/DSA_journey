class Solution:
    def fourSum(self, arr, target):
        n = len(arr)
        result_set = set()  # Used to store unique quadruplets as tuples

        # Loop to fix the first number (arr[i])
        for i in range(n):
            # Loop to fix the second number (arr[j]), always ahead of i
            for j in range(i + 1, n):
                s = set()  # This set is used to find the 4th number (last element of quadruplet)

                # Loop to pick the third number (arr[k])
                for k in range(j + 1, n):
                    sum_val = arr[i] + arr[j] + arr[k]  # Sum of first 3 fixed numbers
                    last = target - sum_val  # Calculate the required 4th number to reach the target

                    # If this 4th number exists in set `s`, we found a valid quadruplet
                    if last in s:
                        # Create a sorted list of the quadruplet to avoid duplicates like [0,1,2,0] vs [0,0,1,2]
                        current = sorted([arr[i], arr[j], arr[k], last])
                        # Convert list to tuple and add to set to ensure uniqueness
                        result_set.add(tuple(current))

                    # Add current number arr[k] to set `s` so it can be matched in the next iterations
                    s.add(arr[k])

        # Convert each tuple in result_set to a list before returning
        return [list(q) for q in result_set]
