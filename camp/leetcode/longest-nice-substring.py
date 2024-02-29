class Solution:
    def longestNiceSubstring(self, s: str) -> str:
 
        def nice(s):
            hash_set = set(s)
            
            for i in range(len(s)):
                if s[i].lower() not in hash_set or s[i].upper() not in hash_set:
                    left = nice(s[:i])
                    right = nice(s[i + 1:])

                    return max(left, right, key=len)

            return s  

        return nice(s)
