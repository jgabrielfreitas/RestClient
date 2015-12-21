from request import request

def main():

    urlToGet = input('Type the B-PAY end point: ')
    serviceToGet = input('Type the service to get: ')

    requestToDo = request()
    requestToDo.end_point = urlToGet
    response = requestToDo.get(serviceToGet)
    print(response)

main()
