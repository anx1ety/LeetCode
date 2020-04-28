import bisect


class Solution:
    def kthSmallest(self, matrix, k):
        n = len(matrix)
        low = matrix[0][0]
        high = matrix[n-1][n-1]

        while low < high:
            mid = (low + high) >> 1
            pos = sum(bisect.bisect_right(row, mid) for row in matrix)
            if pos < k:
                low = mid + 1
            else:
                high = mid

        return high
