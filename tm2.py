thelist=['I','am','Gay']
print(' '.join(thelist))

a = 'I am Gay'
b = a.split('.')
print(b)



a = ['I','am','Gay']               #first way to combine two lists 
b =['and','I','like','Python']
C = a + b 
print(C)

a = ['I','am','Gay']             
b =['and','I','like','Python']                                   
a.extend(b)#second way to combine two lists 
print(a)

a = ['I','am','Gay',['AND','LIKE','PYTHON']]#TH CONCEPT OF OFFSET IN NESTED LISTS
print(a[3][1])

a = '0123456789'
print(a[:])
print(a[:5])
print(a[5:10:2])
print(len(a))
d = a.split()
print(d)
b = a.title()  #there is no capital letter in the string so it will not change nothing but if there were any small letter it would have changed to capital letter
print(b)

#frequent use tools in List
a = [0,1,2,3,4,5,6,7,8,9]
a.sort()
print(a)

a = [0,1,1,3,2,3,3,4,5,6,7,8,9]
a.sort()
print(a)

a = [0,1,1,3,2,3,3,4,5,6,7,8,9]
a.sort()
print(a)

a = [2, 3, 1, 4]
a.sort()
print(a)

a = [2, 3, 1, 4]
sorted(a)
print(a)

b = a.extend()

a.pop()
a.remove()


mutate

function 

function a(input) -> output

ａ　＝　［１］
ａ　＋＝　　［２］

