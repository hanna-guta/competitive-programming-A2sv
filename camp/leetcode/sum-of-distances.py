class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        N = len(nums)
        hash_map = defaultdict(list)

        for i in range(N):
            hash_map[nums[i]].append(i)
        
        res = [0] * N
        for num in hash_map:
            l = hash_map[num]
            pre = [0]

            for i in l:
                pre.append(pre[-1] + i)
            for i, x in enumerate(l):
                left = x * (i + 1) - pre[i + 1]
                right = pre[-1] - pre[i] - x * (len(l) - i)
                res[x] = left + right
        
        return res
            