class Solution(object):
    def isPalindrome(self, s):
        """Is a string a palindrome?"""
        mid = len(s) / 2
        if not s or len(s) == 1:
            return False
        if len(s) % 2 == 0:
            if s[:mid] == s[mid:][::-1]:
                return True
            else:
                return False
        else:
            if s[:mid] == s[mid + 1:][::-1]:
                return True
            else:
                return False

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        long_pal = ""
        pal_len = 0
        for i in range(len(s) - 1):
            for j in range(i + 1, len(s) + 1):
                if self.isPalindrome(s[i:j]):
                    if len(s[i:j]) > pal_len:
                        long_pal = s[i:j]
                        pal_len = len(s[i:j])
        return long_pal


class Solution2(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        long_pal = ""
        pal_len = 0
        centers = [x / 2. for x in range(len(s) * 2 + 1)]
        for i in centers:
            if i % 1 == 0:
                L = int(i)
                R = int(i)
            else:
                L = int(i)
                R = int(i + 1)
            while L >= 0 and R < len(s):
                if s[L] == s[R]:
                    temp_pal = s[L:R + 1]
                    temp_pal_len = len(temp_pal)
                    if pal_len <= temp_pal_len:
                        pal_len = temp_pal_len
                        long_pal = temp_pal
                else:
                    break
                L -= 1
                R += 1
        return long_pal

