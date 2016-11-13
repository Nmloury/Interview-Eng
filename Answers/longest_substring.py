class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = []
        longest = 0
        for c in s:
            if c in l:
                index = l.index(c)
                l = l[index+1:]
            l.append(c)
            if longest < len(l):
                longest = len(l)
        return longest
