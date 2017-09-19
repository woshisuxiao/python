#html=open ('index.html',encoding='utf-8')
#import requests
#from bs4 import BeautifulSoup
#soup=BeautifulSoup(html,'lxml')
##获取商品URL
#div=soup.find('div',class_='bui-grid-body')
##获取tr
#tr_list=div.find('tr',class_='bui-grid-row bui-grid-row-even')
##获取每一行的Td
#td_list=tr_list.find_all('td')
##获取每个产品的网址
#sp_url=(td_list[3].a['href'])
#sp_num=(td_list[4].span.string)
#print (sp_num)
##获取商品的网页代码
#r=requests.get(sp_url,timeout=30)
#pic_soup=BeautifulSoup(r.text,'lxml')
#pic_url=pic_soup.find('img',id='J_ImgBooth')
#pic=requests.get(pic_url['src'].replace('//','http://')).content
#with open(sp_num+'.jpg','wb')as f:
#    f.write(pic)
#
#f.close()
'''
主要用于不同档口的图片下载，生成xls的链接，把图片最终变成XLS表格。
下载图片的ID，淘宝会每天变，使用前需要先检查
还有的问题  try except 这个还需要学习，目前做的不够好。
'''


'''
用于下载每个档口的图片，让他们写价格。 图片以商家编码命名
'''
import requests
from bs4 import BeautifulSoup
import os 

def get_html():
    html_url=[]
    html_list=os.listdir()

    for t in os.listdir():
        if os.path.splitext(t)[1]=='.html':
            html_url.append(t)
    
    return html_url

#html_list=os.listdir()
#html=open ('1.html',encoding='utf-8')
#获取所有要下载产品的链接
def get_url(html):
    url_dict={}
    soup=BeautifulSoup(html,'lxml')

    div=soup.find('div',class_='bui-grid-body')

    odd_list=div.find_all('tr',class_='bui-grid-row bui-grid-row-odd')
    for tr_list in odd_list:
        td_list=tr_list.find_all('td')
        sp_url=(td_list[3].a['href'])
        sp_num=(td_list[4].span.string)
        url_dict[sp_url]=sp_num
        #url_list.append(sp_url)

    even_list=div.find_all('tr',class_='bui-grid-row bui-grid-row-even')
    for tr_list in even_list:
        td_list=tr_list.find_all('td')
        sp_url=(td_list[3].a['href'])
        sp_num=(td_list[4].span.string)
        url_dict[sp_url]=sp_num
        #url_list.append(sp_url)

    return url_dict

#把图片保存
def get_pic(url_list):
    for a in url_list:
        try:
            r=requests.get(a,timeout=30)
            pic_soup=BeautifulSoup(r.text,'lxml')
            pic_url=pic_soup.find('img',id='J_ImgBooth')
            pic=requests.get(pic_url['src'].replace('//','http://')).content
            with open(url_list[a]+'.jpg','wb')as f:
                f.write(pic)
            f.close()
            p=open("xls_pic.txt","a+")
            n=open("xls_name.txt","a+")
            #p.write("<table><img src="+"\"C:\\Users\\Administrator\\Desktop\\test\\"+url_list[a]+".jpg"+"\" width=\"200\" height=\"200\">"+"\n")
            p.write("<table><img src=\""+os.getcwd()+"\\"+url_list[a]+".jpg"+"\" width=\"200\" height=\"200\">"+"\n")
            n.write(url_list[a]+"\n")
            


            print ("下载完毕")
        except BaseException as e:
            print (e)

def main():
    for url in get_html():
        html=open(url,encoding='utf-8')
        sp_dict=get_url(html)
        get_pic(sp_dict)

if __name__=='__main__':
    main()
