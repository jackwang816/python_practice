
_internal_use = 'abc'
class Test(object):
    ''' Test class for property
    '''
    def __init__(self, data):
        self.__data = data
        self._data = 1
    
    def set_data(self, data):
        self.__data = data

if __name__ == "__main__":
    t = Test(1)
    # print(t.__data) # python hide "__"(double underscore) suffix member in class
    print(t._data) # not hide "_"(single underscore)

    t.set_data(2)
    print(dir(t))