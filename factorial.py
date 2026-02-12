#User function Template for python
class Solution:
    def factorial(self, n):
        result = [1]   # store digits of factorial
        
        for x in range(2, n + 1):
            carry = 0
            
            for i in range(len(result)):
                prod = result[i] * x + carry
                result[i] = prod % 10
                carry = prod // 10
            
            # handle remaining carry
            while carry:
                result.append(carry % 10)
                carry //= 10
        
        result.reverse()   # digits should be in correct order
        return result
