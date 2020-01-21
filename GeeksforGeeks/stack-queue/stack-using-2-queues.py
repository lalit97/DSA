'''
https://practice.geeksforgeeks.org/problems/stack-using-two-queues/1/
'''

#User function Template for python3
'''
    :param x: value to be inserted
    :return: None

    queue_1 = [] # first queue
    queue_2 = [] # second queue
    '''
def push_in_stack(x):    
    # global declaration
    global queue_1
    global queue_2
    queue_1.append(x)
    

def pop_from_stack():
    '''
    :return: the value of top of stack and pop from it.
    '''    
    # global declaration
    global queue_1
    global queue_2

    if not queue_1:
        if not queue_2:
            return -1

        # case of 2 continuous pops 
        while len(queue_2) != 1:
            front = queue_2.pop(0)
            queue_1.append(front)
        return queue_2.pop()


    # normal case
    while len(queue_1) != 1:
        front = queue_1.pop(0)
        queue_2.append(front)
    return queue_1.pop()





