import http.client
import uuid

conn = http.client.HTTPSConnection("api.github.com")

random_uuid = uuid.uuid4()
headers = {
    'cache-control': "no-cache",
    'postman-token': "random_uuid"
    }

conn.request("GET", "/users/octocat/repos", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
