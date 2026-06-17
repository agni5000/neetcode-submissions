class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        n = len(nums)

        seen = set()
        counted = 0
    
        for i in range (0,n):

            if not nums[i] in seen:
                seen.add(nums[i])
            else:
                pass

        for i in range (0,n):
            aage = nums[i] + 1
            peeche = nums[i] - 1
            if peeche not in seen:
                count = 1
                abhi = nums[i]

                while abhi+1 in seen:
                    count +=1
                    abhi +=1
                
                counted = max(counted, count)
        
        return counted 

                
               
             
        