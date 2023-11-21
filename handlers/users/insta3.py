
import requests
from bs4 import BeautifulSoup
def download_video3(url):
    session = requests.Session()
    server_url = 'https://saveig.app/'

    headers = {
        "Cache-Control":"no-store, no-cache, must-revalidate",
         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "DNT": "1",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
       
    }
    session.headers.update(headers)
    req = session.get(server_url)
    data = {}
    parse = BeautifulSoup(req.text, 'html.parser')
    get_all_input = parse.findAll('input')
    for i in get_all_input:
        if i.get("id") == "s_input":
            data[i.get("name")] = url
        else:
            data[i.get("name")] = i.get("value")
    post_url = "https://v3.saveig.app/api/ajaxSearch"
    req_post = session.post(post_url, data=data, allow_redirects=True)
    data = req_post.json()
    result = {}
    if data.get('mess',None):
        result['error']='Video Not found'
        return result
    elif data.get('data',None):
        try:
            
            pager = BeautifulSoup(data['data'],features='html.parser')
            urls = pager.find_all('div',attrs={'class':'download-items__btn'})
            images = []
            videos = []
            if urls:
                for url in urls:
                    if url.a['title']=='Download Photo':
                        if url.a['href']:
                            images.append(url.a['href'])
                    if url.a['title']=='Download Video':
                            if url.a['href']:
                                videos.append(url.a['href'])
            result['images'] = images
            result['videos'] = videos
            return result
        except Exception as e:
            result['error']=e
            return result
    else:
        result['error']='Video Not found'
        return result
import requests
from bs4 import BeautifulSoup
def download_video3(url):
    session = requests.Session()
    server_url = 'https://saveig.app/'

    headers = {
        "Cache-Control":"no-store, no-cache, must-revalidate",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "DNT": "1",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
       
    }
    session.headers.update(headers)
    req = session.get(server_url)
    data = {}
    parse = BeautifulSoup(req.text, 'html.parser')
    get_all_input = parse.findAll('input')
    for i in get_all_input:
        if i.get("id") == "s_input":
            data[i.get("name")] = url
        else:
            data[i.get("name")] = i.get("value")
    post_url = "https://v3.saveig.app/api/ajaxSearch"
    req_post = session.post(post_url, data=data, allow_redirects=True)
    data = req_post.json()
    result = {}
    if data.get('mess',None):
        result['error']='Video Not found'
        return result
    elif data.get('data',None):
        try:
            
            pager = BeautifulSoup(data['data'],features='html.parser')
            urls = pager.find_all('div',attrs={'class':'download-items__btn'})
            images = []
            videos = []
            if urls:
                for url in urls:
                    if url.a['title']=='Download Photo':
                        if url.a['href']:
                            images.append(url.a['href'])
                    if url.a['title']=='Download Video':
                            if url.a['href']:
                                videos.append(url.a['href'])
            result['images'] = images
            result['videos'] = videos
            return result
        except Exception as e:
            result['error']=e
            return result
    else:
        result['error']='Video Not found'
        return result
