#w: write only;  r(defalte):read only;  a: add;  r+: read and write ;
f=open('E:/cloud/pythonwork/test.txt','r')
print f
#print 'f.read():   ', f.read()
print '------------------------------------'
#print 'f.readline():  ',f.readline()
print '--------------------------------return a list of rows ----'
print 'f.readlines(): ',f.readlines()
print '------------------------------------'
f.close()
f=open('E:/cloud/pythonwork/test.txt','r+')
f.write('0123456789abcdefghi')
print f.seek(5)
print f.read(1)
f.seek(-3,2) #go to the 3rd byte before the end
print f.read(1)
f.close()

####automatically close file !!!!!
with open('E:/cloud/pythonwork/test.txt','r') as f:
    read_data = f.read()

print read_data , f.closed

###pickle
x=range(5)
f=open('E:/cloud/pythonwork/test1.txt','w')
print x
import pickle
pickle.dump(x,f)
f.close()
del x
#print x
fr=open('E:/cloud/pythonwork/test1.txt','r')
x=pickle.load(fr)
print x