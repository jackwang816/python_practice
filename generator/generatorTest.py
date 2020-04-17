import sys
# 1. basic generator
def my_gen():
    for n in range(3):
        yield n

# 2. generator with parameter
def str_gen(str):
    len_str = len(str)
    for i in range(len_str-1, -1, -1):
        yield str[i]

# 3. empty yield
def empty_yield():
    for i in range(3):
        print(i)
        yield

# 5. yield and send() first version
def yield_send_1(total):
    for i in range(total):
        yield i
    
# 6. yield and send() sencond version
def yield_send_2(total):
    for i in range(total):
        print("before i=%d"%i)
        r = yield i
        print(r)

# 7. consumer&producer mode
def consumer():
    r = ''
    while True:
        # n is what producer send
        # after once cycle return r to the producer
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s'%n)
        r = '200 OK'

def producer(c):
    c.send(None) #send(None) start the consumer working
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n) # send n to consumer and get the return value
        print('[PRODUCER] Consumer return: %s' % r)
    # c.send(None)
    c.close()
# enumerate generator function 
def abc():
   letters = ['a','b','c']
   for letter in letters:
       print letter
       yield letter

def enumerate_abc():
    numbered = enumerate(abc())
    for i, word in numbered:
        print i, word

if __name__ == "__main__":
    iter1 = my_gen()
    try:
        while True:
            print(next(iter1))
    except StopIteration:
        print('end of my_gen iter')

    for i in str_gen('hello'):
        print(i)

    for i in empty_yield():
        pass

    

    total = 3
    y1 = yield_send_1(total)
    for i in range(total):
        print('send(None) return:%d'% y1.send(None))

    y2 = yield_send_2(total)
    print("start")
    print('send(None) return: %d' % y2.send(None)) # first send(None)/next(y2) to start generator
    # next(y2)
    for i in range(total-1):
        print('send(%d) return: %d'%(i, y2.send(i)))
    
    c = consumer()
    producer(c)

    if sys.version_info > (3, 0):
        from py3_generatorTest import yield_from, copy_consumer
        for c in yield_from():
            print(c)
        cc = copy_consumer()
        producer(cc)

    # test enumerate generator
    enumerate_abc()
    



