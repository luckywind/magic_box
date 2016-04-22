###filter
def f(x): return x % 2 != 0 and x % 3 != 0
print filter(f,range(2,25))
##map
def cube(x):return x*x*x
print map(cube,range(1,11))
##
seq=range(8)
def add(x,y):return x+y
print map(add,seq,seq)
##reduce
print reduce(add,range(1,11))
##reduce(f,seq,ini)
def sum(seq):
    def add(x,y):return x+y
    return reduce(add,seq,0)
print sum(range(1,11))
######squares = [x**2 for x in range(10)]
squares=[]
for x in range(10):
    squares.append(x**2)
print squares
##more for ann if.....
print [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]

vec = [-4, -2, 0, 2, 4]
print  [x*2 for x in vec]
###flatting a list
vec = [[1,2,3], [4,5,6], [7,8,9]]
print  [num for elem in vec for num in elem]

##
matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
   ]
print [[row[i] for row in matrix] for i in range(4)]
print "zip:",zip(*matrix)