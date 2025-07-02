def some_function(x,y):
    print(x,y)
    pass

def some_function1(x,y,z):
    print(x,y)
    pass

def some_function2(x,y,z=None):
    print(x,y)
    pass

def some_function3(x,y,z=10):
    print(x,y,z)
    pass

def some_function4(x,y, *args):
    print(x,y,args)
    pass

def some_function5(*args,**kwargs):
    print(args,kwargs)
    pass

def some_function6(a,b,c=True,d=False):
    print(a,b)
    pass

def some_function7(a,b,c=True,d=False):
    print(a,b,c,d)
    pass

some_function(y=2,x=1)
some_function1(1, z=2, y=3)
some_function2(1, 3)
some_function4(1, 3, 2, 3, 4, 5, 1)
some_function5(x=1,s="hello",b=True)
some_function5(1,2,3,x=1,s="hello",b=True)
some_function6(*[1,2])
some_function7(*[1,2],**{"c": "hello", "d": "cool"})