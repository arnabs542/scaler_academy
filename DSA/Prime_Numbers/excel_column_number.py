'''Q4. Excel Column Number
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given a column title as appears in an Excel sheet, return its corresponding column number.



Problem Constraints

1 <= length of the column title <= 5



Input Format

Input a string which represents the column title in excel sheet.



Output Format

Return a single integer which represents the corresponding column number.



Example Input

Input 1:

 AB
Input 2:

 ABCD


Example Output

Output 1:

 28
Output 2:

 19010


Example Explanation

Explanation 1:

 A -> 1
 B -> 2
 C -> 3
 ...
 Z -> 26
 AA -> 27
 AB -> 28'''

class Solution:
	# @param A : string
	# @return an integer
	def titleToNumber(self, A):
	    
	    ans = 0
	    val = 1
	    for i in range(len(A)-1,-1,-1):
	        
	        m = ord(A[i]) - ord('A') + 1
	        ans += val * m
	        val *= 26
	   
	    return ans