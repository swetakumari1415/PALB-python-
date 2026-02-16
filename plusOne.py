class Solution:
    def plusOne(self, digits):
        n = len(digits)
        
        # Start from last digit
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        
        # If all digits were 9 (e.g., 999 → 1000)
        return [1] + digits
