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