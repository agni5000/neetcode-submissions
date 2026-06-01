class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        ndict = dict()

        for i in range (0,n):
            if nums[i] not in ndict:
                ndict.update({nums[i] : 1})
            else :
                ndict[nums[i]] += 1
        
        sorted_items = sorted(ndict.items(),
                      key=lambda x: x[1],
                      reverse=True)

        ans = []

        for i in range(k):
            ans.append(sorted_items[i][0])

        return ans 


