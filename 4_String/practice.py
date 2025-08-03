class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        n = len(haystack)
        k = len(needle)
        if k==0:
            return 0

        next = self.build(needle)
        i = 0
        j = 0
        while i < n:
            if haystack[i] == needle[j]:
                j += 1
                i += 1
            elif j > 0:
                j = next[j-1]
            else:
                i += 1
            
            if j == len(needle):
                return i - j
        
        return -1
    
    def build(self, patt):
        n = len(patt)
        next = [0]
        '''
        next[j] = k
        needle[0:k] == needle[j-k:j] 左闭右开
        双指针，k,j, 
        考虑j和j+1的情况，
        next[j] = k, 
        if needle[j] == needle[k]: next[j+1] = next[j]+1 = k+1


        '''
        prefix_len = 0
        i = 1
        if n <= 2:
            return [0]*n
        
        while i < n:
            if patt[i] == patt[prefix_len]:
                prefix_len += 1
                i += 1
                next.append(prefix_len)
            else:
                if prefix_len > 0:
                    prefix_len = next[prefix_len-1]
                else:
                    next.append(0)
                    i += 1

        return next
    
s = Solution()
print(s.strStr("ababcaababcaabc", "ababcaabc"))  # Output: 6
            