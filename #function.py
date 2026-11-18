#function
def hello():
    print('Hello world')
hello()

def hello(x, y):
    z = x + y
    print(z)
hello(2, 3)

#預設參數值
def hello(x, y=5):
    z = x + y
    print(z)
hello(2)

#關鍵字引數 簡單來說，就是上面是指定數字，現在是指定成不同參數去定義函數
def hello_with_return(name, age):
    msg = 'Hello, my name is {} and I am {} years old.'.format(name, age)
    return msg  # 返回訊息

greeting = hello_with_return("oxxo", 20)
print(greeting)

def test(a, start=0, end=10):
    for i in a[start:end]:
        print(i)
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
test(b, end=len(b))

def test(a, start=0, end=10):
    for i in a[start:end]:
        print(i)
b = [1, 4, 2, 5, 6, 7, 8, 9, 10, 11, 14, 13, 15]
sorted_b = sorted(b)
remove_b = sorted_b[1:-1]
print(remove_b)

def a(x, t):
    if t == 'square':
        return x**2
    elif t =="cube":
        return x**3
        
# calculate operateor 
#plus
a = 10
a += 5
print(a)

#minus or substract
a = 10 
a -= 5 
print(a)

#multiply or times or product 
a = 10
a *= 5
print(a)

#divide or quotient or division + the concept of class amd object and inheritance
class MyNumber:    #build a class 
    def __init__(self, value): #constrict and initialize the default nalue of the class
        self.value = value
        
    def __add__(self, other):
        result = self.value + other.value
        return result     
        

