class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            if target <= matrix[i][-1]:
                row = matrix[i]
                l, r = 0, len(row) - 1
                while l <= r:
                    i = (l + r) // 2
                    val = row[i]
                    if val == target:
                        return True
                    elif val < target:
                        l = i + 1
                    else:
                        r = i - 1
        return False
        