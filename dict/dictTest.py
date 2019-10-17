import sys
IS_VERSION_3 = sys.version_info >= (3, 0)

def dictConstructTest():
    a = dict(one=1, two=2, three=3)
    b = { 'one':1, 'two':2, 'three':3 }
    c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
    d = dict([('one',1), ('two',2), ('three',3)])
    e = dict({'three': 3, 'one': 1, 'two': 2})
    assert(a==b==c==d==e)

def dictIterTest(dict_test):
    if IS_VERSION_3:
        # in python3 items return a iterator
        for key, value in dict_test.items(): 
            print('key=%s, value=%d' %(key, value))
    else:
        # in python2 items() return a list containing tuple '(key, value)'
        for key, value in dict_test.iteritems():
            print('key=%s, value=%d' %(key, value))

def dictUpdateTest():
    d = {'one':1}
    d.update({'two':2})
    d.update(three=3)
    d.update(zip(['four', 'five'], [4,5]))
    d.update([('six',6), ('seven', 7)])
    d.update(dict({'eight':8}))
    print(d)

def dictTest():
    dictConstructTest()
    dict_test = { 'one':1, 'two':2, 'three':3 }
    # list(dict) list the keys of dict
    assert(set(list(dict_test)) == set(['one', 'two', 'three']))
    assert(len(dict_test) == 3)
    # dict[key] get value with key
    # raise KeyError if key is not in the map 
    assert(dict_test['one'] == 1)
    dict_copy = dict_test.copy()
    dict_copy['one'] = 0
    assert(dict_copy['one'] == 0)
    del dict_copy['one']
    assert('one' not in dict_copy)
    assert('two' in dict_copy)
    # iter(dict) return keys iterator
    for key in iter(dict_copy):
        assert(key in dict_copy)
    dict_copy.clear() # clear dict_copy
    assert(len(dict_copy) == 0)
    assert(dict_test.get('one') == 1 and dict_copy.get('one') is None)
    dictIterTest(dict_test)
    assert(dict_test.pop('one') == 1)
    assert(dict_test.get('one') is None)
    dictUpdateTest()

    
if __name__ == "__main__":
    print(IS_VERSION_3)
    dictTest()