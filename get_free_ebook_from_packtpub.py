#!/usr/bin/env python3
#coding:utf-8

import requests
from bs4 import BeautifulSoup

EMAIL = 'zcc87982@psoxs.com'
PASSWORD = 'qwedsa'

BaseURL = 'https://www.packtpub.com'
headers = {'User-Agent':'my_simple_python_code'}

global freetoday
freetoday = ''

s = requests.Session()

def highlight(x):
    return '\033[1m\033[32m{0}\033[0m'.format(x)

def step1():
    'get form_build_id'
    req = s.get(BaseURL,headers=headers)
    soup = BeautifulSoup(req.text,'lxml')
    login_form = soup.find_all('form',attrs={'id':'packt-user-login-form'})[0]
    inputs = login_form.find_all('input')[-2]
    return(inputs.get('id'))

def step2():
    data = {
        'email':EMAIL,
        'password':PASSWORD,
        'op':'Login',
        'form_build_id':step1(),
        'form_id':'packt_user_login_form'
        }
    
    req = s.post(BaseURL,data=data,headers=headers)

def step3():
    'get the name of Free Book for today & get its link'
    global freetoday
    url = BaseURL+'/packt/offers/free-learning'
    req = s.get(url,headers=headers)
    soup = BeautifulSoup(req.text,'lxml')
    name = soup.find_all('h2')[0].text
    name = str(name).strip()
    freetoday = name
    print('Free Book for Toady:'+highlight(name))
    link = soup.find_all('a',attrs={'class':'twelve-days-claim'})[0]
    #dont know why BeautifulSoup dont work here ,sad
    link = str(link).split('"')[3]
    return(BaseURL+ link)

def step4(link):
    global freetoday
    req = s.get(link,headers=headers)
    req = s.get(BaseURL+'/account/my-ebooks',headers=headers)
    soup = BeautifulSoup(req.text,'lxml')
    books = soup.find_all('div',attrs={'class':'title'})
    print('Here is Your Book List:')
    for x in books:
        x = x.text.strip()
        if freetoday in x:
            x = highlight(x)
        print('\t{0}'.format(x))

def main():
    step2()
    free_link = step3()
    step4(free_link)

if __name__ == '__main__':
    main()
