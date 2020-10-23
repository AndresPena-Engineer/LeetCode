# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
# Note: For the purpose of this problem, we define empty string as valid palindrome.

# Example 1:
# Input: "A man, a plan, a canal: Panama"
# Output: true

# Example 2:
# Input: "race a car"
# Output: false
 
# Constraints:
# s consists only of printable ASCII characters.

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Checking if its an alphanumetic, and if so, make all lowercase
        alphanumeric_filter = ''.join(ch for ch in s if ch.isalnum())
        filtered_string = alphanumeric_filter.lower()
        
        # Like stated in the problem, an empty string is a palindrome
        if alphanumeric_filter == "":
            return True
        
        # Checking if the string is equal with its reverse self
        for characters in filtered_string:
            if filtered_string[::-1] == filtered_string:
                return True
            else: 
                return False

# 476 / 476 test cases passed.
# Status: Accepted
# Runtime: 36 ms
# Memory Usage: 14.2 MB