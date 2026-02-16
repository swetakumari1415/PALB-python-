class Solution:

    def median(self, mat):
        n = len(mat)
        m = len(mat[0])

        minVal = float('inf')
        maxVal = float('-inf')

        # finding the minimum and maximum elements
        # in the matrix
        for i in range(n):
            minVal = min(minVal, mat[i][0])
            maxVal = max(maxVal, mat[i][m - 1])

        desired = (n * m + 1) // 2
        lo = minVal
        hi = maxVal

        # binary search to find the median
        while lo < hi:
            mid = lo + (hi - lo) // 2
            place = 0

            # count elements smaller than or equal to mid
            # using bisect_right
            for i in range(n):
                place += bisect_right(mat[i], mid)

            if place < desired:
                lo = mid + 1
            else:
                hi = mid

        return lo
