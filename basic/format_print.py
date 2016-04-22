print 'the story of {0},{1},and {other}.'.format('Bill','manfred',other='Geog')
#!s---str()   !r---repr()
import math
print 'the value of PI is approximately {}'.format(math.pi)
print 'the value of PI is approximately {!r}'.format(math.pi)
print 'the value of PI is approximately {0:.3f}'.format(math.pi)

table= {'sjoerd':4127,'jack':4098,'dcab':7678}
for name,phone in table.items():
    print '{0:10} ==> {1:10d}'.format(name,phone)


