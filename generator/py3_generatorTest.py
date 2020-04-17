
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
# 4. yield from 
def yield_from():
    yield from ['a', 'b', 'c']

# 8. yield from for coroutine chain
def copy_consumer():
    print('[COPY_CONSUMER] copy from consumer')
    yield from consumer()
    print('[COPY_CONSUMER] copy end')

