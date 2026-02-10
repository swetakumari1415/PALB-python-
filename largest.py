
class Solution:
    def largest(self, arr):
        # code here
        maxim = arr[0]
        for num in arr:
            if maxim < num:
                maxim = num
        return maxim

