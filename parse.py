def parse(query:str) -> dict:
    
    if query.find('?') == -1:
        return {}

    queryList = query.split('?')

    queryParams = queryList[1]

    if queryParams == '':
        return {}

    if queryParams.find('&') != -1:
        stringParams = queryParams.split('&')
    else: 
        stringParams = queryParams.split()

    myDict = {}

    for stringParam in stringParams:

        if stringParam == '':
            continue

        paramList = stringParam.split('=')
        key = paramList[0] 
        value = paramList[1]
        myDict[key] = value

    return myDict