import requests
from bs4 import BeautifulSoup
import os,re,time,hashlib,base64


head = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
}
start_urls = []     #定义一个url列表
for i in range(1,1000):
    if(i==1):       
        url = 'http://pic.netbian.com/index.html'   #判断是否为首页，并加入url列表中
        start_urls.append(url)
    else:
        url = 'http://pic.netbian.com/index_'+str(i)+'.html'    #判断是否为非首页，并加入url列表中
        start_urls.append(url)
i = 1   #为了将图片每二十张放入到不同的文件夹
url1='https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx' #自己的webhoook地址
for url in start_urls:              #将url列表url依次取出
    response = requests.get(url)        #向服务器发出get请求，获得响应
    response.encoding='gbk'                 #设置响应的编码格式为GBK
    html = response.text                        #获得相应的文本信息
    soup = BeautifulSoup(html,'lxml')               #通过beautifulsoup库中的lxml HTML 解析器提取数据
    result = soup.find('ul',class_="clearfix").find_all('img')      #找到<img>标签
    
    root = 'D:/page/SpiderImgs/imgs-'+str((i//20)+1)+'/'            #拼接保存的路径  根据自己要保存的路径替换
    for img in result:
        path = root + img['src'].split('/')[-1] #获取图片资源名称(http://pic.netbian.com/uploads/allimg/190824/212516-1566653116f355.jpg中的212516-1566653116f355.jpg)并拼接保存路径
        url = 'http://pic.netbian.com'+img['src']   #拼接图片的url
        r = requests.get(url, headers=head)         #发送get请求图片资源
        if not os.path.exists(root):                #判断文件夹是否存在
            os.makedirs(root)                       #创建新的文件夹
        else:
            with open (path,'wb+') as f:            #创建一个文件以二进制写
                f.write(r.content)                  #将请求服务器图片资源的响应结果写进文件中
                f.close()
                print("图片 "+str(i)+".jpg 保存成功")
        try:
            with open(path,'rb') as f:              #以读二进制的方式打开文件
                base64_data = base64.b64encode(f.read()).decode() #获取base64编码
            file = open(path,'rb')              
            md = hashlib.md5()
            md.update(file.read())
            res1 = md.hexdigest()       #获取图片内容的md5值
            data = {
                "msgtype" : 'image',
                "image":{
                    "base64":base64_data,
                    "md5":res1
                }

            }               #JSON数据格式
            t = requests.post(url1, headers=head, json=data) #发送post请求
        except:
            print("异常")
        print('\n')
        i = i + 1                       #文件夹名称加一
    time.sleep(3)                       #让程序睡3秒

