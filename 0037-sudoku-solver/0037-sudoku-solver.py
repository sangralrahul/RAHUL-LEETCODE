class Solution:
    def solveSudoku(self, board):
        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9

        for r in range(9):
            for c in range(9):
                if board[r][c] != '.':
                    num = int(board[r][c]) - 1
                    bit = 1 << num
                    rows[r] |= bit
                    cols[c] |= bit
                    boxes[(r // 3) * 3 + c // 3] |= bit

        def backtrack():
            best_r = -1
            best_c = -1
            best_mask = 0
            min_count = 10

            for r in range(9):
                for c in range(9):
                    if board[r][c] == '.':
                        box = (r // 3) * 3 + c // 3
                        used = rows[r] | cols[c] | boxes[box]
                        available = (~used) & 0x1FF

                        count = available.bit_count()

                        if count == 0:
                            return False

                        if count < min_count:
                            min_count = count
                            best_r = r
                            best_c = c
                            best_mask = available

                            if count == 1:
                                break
                if min_count == 1:
                    break

            if best_r == -1:
                return True

            box = (best_r // 3) * 3 + best_c // 3

            while best_mask:
                bit = best_mask & -best_mask
                best_mask -= bit

                num = bit.bit_length() - 1
                board[best_r][best_c] = str(num + 1)

                rows[best_r] |= bit
                cols[best_c] |= bit
                boxes[box] |= bit

                if backtrack():
                    return True

                rows[best_r] ^= bit
                cols[best_c] ^= bit
                boxes[box] ^= bit
                board[best_r][best_c] = '.'

            return False

        backtrack()