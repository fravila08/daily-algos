class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @classmethod
    def create_linked_list_from_string(cls, s):
        if not s:
            return cls()
        new_node = cls(int(s[0]))
        if len(s) == 1:
            return new_node
        new_node.next = cls.create_linked_list_from_string(s[1:])
        return new_node

    def __repr__(self):
        return f"val: {self.val} next: [ {self.next} ]"


class MergeTwoSortedList:

    def merge_two_lists(self, l1: ListNode | None, l2: ListNode | None):
        if not l1 or not l2:
            return l1 if l1 else l2
        if l1.val < l2.val:
            l1.next = self.merge_two_lists(l1.next, l2)
            return l1
        else:
            l2.next = self.merge_two_lists(l1, l2.next)
            return l2

    def __call__(self, l1: ListNode | None, l2: ListNode | None):
        return self.merge_two_lists(l1, l2)


merge_sorted_lists = MergeTwoSortedList()


def example(l1, l2):
    l1 = ListNode.create_linked_list_from_string(l1)
    l2 = ListNode.create_linked_list_from_string(l2)
    return merge_sorted_lists(l1, l2)


print(example("124", "134"))
