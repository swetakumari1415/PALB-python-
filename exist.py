class Solution:
    def exist(self, board, word):
        rows = len(board)
        cols = len(board[0])

        def dfs(r, c, index):
            # If all letters matched
            if index == len(word):
                return True

            # Check boundaries and character match
            if (r < 0 or c < 0 or r >= rows or c >= cols 
                or board[r][c] != word[index]):
                return False

            # Mark as visited
            temp = board[r][c]
            board[r][c] = "#"

            # Explore 4 directions
            found = (dfs(r+1, c, index+1) or
                     dfs(r-1, c, index+1) or
                     dfs(r, c+1, index+1) or
                     dfs(r, c-1, index+1))

            # Restore value (backtrack)
            board[r][c] = temp

            return found

        # Start search from each cell
        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0):
                    return True

        return False
