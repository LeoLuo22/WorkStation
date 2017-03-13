"""
import requests
BASE_URL = "http://bksjw.chd.edu.cn"
LOGIN_URL = "http://bksjw.chd.edu.cn/loginAction.do"
HEAD = {'User-Agent':'Mozilla/5.0 (Windows NT 5.1; rv:17.0) Gecko/20100101 Firefox/17.0','Connection': 'Keep-Alive'}
IMG_URL = "http://bksjw.chd.edu.cn/xjInfoAction.do?oper=img" #头像的URL
USER_INFO_URL = "http://bksjw.chd.edu.cn/xjInfoAction.do?oper=xjxx"
GRADE = "http://bksjw.chd.edu.cn/bxqcjcxAction.do"

def login(username):
    session = requests.Session()
    init_session = session.get(BASE_URL)
    data = {'zjh':username,'mm':username,'dllx':'dldl'}
    index = session.post(LOGIN_URL,data=data, headers=HEAD)
    if index.status_code == 200:
        print("登陆成功")
    image = session.get(IMG_URL)
    global img_content
    img_content = image.content
    user_info_index = session.get(USER_INFO_URL,headers=HEAD)
    soup = user_info_index.text#content.decode('utf-8')
    grade = session.get(GRADE, headers=HEAD)
    print(grade.text)
    return soup

def main():
    login(str(201324020211))

if __name__ == "__main__":
    main()
#avi = {'User-Agent':'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; BOIE9;ZHCN)'}
"""
flag = True
print(not flag)
