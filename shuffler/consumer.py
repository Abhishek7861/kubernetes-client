import redis
import time
import requests

r = redis.StrictRedis('localhost', 6379)

MaxCounter = 5
endpoint = "http://localhost:8000/start-job"

while True:
    print("Job Running")
    time.sleep(1)
    value = r.lrange("jobQueue", 0, -1)
    number = r.get("my-count")
    if(number != None):
        print(number.decode())

    if len(value) == 0:
        continue

    lock = r.lock("anyLock")
    lock.acquire()
    r.decr("my-count")
    lock.release()
    item = r.lpop("jobQueue")
    respone = requests.post(endpoint)
    print(respone)
