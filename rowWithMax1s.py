# Solution class that contains the method rowWithMax1s
class Solution:

    def rowWithMax1s(self, arr):
        n = len(arr)  # Number of rows
        m = len(arr[0])  # Number of columns
        r = 0  # Start from the first row
        c = m - 1  # Start from the last column
        max_row_index = -1  # Track the row with the most 1s

        # Traverse from top-right to bottom-left
        while r < n and c >= 0:
            if arr[r][c] == 1:  # Move left if 1 is found
                max_row_index = r  # Update the row with the most 1s
                c -= 1
            else:
                r += 1  # Move down if 0 is found

        return max_row_index  # Return the row with the most 1s
