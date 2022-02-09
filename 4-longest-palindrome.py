#my solution
class Solution:
    def longestPalindrome(self, s: str) -> int:
        letters = {}
        length = 0
        odd_is_present = False
        
        # Build a dictionary with each character count starting in 0
        for i in range(len(s)):
            if i == 0:
                letters[s[i]] = 0
            elif s[i] != s[i-1]:
                letters[s[i]] = 0
        
        # Start counting ocurrencies for each character
        for elem in letters:
            for j in range(len(s)):
                if s[j] == elem:
                    letters[elem] += 1

        # Calculate length
        for elem in letters:
            if letters[elem] % 2 == 0:
                length += letters[elem]
            else:
                length += letters[elem] - 1
                odd_is_present = True
        
        if odd_is_present:
            length += 1

        
        return length  

# Keith Galli solution
class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_count = {}
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
        
        final_count = 0
        odd_is_present = False
        for char in char_count:
            if char_count[char] % 2 == 0:
                final_count += char_count[char]
            else:
                final_count += char_count[char] - 1
                odd_is_present = True
        
        if odd_is_present:
            final_count += 1
    
    return final_count