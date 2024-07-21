class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # def __repr__(self):
    #     return f"val: {self.val}, next ({self.next})"

class AddTwoNumbers:
    
    def build_num_from_list(self, link_list):
        if link_list.next is None:
            return str(link_list.val)
        return self.build_num_from_list(link_list.next) + str(link_list.val)

    @classmethod
    def build_list_from_num(self, str_num):
        if len(str_num) == 1:
            return ListNode(int(str_num))
        curr_node = ListNode(int(str_num[0]))
        curr_node.next = self.build_list_from_num(str_num[1:])
        return curr_node

    def __call__(self, l1:ListNode, l2:ListNode):
        sum_of_lists = int(self.build_num_from_list(l1)) + int(self.build_num_from_list(l2))
        if sum_of_lists == 0:
            return ListNode(0)
        sum_reversed = str(sum_of_lists)[::-1]
        linked_list = self.build_list_from_num(sum_reversed)
        return linked_list
        

addTwoNumbers = AddTwoNumbers()