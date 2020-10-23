# Write a function that reverses a string. The input string is given as an array of characters char[].
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
# You may assume all the characters consist of printable ascii characters.

# Example 1:
# Input: ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]

# Example 2:
# Input: ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]

class Solution:
    def reverseString(self, s):
        """
        Do not return anything, modify s in-place instead.
        """
        # Sometimes the most simple solutions are the best solutions, and I found that just 
        # using a built in function is the best way to solve it. No need to reinvent the wheel.
        s.reverse()

# 478 / 478 test cases passed.
# Status: Accepted
# Runtime: 156 ms
# Memory Usage: 19.7 MB