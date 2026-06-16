from typing import List

class Solution:
	def twoSum(self, nums: List[int], target: int) -> List[int]:
		n = len(nums)
		for i in range(n):
			for j in range(i + 1, n):
				if target - nums[i] == nums[j]:
					return [i, j]
		return []
	
if __name__ == "__main__":
	slt = Solution()
	nums = [6, 8, 9, 1, 3, 4, 5, 7, 2]
	ans = slt.twoSum(nums, target=6)
	print(ans)