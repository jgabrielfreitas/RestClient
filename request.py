import http.client
import uuid
from header import header

class request:

    end_point = ""
    headers = []

    def get(self, service):

        print('### GET METHOD ###')
        print('end_point -> ' + self.end_point)
        print('service -> ' + service)
        print('##############################')
        print('##############################')

        headers = {
                'authorization': "D8199B61-CD5C-4837-8616-9A43B8103E5D"
                }

        for currentHeader in headers:
            print('headers -> ' + currentHeader)

        conn = http.client.HTTPSConnection(self.end_point)

        conn.request("GET", service, '', headers=headers)
        res = conn.getresponse()
        print('STATUS: {0} {1}'.format(res.status, res.reason))
        data = res.read()

        return data.decode("utf-8")
