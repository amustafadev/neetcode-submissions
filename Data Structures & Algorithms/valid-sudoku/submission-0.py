class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # init sets
        rows = {i:set() for i in range(9)}
        cols = {i:set() for i in range(9)}
        sqrs = {i:set() for i in range(9)}

        # loop over cells
        for i in range(9):
            for j in range(9):
                # get value
                val = board[i][j]

                # skip empty
                if val == ".":
                    continue
                
                # calculate square index
                s = 3 * (i // 3) + (j // 3)

                # check duplicates
                if (val in rows[i]) or (val in cols[j]) or (val in sqrs[s]):
                    return False

                # update
                rows[i].add(val)
                cols[j].add(val)
                sqrs[s].add(val)

        # return
        return True