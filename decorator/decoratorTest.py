import functools

PLUGIN = dict()
def register(func):
    PLUGIN[func.__name__] = func
    return func

def call_twice(func):
    @functools.wraps(func)
    def wrapper_func(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    
    return wrapper_func

def call_times(num_times):
    def descorator_func(func):
        @functools.wraps(func)
        def wrapper_func(*args, **kwargs):
            for idx in range(num_times-1):
                func(*args, **kwargs)
            return func(*args, **kwargs)
        return wrapper_func
    assert(isinstance(num_times, int))
    return descorator_func

# only python 3.0 above support it
# def call_times_both(_func=None, *, num_times=2):
#     def descorator_func(func):
#         @functools.wraps(func)
#         def wrapper_func(*args, **kwargs):
#             for idx in range(num_times-1):
#                 func(*args, **kwargs)
#             return func(*args, **kwargs)
    
#     if _func is None:
#         return descorator_func
#     else:
#         return descorator_func(_func)

class CalTimes():
    def __init__(self, func):
        functools.update_wrapper(self, func) # do not use '@' decorator symbol
        self.func = func
        self.call_times = 0
    def __call__(self, *args, **kwargs):
        print 'call times:%d'%self.call_times
        self.call_times += 1
        return self.func(*args, **kwargs)

class CalTimesParam():
    def __init__(self, num_times=2):
        # functools.update_wrapper(self, func)
        # self.func = func
        self.num_times = num_times
        self.call_times = 0

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper_func(*args, **kwargs):
            for idx in range(self.num_times-1):
                func(*args, **kwargs)
            return func(*args, **kwargs)
        print 'call times:%d'%self.call_times
        self.call_times += 1
        return wrapper_func

@call_twice
@register
def callprint(str):
    print(str)

@call_times(3)
def callprint(str):
    print(str)

@CalTimes
def callprint(str):
    print(str)

@CalTimesParam(2)
def callprint(str):
    print(str)

def Singleton(cls):
    """Make a class a Singleton class (only one instance)"""
    @functools.wraps(cls)
    def wrapper_func(*args, **kwargs):
        if wrapper_func.singleton is None:
            wrapper_func.singleton = cls(*args, **kwargs)
        return wrapper_func.singleton
    wrapper_func.singleton = None
    return wrapper_func
@Singleton
class Solution(object):
    pass

if __name__ == '__main__':
    callprint('fjoa')
    print callprint.__name__
    print callprint
    print PLUGIN
    print "Test Singleton:"
    s1 = Solution()
    s2 = Solution()
    print (s1, id(s1))
    print (s2, id(s2))
    print s1 is s2
    
