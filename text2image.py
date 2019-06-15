import time
import requests
import shutil

def download_file(url, fpath):
    with requests.get(url, stream=True) as r:
        with open(fpath, 'wb') as f:
            shutil.copyfileobj(r.raw, f)
    return fpath

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'}


positive_list = ["真誠","卓越","進步","開明","友善","大方","機智","愛台","清廉", "勤政"]
negative_list = ["虛偽","拙劣","退步","獨裁","惡劣","小氣","愚昧","賣台","貪汙", "怠惰"]


for text in positive_list:
    url = 'http://api.img4me.com/?text=%s&font=arial&fcolor=000000&size=10&type=png&size=35' % text
    
    # Get Image Url
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    img_url = response.text
    # Second request to download image
    fpath = 'pos/' + text + '.png'
    outpath = download_file(img_url, fpath)
    print(outpath)
    time.sleep(0.8)

for text in negative_list:
    url = 'http://api.img4me.com/?text=%s&font=arial&fcolor=000000&size=10&type=png&size=35' % text
    
    # Get Image Url
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    img_url = response.text
    # Second request to download image
    fpath = 'neg/' + text + '.png'
    outpath = download_file(img_url, fpath)
    print(outpath)
    time.sleep(0.8)