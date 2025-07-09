class Solution:
    def thirdLargest(self,arr):
        # code here
        # -1 for non existing number
        # if the array only contains positive
        largest=-1
        slargest=-1
        tlargest=-1
        #iterate array
        for i in arr:
            if i>largest:
                tlargest=slargest
                slargest=largest
                largest=i
            elif i>slargest:
                tlargest=slargest
                slargest=i
            elif i>tlargest:
                tlargest=i
        # returns the third largest element in the array
        return tlargest
