
class UnderscoreTest(object):
    ''' class to test underscore syntax
    '''
    def __init__(self, data):
        self._weak_priv = data
        self.__mangle = data

if __name__ == "__main__":
# 1. underscore for ignore
    x, _, y = (1, 2, 3) # result: x=1, y=3
    for _ in range(3): # just ignore the var in range
        pass
    
# 2. single underscore weak private
    from weakPriv import *
    # only import pub_func ignore _priv_var and _priv_func
    pub_func()
    # _priv_func() NameError: name '_priv_func' is not defined
    from weakPriv import _priv_func
    # not real private now can call _priv_func
    _priv_func()
    # in class we can get the weak private variable
    ut = UnderscoreTest(10)
    print(ut._weak_priv)

### 3. double underscore
# Any identifier of the form __spam (at least two leading underscores, 
# at most one trailing underscore) is textually replaced with _classname__spam, 
# where classname is the current class name with leading underscore(s) stripped.
# Sometimes, some people use it as like real private ones using these features, 
# but it is not for private and not recommended for that. 
###

    # print(ut.__mangle) AttributeError: 'UnderscoreTest' object has no attribute '__mangle'
    print(ut._UnderscoreTest__mangle)


    