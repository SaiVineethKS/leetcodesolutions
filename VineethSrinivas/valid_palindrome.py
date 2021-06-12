import math
class Solution:
    def canBePalindrome(s: str) -> bool:
        letter_count = dict()
        for letter in s:
            if letter.isalnum():
                letter = letter.lower()
                count = letter_count.get(letter, 0)
                letter_count.update({letter: count+1})
        
        odd_count = 0
        for count in letter_count.values():
            if count % 2 != 0:
                # odd count
                odd_count += 1
                
        return odd_count <= 1        
    
    def isPalindrome(self, s: str) -> bool:
        """
        Check if my given string is palindrome
        considering only alphanumeric characters involved
        """
        start, end = 0, len(s) - 1
        is_palindrome = True
        while start <= end:
            if not s[start].isalnum():
                start += 1
                continue
            if not s[end].isalnum():
                end -= 1
                continue
            print("Is Valid")
            if s[start].lower() != s[end].lower():
                is_palindrome = False
                break
            start += 1
            end -= 1
        
        return is_palindrome