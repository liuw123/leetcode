class Solution(object):
	def twoSum(self, nums, target):
		index1 = 0
		index2 = 1
		while index1<len(nums)-1:
			new_target = target-nums[index1]
			while index2<len(nums):
				if new_target==nums[index2]:
					return [index1,index2]
				index2 += 1
			index1 += 1
			index2 = index1+1