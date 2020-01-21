

'''
thought that in the morning :D
cool one 
always have a problem in mind.

'''


'''
    lis[][0]:Petrol
    lis[][1]:Distance
'''
#Your task isto complete this function
#Your function should return the starting point
def tour(lists, n):
    total_sum = 0   # to make sure the answer is not -1
    par_sum = 0
    index = 0

    for i in range(n):
        lis = lists[i]
        petrol, distance = lis
        total_sum += (petrol - distance)

        par_sum += (petrol - distance)
        if par_sum < 0:
            par_sum = 0
            index = i + 1

    if total_sum < 0:
        return -1
    else:
        if par_sum > 0:
            return index
        else:
            return -1