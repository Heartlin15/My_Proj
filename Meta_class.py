class MetaCls(type): 
    """A sample metaclass without any functionality"""
    def __new__(cls, clsname, supercls, attrdict): 
          
        return super(MetaCls, cls).__new__(cls, clsname, supercls, attrdict) 
  
## a class of the type metclass 
A = MetaCls('A', (object, ), {}) 
print('Type of class A:', type(A)) 
  
class B(object): 
    pass
print('Type of class B:', type(B)) 
  
## class C inherits from both the class, A and B 
class C(A, B): 
    pass
print('Type of class C:', type(C))