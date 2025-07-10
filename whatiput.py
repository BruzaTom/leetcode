class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        sub = []
        subs = []
        for char in s:
            if char not in sub:
                sub.append(char)
            else:
                subs.append(sub)
                temp = []
                found = False
                for c in sub:
                    if found == True:
                        temp.append(c)
                    if c == char:
                        found = True
                sub = temp
                sub.append(char)
        subs.append(sub)
        l = 1
        for ss in subs:
            print(ss)
            if len(ss) > l:
                
                l = len(ss)
        return l