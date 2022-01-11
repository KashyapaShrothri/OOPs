import sys
import time
from pprint import pprint

class Test:
    def __init__(self):
        print('constructor execution')

    def __del__(self):
        print('Destructor Execution')


t1 = Test()
t2 = t1

print(sys.getrefcount(t1))

pprint(dir(Test))
'''
Operator	Magic Method
–	__sub__(self, other)
*	__mul__(self, other)
+	__add__(self, other)
/	__truediv__(self, other)
//	__floordiv__(self, other)
%	__mod__(self, other)
**	__pow__(self, other)
>>	__rshift__(self, other)
<<	__lshift__(self, other)
&	__and__(self, other)
|	__or__(self, other)
^	__xor__(self, other)
Comparison Operators :
Operator	Magic Method
<	__LT__(SELF, OTHER)
>	__GT__(SELF, OTHER)
<=	__LE__(SELF, OTHER)
>=	__GE__(SELF, OTHER)
==	__EQ__(SELF, OTHER)
!=	__NE__(SELF, OTHER)
Assignment Operators :
Operator	Magic Method
-=	__ISUB__(SELF, OTHER)
+=	__IADD__(SELF, OTHER)
*=	__IMUL__(SELF, OTHER)
/=	__IDIV__(SELF, OTHER)
//=	__IFLOORDIV__(SELF, OTHER)
%=	__IMOD__(SELF, OTHER)
**=	__IPOW__(SELF, OTHER)
>>=	__IRSHIFT__(SELF, OTHER)
<<=	__ILSHIFT__(SELF, OTHER)
&=	__IAND__(SELF, OTHER)
|=	__IOR__(SELF, OTHER)
^=	__IXOR__(SELF, OTHER)
Unary Operators :
Operator	Magic Method
–	__NEG__(SELF, OTHER)
+	__POS__(SELF, OTHER)
~	__INVERT__(SELF, OTHER)
'''

'''
['__class__', -----  
 '__del__',  ----   Destructor
 '__delattr__',
 '__dict__',  ------  variables
 '__dir__', --------  directory or methods
 '__doc__', -------   doc string
 '__eq__',  -------   equal 
 '__format__',  ----- formatter
 '__ge__', ---------- greater than or equal to
 '__getattribute__',
 '__gt__', ---------- greater than
 '__hash__',
 '__init__', -------- constructor
 '__init_subclass__',
 '__le__', ---------- less than or equal to
 '__lt__', ---------- less than
 '__module__',
 '__ne__', ---------- not equal to
 '__new__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__setattr__',
 '__sizeof__',
 '__str__',
 '__subclasshook__',
 '__weakref__']
 '''