class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #count Freq
        freq = {}
        for x in nums:
            freq[x] = freq.get(x,0) + 1

        #Create Bucket's
        bucket = [[] for _ in range(len(nums) + 1)]

        #Numbers in Buckets 
        for key, value in freq.items():
            bucket[value].append(key)

        #Top K
        res = []
        for i in range(len(bucket) - 1, -1, -1):
            for x in bucket[i]:
                res.append(x)
            if len(res) == k:
                return res

        