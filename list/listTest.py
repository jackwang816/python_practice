
def listTest():
    li_test = []
    li_test.append(0)
    assert(len(li_test) == 1)
    assert(li_test[0] == 0)
    li_test.extend([1,2,3])
    assert(len(li_test) == 4)
    li_test.insert(1, 9) # insert 9 before the index 1
    assert(li_test[1] == 9 and li_test[2] == 1)
    # remove elem '9' in li_test
    # if not exist raise ValueError exceptional
    li_test.remove(9)
    assert(li_test[1] == 1)
    assert(li_test.pop() == 3)
    li_test.append(3)
    li_test.extend([1,2,3])
    # a.index(x[,start[, end]])
    assert(li_test.index(3) == 3)
    # find index from index 4 to len(li_test)
    assert(li_test.index(3, 4) == 6)
    assert(li_test.count(3) == 2) # count elem '3' in li_test
    # list.copy() only supported in python 3.x
    # li_copy = li_test.copy()
    li_copy = li_test[:]
    # sort
    li_copy.sort(), li_test.sort(reverse=True)
    n = len(li_test) - 1
    for i,elem in enumerate(li_test):
        assert(elem == li_copy[n-i])
    # reverse
    li_copy.reverse()
    for i, elem in enumerate(li_test):
        assert(elem == li_copy[i])

if __name__ == "__main__":
    listTest()
