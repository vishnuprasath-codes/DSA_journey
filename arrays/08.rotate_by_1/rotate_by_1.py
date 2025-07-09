class Solution:
    def rotate(self, arr):
        # store the last element in a variable
        lastElement = arr[-1]

        # assign every value by its predecessor
        for i in range(len(arr) - 1, 0, -1):
            arr[i] = arr[i - 1]

        # first element will be assigned by last element
        arr[0] = lastElement
