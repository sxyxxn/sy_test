# web1.py
# 크롤링
from socket import SIO_KEEPALIVE_VALS
from bs4 import BeautifulSoup

# 파일을 로딩
page = open("c:\\work\\test01.html","rt",encoding="utf-8").read()
# 검색이 용이한 객체
soup = BeautifulSoup(page,"html.parser")
print( soup.prettify() )