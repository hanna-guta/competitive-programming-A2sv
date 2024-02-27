class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        ans = inf
        arr =  [0] * k

        def backtrack(idx, curr_max):
            nonlocal ans
          
            if curr_max >= ans:
                return
            
            if idx == len(cookies):
                ans = min(ans, curr_max)
                return

            for i in range(k):
                arr[i] += cookies[idx]
                backtrack(idx + 1, max(curr_max, arr[i]))
                arr[i] -= cookies[idx]

        backtrack(0, 0)
        return ans
