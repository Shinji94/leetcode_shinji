#O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                x = nums[i]+nums[j]
                if x == target :
                    return i,j
#O(n^2)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    	for i in rang(len(nums)):
    		for j in range(i+1,len(nums)):
    			if nums[i] + nums[j] == target:
    				return [i,j]
    		return None