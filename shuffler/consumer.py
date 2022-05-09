import redis
import time

r = redis.StrictRedis('localhost', 6379)

MaxCounter = 5

while True:
    print("Job Running")
    time.sleep(5)
    value = r.lrange("jobQueue", 0, -1)
    number = r.get("my-count")
    print(number.decode())

    if len(value) == 0:
        continue

    lock = r.lock("anyLock")
    lock.acquire()
    r.decr("my-count")
    lock.release()
    item = r.lpop("jobQueue")
    print(item.decode())
