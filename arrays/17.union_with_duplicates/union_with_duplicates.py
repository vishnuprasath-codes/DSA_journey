class Solution:    
    def findUnion(self, a, b):
        # Create an empty set to store unique elements from both arrays
        st = set()
        
        # Create an empty list to store the final result
        result = []

        # Loop through each element in list 'a' and add it to the set
        for i in range(len(a)):
            st.add(a[i])  # Duplicates will be ignored automatically

        # Loop through each element in list 'b' and add it to the set
        for i in range(len(b)):
            st.add(b[i])  # Again, duplicates are ignored by set

        # Now the set contains only unique elements from both 'a' and 'b'

        # Convert the set to a list by appending each element to result
        for it in st:
            result.append(it)

        # Return the final union of both arrays as a list
        return result
