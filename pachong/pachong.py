from urllib import request

if __name__ == '__main__':
    url = 'https://baijiahao.baidu.com/s?id=1681154448614237720&wfr=spider&for=pc'
    req = request.Request(url)
    print(req)

    response = request.urlopen(url)
    print(response)

    print(response.getcode())
    data=response.read()
    real_data=str(data,encoding='utf-8')
    print(real_data)
