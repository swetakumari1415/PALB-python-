class Solution:
    def smallestSubWithSum(self, x, arr):
        # Your code goes here 
        n = len(arr)
        min_len = float('inf')
        curr_sum = 0
        start = 0
        
        for end in range(n):
            curr_sum += arr[end]
            
            while curr_sum > x:
                min_len = min(min_len, end - start + 1)
                curr_sum -= arr[start]
                start += 1
        
        return 0 if min_len == float('inf') else min_len
     
