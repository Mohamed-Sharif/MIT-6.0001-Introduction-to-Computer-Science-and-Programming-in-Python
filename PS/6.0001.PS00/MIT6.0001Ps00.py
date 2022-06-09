import numpy as np
try:
    x = int(input('Enter number x:'))
    y = int(input('Enter number y:'))
    print ('x**y =',x**y)
    print ('log ({}) ='.format(x), np.log2(x))
except:
    print ('please enter interger numbers')

