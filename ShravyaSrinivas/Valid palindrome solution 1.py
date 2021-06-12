class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s.reverse()
        # s.split(' ')
        new_string = ''
        reverse_string1 = ""
        for letter in s:
            if letter.isalnum():
                new_string += letter

        def reverse_string(s):
            return s[::-1]

        reverse_string1 = reverse_string(new_string)
        if new_string.lower() == reverse_string1.lower():
            return True
        else:
            return False
