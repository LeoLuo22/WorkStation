class Solution(object):
    def totalNQueens(self, n):
        self.results = 0
        self.solve(n)
        return self.results

    def solve(self, n, index=0, column=None, diagonal=None, anti_diagonal=None):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        if index >= n:
            self.results += 1
            return

        if not column:
            column = [False] * n
            diagonal = {}
            anti_diagonal = {}

        for row in xrange(n):
            if not column[row] and index - row not in diagonal and index + row not in anti_diagonal:
                column[row] = True
                diagonal[index - row] = True
                anti_diagonal[index + row] = True
                self.solve(n, index + 1, column, diagonal, anti_diagonal)
                column[row] = False
                del diagonal[index - row]
                del anti_diagonal[index + row]
