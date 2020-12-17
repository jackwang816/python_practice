#! /bin/bash

RECURSIVE = 'recursive'
DP_FULL_MATRIX = 'dpFullMatrix'
DP_TWO_ROWS = 'dpTwoRows'
class LevenshteinDistance(object):
    def __init__(self):
        self.func_dict = {
            RECURSIVE: self._recursive,
            DP_FULL_MATRIX: self._dp_full_matrix,
            DP_TWO_ROWS: self._dp_two_rows,
        }

    def _triple_min(self, a: int, b: int, c: int) -> int:
        ret = a if a < b else b
        return ret if ret < c else c

    def solution(self, str1: str, str2: str, solution: str = RECURSIVE) -> int:
        try:
            return self.func_dict[solution](str1, str2)
        except KeyError as e:
            raise Exception('Invalid solution name: {}'.format(e))
        
    def _recursive(self, str1: str, str2: str) -> int:
        n, m = len(str1), len(str2)
        if n == 0:
            return m
        if m == 0:
            return n
        if str1[0] == str2[0]:
            return self._recursive(str1[1:], str2[1:])
        else:
            return 1 + self._triple_min(
                self._recursive(str1[1:], str2), # deletion
                self._recursive(str1, str2[1:]), # insertion
                self._recursive(str1[1:], str2[1:]), # substitution
            )

    def _dp_full_matrix(self, str1:str, str2:str, state_matrix: list = None) -> int:
        n, m = len(str1), len(str2)
        dp = [[0] * (m+1) for i in range(n+1)] if not state_matrix else state_matrix
        for i in range(n+1):
            for j in range(m+1):
                if i == 0:
                    dp[i][j] = j
                    continue
                if j == 0:
                    dp[i][j] = i
                    continue
                if str1[i-1] == str2[j-1]: # dp matrix size n+1 m+1
                    dp[i][j] = dp[i-1][j-1]
                    continue
                dp[i][j] = 1 + self._triple_min(
                    dp[i-1][j], # deletion
                    dp[i][j-1], # insertion
                    dp[i-1][j-1], # substitution
                )

        return dp[n][m]

    def _find_min_index(self, state: list, i: int, j: int) -> (int, int):
        comp_list = []
        assert(i >= 0 and j>=0)
        if i-1 >= 0:
            comp_list.append((state[i-1][j], i-1, j, 'deletion'))
        if j-1 >= 0:
            comp_list.append((state[i][j-1], i, j-1, 'insertion'))
        if i-1 >= 0 and j-1 >= 0:
            comp_list.append((state[i-1][j-1], i-1, j-1, 'substitution'))
        min_tuple = comp_list[0]
        for item in comp_list:
            if item[0] < min_tuple[0]:
                min_tuple = item
        # change move to match and use state[i-1][j-1] for state equal
        # think about 'abce', 'abcde'
        min_tuple = (state[i-1][j-1], i-1, j-1, 'match') \
            if min_tuple[0] == state[i][j] else min_tuple
        return min_tuple[1], min_tuple[2], min_tuple[3]

    def _dp_find_backtrace(self, state: list, n: int, m: int) -> list:
        i, j = n, m
        backtrace = []
        while (not (i==0 and j==0)):
            i, j, move = self._find_min_index(state, i, j)
            backtrace.append((i, j, move))
        return backtrace

    def _print_backtrace(self, str1: str, str2: str, backtrace:list) -> list:
        bt_list = []
        for bt in backtrace:
            if bt[2] == 'match':
                bt_list.append('{} match'.format(str1[bt[0]]))
            elif bt[2] == 'insertion':
                bt_list.append('insert {}'.format(str2[bt[1]]))
            elif bt[2] == 'deletion':
                bt_list.append('delete {}'.format(str1[bt[0]]))
            elif bt[2] == 'substitution':
                bt_list.append('substitude {} with {}'.format(str1[bt[0]], str2[bt[1]]))
            else:
                bt_list.append('invalid move')
        print('src string: {}'.format(str1))
        print('dst string: {}'.format(str2))
        print(', '.join(bt_list))

    def _print_state_matrix(self, state: list):
        for dp in state:
            print(dp)

    def dp_find_backtrace(self, str1: str, str2: str, do_print: bool = False):
        n, m = len(str1), len(str2)
        dp = [[0] * (m+1) for i in range(n+1)]
        self._dp_full_matrix(str1, str2, dp)
        # self._print_state_matrix(dp)
        backtrace = self._dp_find_backtrace(dp, n, m)
        backtrace.reverse()
        return self._print_backtrace(str1, str2, backtrace) if do_print else backtrace
        
    def _dp_two_rows(self, str1:str, str2:str) -> int:
        n, m = len(str1), len(str2)
        dp = [[0] * (m+1) for i in range(2)]
        for i in range(n+1):
            for j in range(m+1):
                prev = 1 - i % 2
                if i == 0:
                    dp[i%2][j] = j
                    continue
                if j == 0:
                    dp[i%2][j] = i
                    continue
                if str1[i-1] == str2[j-1]:
                    dp[i%2][j] = dp[prev][j-1]
                    continue
                dp[i%2][j] = 1 + self._triple_min(
                    dp[prev][j], # deletion
                    dp[i%2][j-1],  # insertion
                    dp[prev][j-1], # substitution
                )
        return dp[n%2][m]

def test_recusive(ldist):
    assert(ldist.solution('', '') == 0)
    assert(ldist.solution('a', '') == 1)
    assert(ldist.solution('a', 'a') == 0)
    assert(ldist.solution('', 'abc') == 3)
    assert(ldist.solution('a', 'abcde') == 4)
    assert(ldist.solution('mnpt', 'abcde') == 5)
    assert(ldist.solution('mnptq', 'abcd') == 5)
    assert(ldist.solution('abce', 'abcde') == 1)

def test_dp_full_matrix(ldist):
    assert(ldist.solution('', '', DP_FULL_MATRIX) == 0)
    assert(ldist.solution('a', '', DP_FULL_MATRIX) == 1)
    assert(ldist.solution('a', 'a', DP_FULL_MATRIX) == 0)
    assert(ldist.solution('', 'abc', DP_FULL_MATRIX) == 3)
    assert(ldist.solution('a', 'abcde', DP_FULL_MATRIX) == 4)
    assert(ldist.solution('mnpt', 'abcde', DP_FULL_MATRIX) == 5)
    assert(ldist.solution('mnptq', 'abcd', DP_FULL_MATRIX) == 5)
    assert(ldist.solution('abce', 'abcde', DP_FULL_MATRIX) == 1)

def test_two_rows(ldist):
    assert(ldist.solution('', '', DP_TWO_ROWS) == 0)
    assert(ldist.solution('a', '', DP_TWO_ROWS) == 1)
    assert(ldist.solution('a', 'a', DP_TWO_ROWS) == 0)
    assert(ldist.solution('', 'abc', DP_TWO_ROWS) == 3)
    assert(ldist.solution('a', 'abcde', DP_TWO_ROWS) == 4)
    assert(ldist.solution('mnpt', 'abcde', DP_TWO_ROWS) == 5)
    assert(ldist.solution('mnptq', 'abcd', DP_TWO_ROWS) == 5)
    assert(ldist.solution('abce', 'abcde', DP_TWO_ROWS) == 1)

def test_print_backtrace(ldist):
    ldist.dp_find_backtrace('', '', True)
    ldist.dp_find_backtrace('a', '', True)
    ldist.dp_find_backtrace('a', 'a', True)
    ldist.dp_find_backtrace('', 'abc', True)
    ldist.dp_find_backtrace('a', 'abcde', True)
    ldist.dp_find_backtrace('mnpt', 'abcde', True)
    ldist.dp_find_backtrace('mnptq', 'abcd', True)
    ldist.dp_find_backtrace('abce', 'abcde', True)

if __name__ == "__main__":
    ldist = LevenshteinDistance()
    try:
        ldist.solution(1, 'wfejoi', 'aaa')
    except Exception as e:
        print(e)
    test_recusive(ldist)
    test_dp_full_matrix(ldist)
    test_two_rows(ldist)
    test_print_backtrace(ldist)
    # print(ldist.dp_find_backtrace('abce', 'abcde'))
    # print(ldist.dp_find_backtrace('a', ''))
    