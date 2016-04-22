tel={'jack':2354,'sape':4645}
tel['guido']=4127
print tel,tel['jack'],tel.keys(),'guido' in tel

print dict([('sape',2356),('guido',4127),('jack',4098)])#  dengjiayu
print dict(sape=2356,guido=4127,jack=4098)

print dict([(x,x**2)for x in(2,5,6)])
##########Looping
knights={'gallahad':'the pure','robin':'the brave'}
for k,v in knights.iteritems():         #iteritems
    print k,v

for i,v in enumerate(['tic','tac','toe']):
    print i,v

questions=['name','quest','favorite color']
answers=['lancelot','the loly grail','blue']
for q,a in zip(questions,answers):
    print 'what is your {0}? it is {1}.'.format(q,a)

for i in reversed(xrange(1,10,2)):
    print i

basket = ['apple','orange','apple','pear','orange','banana']
for f in sorted(set(basket)):
    print f

