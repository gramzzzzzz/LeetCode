class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        m = len(str1)
        n = len(str2)
        i, j = 0, 0
        while i < m:
            if str1[i] == str2[j]:
                i += 1
                j += 1
            else:
                if (ord(str1[i])-96)%26 == ord(str2[j])-97:
                    i += 1
                    j += 1
                else:
                    i += 1
            if j >= n:
                return True
        return False