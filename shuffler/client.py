import aiohttp
import asyncio

headers={
    'Content-type':'application/json', 
    'Accept':'application/json',
    "Authorization": "Bearer eyJhbGciOiJSUzUxMiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJ0U09MUkR6a21JWERRUVZ4WU1kN2ZFa2Q1Y1BvS3l6dXdmQ1U1NUFuVVhBIn0.eyJleHAiOjE2NTIxMzA1ODAsImlhdCI6MTY1MjA5NDU4MCwianRpIjoiMjJhN2M1OWEtNzM1OS00ZTRkLThlMjAtMDkwYTNmMWM4YWI3IiwiaXNzIjoiaHR0cHM6Ly9rZXljbG9hay5hd3MtZXhwZXJpbWVudC1jb3JlLXYxLm1hdnEuaW8vYXV0aC9yZWFsbXMvYXdzLXRlc3QtMDAwMCIsInN1YiI6ImQwNzEwZDE4LTNjMjctNDk2ZS1hNWQxLTdmNmUzMjVkMzU2YiIsInR5cCI6IkJlYXJlciIsImF6cCI6ImxvZ2luIiwic2Vzc2lvbl9zdGF0ZSI6IjU4OGQ4NzI3LTQyYWEtNDc4My05ZjdiLTQ5YTRkMGFiODA0MiIsImFjciI6IjEiLCJhbGxvd2VkLW9yaWdpbnMiOlsiaHR0cDovL2FkbWluOS5sb2NhbGhvc3Q6NDIwMCIsImh0dHA6Ly9hZG1pbjQubG9jYWxob3N0OjQyMDAiLCJodHRwOi8vYWRtaW41LmxvY2FsaG9zdDo0MjAwIiwiaHR0cDovL2FkbWluMy5sb2NhbGhvc3Q6NDIwMCIsImh0dHA6Ly9hZG1pbjEubG9jYWxob3N0OjQyMDAiLCIqIiwiaHR0cDovL2FkbWluNy5sb2NhbGhvc3Q6NDIwMCIsImh0dHA6Ly9hZG1pbi5sb2NhbGhvc3Q6NDIwMCIsImh0dHA6Ly9hZG1pbjYubG9jYWxob3N0OjQyMDAiLCJodHRwOi8vYWRtaW44LmxvY2FsaG9zdDo0MjAwIl0sInNjb3BlIjoicHJvZmlsZSBlbWFpbCIsInNpZCI6IjU4OGQ4NzI3LTQyYWEtNDc4My05ZjdiLTQ5YTRkMGFiODA0MiIsImVtYWlsX3ZlcmlmaWVkIjpmYWxzZSwibmFtZSI6InNoaXZhbSBzaW5naCIsInByZWZlcnJlZF91c2VybmFtZSI6Im1hdnE6Y29yZTovL3RlbmFudHMvaWRwLWF3cy1kZXYvdXNlcnMvc2hpdmFtLXNpbmdoIiwiZ2l2ZW5fbmFtZSI6InNoaXZhbSIsImZhbWlseV9uYW1lIjoic2luZ2giLCJlbWFpbCI6InNoaXZhbS5zaW5naEBtYXZxLmNvbSJ9.irUBj3r5eYw-6NHDs8fXO03PPvBdH_yTwnbM2t43e2QAGA7hJ0FK37s-zSZodrn4CbEqfkrCL32Swq0hRddMDHARNU3waahmPKiDPXHkTxX00vrbmlniGcgh-qOc7XXJ1d1G3Zn0G677Zwnv_Z026IJe89mPKW33ckRg0l2-xzIuR3PoG5zEFA93kREerCaVjd9Wld7J6Wkx_kuLDEjIdfJhU4MT8iP5ZXsOc8kL8nzznypCvegs7AyE0dhzUSRObuAniFYX25avk60q9-hNfKYl-f-5EI1afUhpr_Pv9bJTqKkEhg2ts2LBWVulUc1Dp8ljUiE7FOcP8Dro56XDeQ"
    }

async def getResponse(session, i):

    params = {"modelId": i, "projectId": i*2, "modelType": "kvp", "jobType":"train"}

    async with session.get('http://localhost:5000/job/custom-training', params=params, headers=headers) as response:
        html = await response.text()
        print('done' + str(i))

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [getResponse(session, i) for i in range(200)] # create list of tasks
        await asyncio.gather(*tasks) # execute them in concurrent manner

asyncio.run(main())