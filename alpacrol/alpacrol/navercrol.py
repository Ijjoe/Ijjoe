

def NaverNewFnc():
    url = 'https://search.naver.com/search.naver?where=news&ie=utf8&sm=nws_hty&query=%EC%84%B1%EC%88%98%EB%8F%99+%ED%95%9C%EC%8B%9D+%EB%B7%94%ED%8E%98'
    
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
               'Referer': 'https://news.naver.com/'}
    
    resp = requests.get(url, headers=headers)
    return resp
