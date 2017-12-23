# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def addTwoNumbers(self, l1, l2):
		result = ListNode(0)
		result_pos = result
		l1_pos = l1
		l2_pos = l2
		add_num = 0
		if l1_pos==None:
			return l2
		else:
			tmp_result_1 = l1_pos.val
		if l2_pos==None:
			return l1
		else:
			tmp_result_2 = l2_pos.val
		tmp_sum = tmp_result_1+tmp_result_2
		if tmp_sum>9:
			result_pos.val = tmp_sum-10
			add_num = 1
		else:
			result_pos.val = tmp_sum
			add_num = 0
		while True:
			l1_pos = l1_pos.next
			l2_pos = l2_pos.next
			if l1_pos==None:
				if l2_pos==None:
					if add_num!=0:
						tmp_result_obj = ListNode(add_num)
						result_pos.next = tmp_result_obj
					return result
				l2_pos.val += add_num
				result_pos.next = l2_pos
				return result
			else:
				tmp_result_1 = l1_pos.val
			if l2_pos==None:
				if l1_pos==None:
					if add_num!=0:
						tmp_result_obj = ListNode(add_num)
						result_pos.next = tmp_result_obj
					return result
				l1_pos.val += add_num
				result_pos.next = l1_pos
				return result
			else:
				tmp_result_2 = l2_pos.val
			tmp_sum = tmp_result_1+tmp_result_2+add_num
			if tmp_sum>9:
				cur_val = tmp_sum-10
				add_num = 1
			else:
				cur_val = tmp_sum
				add_num = 0
			tmp_result_obj = ListNode(cur_val)
			result_pos.next = tmp_result_obj
			result_pos = result_pos.next