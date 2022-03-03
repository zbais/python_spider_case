# -*- coding:UTF-8 -*-
import requests, xlwt, xlrd, re
from bs4 import BeautifulSoup
from lxml import etree


def main():
    baseurl = 'https://3gmfw.cn/article/html2/2020/03/05/515646.html'
    savepath = '疫情题目1.xls'
    getData(baseurl)
    saveDate(baseurl,savepath)


def getData(baseurl):
    html = askUrl(baseurl)
    soup = BeautifulSoup(html, 'lxml')
    texts = soup.find_all('div',class_='mainNewsContent NewsContent')
    bf = BeautifulSoup(str(texts),'lxml')
    lists = bf.find_all('p')
    list1 = str(lists[4]).split('<br/>')
    list1 = str(list1).replace(r"'\n',",'').replace('<p>','').replace(", '</p>'",'').replace(r'\n','').replace('[','').replace(']','').replace("'",'').split(', ')
    return list1

def askUrl(baseurl):
    response = requests.get(baseurl)
    response.encoding='GBK'
    html = response.text
    return html

def saveDate(baseurl,savepath):
    list1 = getData(baseurl)
    book = xlwt.Workbook()
    sheet = book.add_sheet("Test")
    value_title = ["题目","A项","B项","C项","D项或答案","答案"]
    for i in range(0,6):
        sheet.write(0,i,value_title[i])
    m=1
    n=0
    for i in range (0,len(list1)):
        if(((list1[i][0]<='9')&(list1[i][0]>='0'))|(((list1[i][1]<='D')&(list1[i][1]>='A'))|((list1[i][1]<='9')&(list1[i][1]>='0')))):
            sheet.write(m,n,list1[i])
            #print(m,n)
            n = n+1
        else:
            sheet.write(m,n,list1[i])
            #print("--------------")
            #print(m,n)
            n=0
            m = m+1
                
    book.save(savepath)
if __name__ == "__main__":
    main()
    



""" if __name__ == "__main__":
    url = 'https://3gmfw.cn/article/html2/2020/03/05/515646.html'
    response = requests.get(url)
    response.encoding='GBK'
    #print(response.text)
    html = response.text
    soup = BeautifulSoup(html, 'lxml')
    texts = soup.find_all('div',class_='mainNewsContent NewsContent')
    
    bf = BeautifulSoup(str(texts),'lxml')
    lists = bf.find_all('p')
    #print(lists[4])
    #print(type(lists[4]))

    list1 = str(lists[4]).split('<br/>')
    #list1 = str(list1).rstrip
    #list1 = list1.remove(r"n")
    
    #去除多余字符
    list1 = str(list1).replace(r"'\n',",'').replace('<p>','').replace(", '</p>'",'').replace(r'\n','').replace('[','').replace(']','').replace("'",'').split(', ')
    #print(list1[][0])
    #for s in list1:
        #找题目
        #if((s[0]<=57&s[0]>=48)|(s[1]<=57&s[1]>=48)){}
    
    #list1 = re.sub('<p>|</p>','',str(list1))
    #list1 = str(list1).replace("'\n',",'',15)
    book = xlwt.Workbook()
    sheet = book.add_sheet("Test")
    value_title = ["题目","A项","B项","C项","D项","答案"]
    for i in range(0,6):
        sheet.write(0,i,value_title[i])
    m=1
    n=0
    for i in range (0,len(list1)):
        if(((list1[i][0]<='9')&(list1[i][0]>='0'))|(((list1[i][1]<='D')&(list1[i][1]>='A'))|((list1[i][1]<='9')&(list1[i][1]>='0')))):
            sheet.write(m,n,list1[i])
            print(m,n)
            n = n+1
        else:
            sheet.write(m,n,list1[i])
            print("--------------")
            print(m,n)
            n=0
            m = m+1
                
    book.save('疫情题目1.xls')
    
    #print(list1)
    for i in range(len(list1)):
        if(list1[i] == ' '):
            print("空格")
        else:
            print(list1[i])
        
        #print('\n') """
        
