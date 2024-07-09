class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        row_counts = [0] * m
        col_counts = [0] * n

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    row_counts[i] += 1
                    col_counts[j] += 1
        
        special_count = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1 and row_counts[i] == 1 and col_counts[j] == 1:
                    special_count += 1
        return special_count