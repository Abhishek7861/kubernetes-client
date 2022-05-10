import aiohttp
import asyncio

headers={
    'Content-type':'application/json', 
    'Accept':'application/json',
    "Authorization": "Bearer eyJhbGciOiJSUzUxMiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJ0U09MUkR6a21JWERRUVZ4WU1kN2ZFa2Q1Y1BvS3l6dXdmQ1U1NUFuVVhBIn0.eyJleHAiOjE2NTIxOTI5MzMsImlhdCI6MTY1MjE1NjkzMywianRpIjoiMmQyOTAxOGYtMDgyZi00ZDMxLWEyNTAtZjNhZWQ0YWM3NmRmIiwiaXNzIjoiaHR0cHM6Ly9rZXljbG9hay5hd3MtZXhwZXJpbWVudC1jb3JlLXYxLm1hdnEuaW8vYXV0aC9yZWFsbXMvYXdzLXRlc3QtMDAwMCIsInN1YiI6ImQwNzEwZDE4LTNjMjctNDk2ZS1hNWQxLTdmNmUzMjVkMzU2YiIsInR5cCI6IkJlYXJlciIsImF6cCI6ImxvZ2luIiwic2Vzc2lvbl9zdGF0ZSI6ImQzODlhMjRlLTIzOTUtNGZkNS1hYTg1LTk3YjlmMDUzMDYzYSIsImFjciI6IjEiLCJhbGxvd2VkLW9yaWdpbnMiOlsiaHR0cDovL2FkbWluOS5sb2NhbGhvc3Q6NDIwMCIsImh0dHA6Ly9hZG1pbjQubG9jYWxob3N0OjQyMDAiLCJodHRwOi8vYWRtaW41LmxvY2FsaG9zdDo0MjAwIiwiaHR0cDovL2FkbWluMy5sb2NhbGhvc3Q6NDIwMCIsImh0dHA6Ly9hZG1pbjEubG9jYWxob3N0OjQyMDAiLCIqIiwiaHR0cDovL2FkbWluNy5sb2NhbGhvc3Q6NDIwMCIsImh0dHA6Ly9hZG1pbi5sb2NhbGhvc3Q6NDIwMCIsImh0dHA6Ly9hZG1pbjYubG9jYWxob3N0OjQyMDAiLCJodHRwOi8vYWRtaW44LmxvY2FsaG9zdDo0MjAwIl0sInNjb3BlIjoicHJvZmlsZSBlbWFpbCIsInNpZCI6ImQzODlhMjRlLTIzOTUtNGZkNS1hYTg1LTk3YjlmMDUzMDYzYSIsImVtYWlsX3ZlcmlmaWVkIjpmYWxzZSwibmFtZSI6InNoaXZhbSBzaW5naCIsInByZWZlcnJlZF91c2VybmFtZSI6Im1hdnE6Y29yZTovL3RlbmFudHMvaWRwLWF3cy1kZXYvdXNlcnMvc2hpdmFtLXNpbmdoIiwiZ2l2ZW5fbmFtZSI6InNoaXZhbSIsImZhbWlseV9uYW1lIjoic2luZ2giLCJlbWFpbCI6InNoaXZhbS5zaW5naEBtYXZxLmNvbSJ9.mDyDhFIZIu4IpSxfHCDd6TbclqiYVxTMgpg477RFwKllaJTtPVui5R36d2Kpq448J_yqiAmcLDavVbwdLu-sOLcJoqeNDclCER8-m4pYgg9kgB9OQZ5Fvjt0YcIYum1oBnSc4wDHpDNPpO_orHoRV6wE7Wc55YZgT9z-ABPKWDOLKYuJJ99SVuOQvFIAL9kU8smXIbjKeGaTFqOJJlEeNhJBtWlvcXtyxlP6ze2DfRTTZBR90f_6RWBPbxIdP0N3ZDR68nv6ue_JPZQLr0RT4QtvsuzNe350e7IaJ0yl1iSE3e4JepzB_GjI6OOgQsSY5b_ClffyJB-ptfmJWWGWUQ"
    }

async def getResponse(session, i):

    params = {"modelId": i, "projectId": i*2, "modelType": "kvp", "jobType":"train"}

    async with session.get('http://localhost:6000/job/custom-training', params=params, headers=headers) as response:
        html = await response.text()
        print('done' + str(i))

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [getResponse(session, i) for i in range(100)] # create list of tasks
        await asyncio.gather(*tasks) # execute them in concurrent manner

asyncio.run(main())