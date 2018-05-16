#Handling dofferent exceptions

def RaiseExceptions(a):
    if type(a)!=type('a'):
        raise ValueError("They are not of the same type")
    try:
        RaiseExceptions(1) :
    except value error as e:
        print(e)

## Now throwing the exceptions as well
def TestCase(a,b):
    if(a<b):
        assert "A is greater and b is smaller")
    else:
        assert "B is greater and a is smaller")

try :
        Testcase(1.1,2)
except AssertionError as e:
    print(e)