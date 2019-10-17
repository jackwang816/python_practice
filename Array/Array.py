# test function for python array(list)

def array_test():
    testArray = [1,3,5,2,6]
    testArray.append(3)
    
    # test occurrences of value 3
    assert(testArray.count(3) == 2)
    
    # test list len
    assert(len(testArray) == 6)

    # test list extend
    testArray.extend([3, 6, 7])
    assert(len(testArray) == 9)
    
    # test list pop
    assert(testArray.pop() == 7)

    # test list index
    assert(testArray.index(3) == 1)
    assert(testArray.index(3, 2) == 5)

    # test list insert
    testArray.insert(2, 4)
    assert(len(testArray) == 9)
    assert(testArray[2] == 4)

    # test list remove
    testArray.remove(3)
    assert(len(testArray) == 8)
    assert(testArray[1] == 4)

    # test list reverse
    print 'befor reverse %s' % str(testArray)
    testArray.reverse()
    print 'after reverse %s' % str(testArray)

    # test list sort
    print 'befor sort %s' % str(testArray)
    testArray.sort()
    print 'after sort %s' % str(testArray)

if __name__ == "__main__":
    array_test()
