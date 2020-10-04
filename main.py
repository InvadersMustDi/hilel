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

if __name__ == '__main__':

    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}

def parse_cookie(query: str) -> dict:
 
    queryList = query.split(';')


    if queryList == '':
        return {}

    myDict = {}

    for stringParam in queryList:

        if stringParam == '':
            continue

        paramList = stringParam.split('=', 1)
        key = paramList[0] 
        value = paramList[1]
        myDict[key] = value
        
    
    print(myDict)

    return myDict

if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name' : 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}