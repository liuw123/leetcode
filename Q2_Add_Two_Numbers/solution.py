# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def addTwoNumbers(self, l1, l2):
		if l1==None:
			return l2
		if l2==None:
			return l1
		cur_val = l1.val+l2.val
		add_num = 0
		if cur_val>9:
			cur_val = cur_val-10
			add_num = 1
		result = ListNode(cur_val)
		tmp_sol = Solution()
		next_result = tmp_sol.addTwoNumbers(l1.next,l2.next)
		if add_num==1:
			add_obj = ListNode(1)
			next_result = tmp_sol.addTwoNumbers(next_result,add_obj)
		result.next = next_result
		return result
