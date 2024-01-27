# Function: romanToInt
# Author: Shawal
# IDE: LeetCode Python IDE

class Solution:
    def romanToInt(self, s: str) -> int:
        # Dictionary to store the values of Roman numerals
        m = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        # Variable to store the result
        ans = 0
        
        # Loop through each character in the input string
        for i in range(len(s)):
            # Check if the current numeral is smaller than the next one
            if i < len(s) - 1 and m[s[i]] < m[s[i+1]]:
                # Subtract the current numeral's value from the result
                ans -= m[s[i]]
            else:
                # Add the current numeral's value to the result
                ans += m[s[i]]
        
        # Return the final result
        return ans
