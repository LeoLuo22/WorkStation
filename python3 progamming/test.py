import urllib
import http.cookiejar
import requests
from PIL import Image
from io import StringIO
s= requests.Session()

a = s.get("http://wiscom.chd.edu.cn:8080/reader/captcha.php")
t = s.get("http://wiscom.chd.edu.cn:8080/reader/captcha.php")
e = s.get("http://wiscom.chd.edu.cn:8080/reader/redr_verify.php")
print(a.request.headers)
print(t.request.headers)
print(e.request.headers)
"""
print(type(r.content))
with open('test.gif', 'wb') as fd:
    fd.write(r.content)
i = Image.open('test.gif')
i.show()
code = pytesseract.image_to_string(Image.open('captcha.gif'))
print(code)
cookie = r.cookies['PHPSESSID']
"""
