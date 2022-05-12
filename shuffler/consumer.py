from email.policy import HTTP
import redis
import time
import json
import requests
from requests.auth import HTTPBasicAuth
from requests.models import PreparedRequest

def consumerService(job):
    job = json.loads(job)
    req = PreparedRequest()

    if job["jobType"] == "Training":
        API_ENDPOINT = "https://product-dms-ai-model-integration-job-creator-service-devx.aws-experiment-data-v1.mavq.io/start"
        print("Trigger Training Job")

        params = {'userid':job["userId"],'modelid':job["modelId"],'projectid':job["projectId"],'modeltype':job["modelType"]}
        #req.prepare_url(API_ENDPOINT, params)
        try:
            r = requests.post(url = API_ENDPOINT, params=params,auth=HTTPBasicAuth('jobuser',"ZTI4YWJjZjc4ZmMwZWFkNGE0NzM1OGNk"))
            print(r.content)
            if 200<=r.status_code<=299:
                print("Job Successfully scheduled")
            else:
                endpoint = "http://localhost:5000/v1/job/schedule-failed"
                data = "Job Scheduling Failed"
                headers={
                'Content-type':'application/json', 
                'Accept':'application/json',
                "Authorization": "Bearer eyJhbGciOiJSUzUxMiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJ0U09MUkR6a21JWERRUVZ4WU1kN2ZFa2Q1Y1BvS3l6dXdmQ1U1NUFuVVhBIn0.eyJleHAiOjE2NTIyODk5NjksImlhdCI6MTY1MjI1Mzk2OSwianRpIjoiYjUyNzQ4ZjYtZTllZC00YWI1LTkzZjItMjA4N2I4OWZjMjZkIiwiaXNzIjoiaHR0cHM6Ly9rZXljbG9hay5hd3MtZXhwZXJpbWVudC1jb3JlLXYxLm1hdnEuaW8vYXV0aC9yZWFsbXMvYXdzLXRlc3QtMDAwMCIsInN1YiI6ImQwNzEwZDE4LTNjMjctNDk2ZS1hNWQxLTdmNmUzMjVkMzU2YiIsInR5cCI6IkJlYXJlciIsImF6cCI6ImxvZ2luIiwic2Vzc2lvbl9zdGF0ZSI6IjVkYzg5YmJiLTA5MWEtNDM4NC05MjYzLTlhOTQ0MWU0OTdjYyIsImFjciI6IjEiLCJhbGxvd2VkLW9yaWdpbnMiOlsiaHR0cDovL2FkbWluOS5sb2NhbGhvc3Q6NDIwMCIsImh0dHA6Ly9hZG1pbjQubG9jYWxob3N0OjQyMDAiLCJodHRwOi8vYWRtaW41LmxvY2FsaG9zdDo0MjAwIiwiaHR0cDovL2FkbWluMy5sb2NhbGhvc3Q6NDIwMCIsImh0dHA6Ly9hZG1pbjEubG9jYWxob3N0OjQyMDAiLCIqIiwiaHR0cDovL2FkbWluNy5sb2NhbGhvc3Q6NDIwMCIsImh0dHA6Ly9hZG1pbi5sb2NhbGhvc3Q6NDIwMCIsImh0dHA6Ly9hZG1pbjYubG9jYWxob3N0OjQyMDAiLCJodHRwOi8vYWRtaW44LmxvY2FsaG9zdDo0MjAwIl0sInNjb3BlIjoicHJvZmlsZSBlbWFpbCIsInNpZCI6IjVkYzg5YmJiLTA5MWEtNDM4NC05MjYzLTlhOTQ0MWU0OTdjYyIsImVtYWlsX3ZlcmlmaWVkIjpmYWxzZSwibmFtZSI6InNoaXZhbSBzaW5naCIsInByZWZlcnJlZF91c2VybmFtZSI6Im1hdnE6Y29yZTovL3RlbmFudHMvaWRwLWF3cy1kZXYvdXNlcnMvc2hpdmFtLXNpbmdoIiwiZ2l2ZW5fbmFtZSI6InNoaXZhbSIsImZhbWlseV9uYW1lIjoic2luZ2giLCJlbWFpbCI6InNoaXZhbS5zaW5naEBtYXZxLmNvbSJ9.HgMvfGak2B-pejy8DLHOftBxTTD8tM7gEaYleORujAVQhj03wPBXiPDdujFs_YgE_uLNO5sVRDkg8TAXURxn8gvELCMH_1tMPI06P0Xdm2Xuo9TZpXhA743SKaYA9BvbehgAiyBfi5e1QHRYYBYN3M-oDaaep04XmGsy1tSQM_ANmEc7BjTZhcGGm8peopqTJWyQJyDEP914fK_nwMl-Z1UWw-ihv35jzW6PoHLI3lrBlNCBYICPivpu5_IRN4W1s4gg9oAokIqKFYG-bE3aB9vFaWEKDo9ghp7_-r8bzROIQ89fE0eFOgrJrnuVBDeI5-gXiEK0o9VrBTkgOFTurA"
                }

                respone = requests.post(endpoint, data=data, headers=headers)
                print(respone.content)
                print("Job Scheduling Failed")
                
        except requests.exceptions.ConnectionError:
            endpoint = "http://localhost:5000/v1/job/schedule-failed"
            data = "Job Scheduling Failed"
            headers={
            'Content-type':'application/json', 
            'Accept':'application/json',
            "Authorization": "Bearer eyJhbGciOiJSUzUxMiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJ0U09MUkR6a21JWERRUVZ4WU1kN2ZFa2Q1Y1BvS3l6dXdmQ1U1NUFuVVhBIn0.eyJleHAiOjE2NTIyMTM3NzIsImlhdCI6MTY1MjE3Nzc3MiwianRpIjoiZTI5ZjExMzQtNjE3Yy00NzJjLTkxMGEtOWFlYmFmNjk4OWE0IiwiaXNzIjoiaHR0cHM6Ly9rZXljbG9hay5hd3MtZXhwZXJpbWVudC1jb3JlLXYxLm1hdnEuaW8vYXV0aC9yZWFsbXMvYXdzLXRlc3QtMDAwMCIsInN1YiI6ImQwNzEwZDE4LTNjMjctNDk2ZS1hNWQxLTdmNmUzMjVkMzU2YiIsInR5cCI6IkJlYXJlciIsImF6cCI6ImxvZ2luIiwic2Vzc2lvbl9zdGF0ZSI6IjhlNmMwOGI4LWFlZmMtNGI2OC04MjExLWIzYmQ2ODI1NjgzOCIsImFjciI6IjEiLCJhbGxvd2VkLW9yaWdpbnMiOlsiaHR0cDovL2FkbWluOS5sb2NhbGhvc3Q6NDIwMCIsImh0dHA6Ly9hZG1pbjQubG9jYWxob3N0OjQyMDAiLCJodHRwOi8vYWRtaW41LmxvY2FsaG9zdDo0MjAwIiwiaHR0cDovL2FkbWluMy5sb2NhbGhvc3Q6NDIwMCIsImh0dHA6Ly9hZG1pbjEubG9jYWxob3N0OjQyMDAiLCIqIiwiaHR0cDovL2FkbWluNy5sb2NhbGhvc3Q6NDIwMCIsImh0dHA6Ly9hZG1pbi5sb2NhbGhvc3Q6NDIwMCIsImh0dHA6Ly9hZG1pbjYubG9jYWxob3N0OjQyMDAiLCJodHRwOi8vYWRtaW44LmxvY2FsaG9zdDo0MjAwIl0sInNjb3BlIjoicHJvZmlsZSBlbWFpbCIsInNpZCI6IjhlNmMwOGI4LWFlZmMtNGI2OC04MjExLWIzYmQ2ODI1NjgzOCIsImVtYWlsX3ZlcmlmaWVkIjpmYWxzZSwibmFtZSI6InNoaXZhbSBzaW5naCIsInByZWZlcnJlZF91c2VybmFtZSI6Im1hdnE6Y29yZTovL3RlbmFudHMvaWRwLWF3cy1kZXYvdXNlcnMvc2hpdmFtLXNpbmdoIiwiZ2l2ZW5fbmFtZSI6InNoaXZhbSIsImZhbWlseV9uYW1lIjoic2luZ2giLCJlbWFpbCI6InNoaXZhbS5zaW5naEBtYXZxLmNvbSJ9.MS_uzZIRi86XQBWeBNqZK2kSS9hfuGOd57XhY3wlJ6ENa6CbSulu4BNhpXjT0iWZqyoosFk7JMSJdE8z2DHhLJlpD15-jTgHw_qL-TwQ45cC_toE3oQ3DAgLiXAOh8NyefSXDht-kr60FS-Vkp2tCtEarB5-IBIGQgcm4Xe4Tk7BZm_rlrAhMkTVLUHJR63KsClTqhZs4fJGHzP2sQQ2eiLZdryeY9-JB-sYZb6Y169w95WLOOSeZlhUdupnoJx-Fg0mZy-RfpQQOEH3sRErcPd82IfEZVTjfOPIDYIRR4QEs20jTiLDTAlMj1Q6JdCYt1D6iH22mrc9Ck0FRaNqng"
            }

            respone = requests.post(endpoint, data=data, headers=headers)
            print(respone.content)
            print("Job Scheduling Failed")


r = redis.StrictRedis('localhost', 6379)

MaxCounter = 10

r.set("my-count","0")
r.set("scheduled","0")

while True:
    print("Consumer Job Running")
    time.sleep(1)
    value = r.lrange("jobQueue", 0, -1)
    number = r.get("my-count")
    scheduled = r.get("scheduled")
    print(number.decode())

    if len(value) == 0 or int(scheduled)>=MaxCounter:
        continue

    lock = r.lock("anyLock")
    lock.acquire()
    r.incr("scheduled")
    lock.release()
    job = r.lpop("jobQueue")
    print(job.decode())
    consumerService(job.decode())
