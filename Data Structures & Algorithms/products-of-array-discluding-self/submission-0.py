class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n= len(nums)
        result = [1]*n
    
        for i in range (0,n):
            product = 1 
            for j in range (n):
                if j != i:
                    product  *= nums[j]
            result[i] = product 
        return result 
