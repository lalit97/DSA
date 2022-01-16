'''
https://practice.geeksforgeeks.org/problems/intersection-point-in-y-shapped-linked-lists/1/
'''

def intersetPoint(head_a,head_b):
    curr_a, curr_b = head_a, head_b
    head_change_count_a = 0
    head_change_count_b = 0
    while True:
        if curr_a == curr_b:
            return curr_a
        if curr_a.next is None:
            curr_a = head_b
            head_change_count_a += 1
        else:
            curr_a = curr_a.next
        if curr_b.next is None:
            curr_b = head_a
            head_change_count_b += 1
        else:
            curr_b = curr_b.next

        if head_change_count_a == 2 or head_change_count_b == 2:
            return -1
