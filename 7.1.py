# Definition for singly-linked list.
class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

def main():

    L1 = ListNode()
    L2 = ListNode()
    L1.data = 2
    L2.data = 3

    L1next1 = ListNode()
    L1.next = L1next1
    L1next1.data = 5

    L2next1 = ListNode()
    L2.next = L2next1
    L2next1.data = 11

    L1next2 = ListNode()
    L1next1.next = L1next2
    L1next2.data = 7

    print('L1: ', end='')
    printlinkedlist(L1)
    print('')

    print('L2: ', end='')
    printlinkedlist(L2)
    print('')

    result = merge_two_sorted_lists(L1, L2)

    print('merged array: ', end='')
    printlinkedlist(result)
    print('')

def merge_two_sorted_lists(L1, L2):

    dummy_head = tail = ListNode()

    while L1 and L2:
        if L1.data <= L2.data:
            tail.next, L1, = L1, L1.next
        else:
            tail.next, L2 = L2, L2.next
        tail = tail.next

    tail.next = L1 or L2
    return dummy_head.next

def printlinkedlist(linkedlist):
    while linkedlist:
        print(linkedlist.data, end=' ')
        if linkedlist.next:
            print("->", end = ' ')
        linkedlist = linkedlist.next

if __name__ == "__main__":
    main()