'''
mycodeschool video

https://www.youtube.com/watch?v=dxyYP3BSdcQ
'''

'''
Remember whenever we try to return something 
the value gets evaluted first
then the return statement works
'''


def fun_a():
    val = 5
    return fun_b(val) 



def fun_b(val):
    if val == 1:
        return True
    else:
        val -= 1
        return fun_b(val)

if __name__ == '__main__':
    x = fun_a() 
    print(x)

