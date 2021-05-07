class Solution:
    def isAnagram(self, s, t):
        s = ''.join(sorted(s))
        t = ''.join(sorted(t))
        if s == t:
            return True
        else:
            return False

