'''
https://practice.geeksforgeeks.org/problems/merge-k-sorted-linked-lists/1

https://leetcode.com/problems/merge-k-sorted-lists/discuss/10513/108ms-python-solution-with-heapq-and-avoid-changing-heap-size




why index is needed to passed in tuple 

problem

https://stackoverflow.com/questions/33764584/typeerror-unorderable-types-node-node


solution
https://leetcode.com/problems/merge-k-sorted-lists/discuss/200714/Python3-only-error-I-can't-find-much-documentation-on./207341/


first comment on this 
https://leetcode.com/problems/merge-k-sorted-lists/discuss/10513/108ms-python-solution-with-heapq-and-avoid-changing-heap-size/178752

'''
'''
    Your task is to merge the given k sorted
    linked lists into one list and return
    the head of the new formed linked list.
    
    Function Arguments: array "heads" (containing heads of linked lists), n size of array a.
    Return Type: head node.;
    {
        # Node Class
        class Node:
            def __init__(self, data):   # data -> value stored in node
                self.data = data
                self.next = None
    }

'''
import heapq


def merge(heads,n):
    heap_ = []
    for index, head in enumerate(heads):
        if head:
            tup = (head.data, index, head)
            heap_.append(tup)
    heapq.heapify(heap_)

    data, index, node = heapq.heappop(heap_)
    ans_head = node
    current = ans_head

    if node.next is not None:
        next_tup = (node.next.data, index, node.next)
        heapq.heappush(heap_, next_tup)
    while heap_:
        data, index, node = heapq.heappop(heap_)
        current.next = node
        current = current.next
        if node.next is not None:
            next_tup = (node.next.data, index, node.next)
            heapq.heappush(heap_, next_tup)
    return ans_head



