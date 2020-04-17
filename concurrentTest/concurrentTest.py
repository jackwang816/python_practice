import time
import concurrent.futures

def my_sleep(s):
    time.sleep(s)
    return s

e = concurrent.futures.ThreadPoolExecutor(4)
# s = range(10)
s = list(reversed(xrange(10)))
for i in e.map(my_sleep, s):
    print(i)

with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
    result_futures = list(map(lambda x: executor.submit(my_sleep, x), s))
    results = [f.result() for f in concurrent.futures.as_completed(result_futures)]
print results