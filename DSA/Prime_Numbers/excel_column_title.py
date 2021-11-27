'''Q3. Excel Column Title
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given a positive integer A, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 


Problem Constraints

1 <= A <= 109



Input Format

First and only argument of input contains single integer A



Output Format

Return a string denoting the corresponding title.



Example Input

Input 1:

A = 3
Input 2:

 
A = 27


Example Output

Output 1:

"C"
Output 2:

"AA"


Example Explanation

Explanation 1:

 
3 corrseponds to C.
Explanation 2:

    1 -> A,
    2 -> B,
    3 -> C,
    ...
    26 -> Z,
    27 -> AA,
    28 -> AB'''

class Solution:
    # @param A : integer
    # @return a strings
    def convertToTitle(self, A):
        
        ans = ''
        
        while A:
            A -= 1
            ans = chr(ord('A') + A % 26) + ans
            A //= 26
           
        return ans
