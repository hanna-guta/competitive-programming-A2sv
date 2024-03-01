class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        N = len(arr)
        left = [-1] * N
        right = [N] * N

        stack = []

        for i in range(len(arr)):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            if stack:
                left[i] = stack[-1]
            stack.append(i)

        stack = []

        for i in range(N - 1 , -1 , -1):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            if stack:
                right[i] = stack[-1]
            stack.append(i)

        mod = 10**9 + 7  

        ans = sum((i - left[i]) * (right[i] - i) * VAL for i, VAL in enumerate(arr)) % mod
      
        return ans



        