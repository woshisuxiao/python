from selenium import webdriver
import time
import json
import random
from lxml import etree
page_bottom="document.documentElement.scrollTop=10000"
url="替换你的URL"
def down_info(uid,name,href,guanzi,fensi,weibo,info):
    with open ("xxxx.txt",'a+',encoding='utf-8') as f:
        #f.write("uid"weibo_uid)
        f.write("微博名字: "+name+"|简介 "+info+"|关注:"+guanzi+"|粉丝:"+fensi+"|微博: "+weibo+"|网址: "+href+"|uid: "+uid+"\n")
        f.write("*"*100+"\n")


    f.close()

    

def get_info(shuju):
    #print (shuju)
    #with open ("xxxx.txt",'a+') as f:
    for b in shuju:
        #print (b.text)
            #print (b.text)
                #f.write(b.get_attribute("innerHTML"))
                #f.write(b.text+'\n')
                #f.write("*"*20)


        html1=b.get_attribute("innerHTML")

        html=etree.HTML(html1)


        weibo_uid=html.xpath('//*[@class="person_name"]/a/@uid')[0]
        weibo_name=html.xpath('//*[@class="person_name"]/a/@title')[0]
        href=html.xpath('//*[@class="person_name"]/a/@href')[0]
        weibo_href=href.replace('//','http://')
        weibo_guanzi=html.xpath('//*[@class="person_num"]/span[1]/a/text()')[0]
        weibo_fensi=html.xpath('//*[@class="person_num"]/span[2]/a/text()')[0]
        weibo_weibo=html.xpath('//*[@class="person_num"]/span[3]/a/text()')[0]
        weibo_new=(html.xpath('//*[@class="person_info"]/p')[0]).xpath('string(.)')
        weibo_info=weibo_new.replace('\t','').replace('\n','')

        try:
            down_info(weibo_uid,weibo_name,weibo_href,weibo_guanzi,weibo_fensi,weibo_weibo,weibo_info)
        except BaseException as e:
            print (e)
            continue
    

def main():
    browser = webdriver.Chrome()
    browser.set_page_load_timeout(30)    
    browser.maximize_window()
    #set the amount of time to wait for a page load to complete before throwing an error.
    loginurl = 'http://weibo.com/'
    browser.get(loginurl)
    
    browser.implicitly_wait(30)
    #sign in the username //*[@id="loginname"]
    try:
        browser.find_element_by_xpath('//*[@id="loginname"]').send_keys('753239196@qq.com')
        print('user success!')
    except:
        print('user error!')
    time.sleep(1)
    
    #sign in the pasword
    try:
        browser.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[2]/div/input').send_keys('wB@suxiao9222')
        print('pw success!')
    except:
        print('pw error!')
    time.sleep(1)
    
    #click to login //*[@id="pl_login_form"]/div/div[3]/div[6]/a/span
    try:
        browser.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[6]/a').click()
        print('click success!')
    except:
        print('click error!')
    browser.implicitly_wait(30)
    browser.get(url)
    browser.implicitly_wait(30)
    #for i in range(50):
    while True:
        browser.execute_script(page_bottom)
        list_page_source=browser.find_elements_by_class_name('list_person')
        #print (list_page_source[1].get_attribute("innerHTML"))

        get_info(list_page_source)
        time.sleep(random.randint(5,15))
        try:
            browser.find_element_by_link_text("下一页").click()
        except BaseException as e:
            browser.close()
            print (e)
            break
                

if __name__== "__main__":
    main()
