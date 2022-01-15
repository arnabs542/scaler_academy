'''Q4. Repeating Subsequence
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given a string A, find if there is any subsequence that repeats itself.

A subsequence of a string is defined as a sequence of characters generated by deleting some characters in the string without changing the order of the remaining characters.

NOTE: Subsequence length should be greater than or equal to 2.



Problem Constraints

1 <= length(A) <= 100



Input Format

The first and the only argument of input contains a string A.



Output Format

Return an integer, 1 if there is any subsequence which repeat itself else return 0.



Example Input

Input 1:

 A = "abab"
Input 2:

 A = "abba"


Example Output

Output 1:

 1
Output 2:

 0


Example Explanation

Explanation 1:

 "ab" is repeated.
Explanation 2:

 There is no repeating subsequence.'''

class Solution:
    # @param A : string
    # @return an integer
    def anytwo(self, A):

        # flag = [False]
        
        # dp = [[-1 for i in range(len(A))] for j in range(len(A))]

        # max_repeat = self.modified_lcs_recursive(A, A, 0, 0, dp, flag)
        
        # return 1 if flag[0] else 0

        return self.modified_lcs_tabular(A)
    
    def modified_lcs_recursive(self, s1, s2, i, j, dp, flag):

        if i == len(s1) or j == len(s2):
            return 0
        
        if s1[i] == s2[j] and i != j:
        
            if dp[i][j] == -1:

                dp[i][j] = 1 + self.modified_lcs_recursive(s1, s2, i + 1, j + 1, dp, flag)
        
        elif (s1[i] == s2[j] and i == j) or (s1[i] != s2[j]):

            if dp[i][j] == -1:

                c1 = self.modified_lcs_recursive(s1, s2, i, j + 1, dp, flag)

                c2 = self.modified_lcs_recursive(s1, s2, i + 1, j, dp, flag)
                
                dp[i][j] = max(c1, c2)
        
        if dp[i][j] >= 2 and not flag[0]:
            flag[0] = True
        
        return dp[i][j]

    def modified_lcs_tabular(self, st):

        n = len(st)

        dp = [[0 for i in range(n + 1)] for j in range(n + 1)]

        dp[0][0] = 1

        for i in range(1, n + 1):

            for j in range(1, n + 1):

                if st[i - 1] == st[j - 1] and i != j:

                    dp[i][j] = 1 + dp[i - 1][j - 1]
                
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

                if dp[i][j] >= 2:
                    return 1
        
        return 0