from request import request

def main():

    serviceToGet = ''

    # capture url to execute
    urlToGet = input('Base URL (ex: www.github.com): ')

    # check if has any service to consume
    any_service = input('Has any service? [Y/N]: ')

    if any_service.upper() == 'Y':
        serviceToGet = input('Type the service: ')
    else:
        serviceToGet = '/';

    # start request
    requestToDo = request()
    requestToDo.end_point = urlToGet
    response = requestToDo.get(serviceToGet)
    print('Your response:\n##############################\n')
    print(response)
    print('\n############ END REQUEST #############')

main()
