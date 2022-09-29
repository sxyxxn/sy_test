# web1.py
# 크롤링
from socket import SIO_KEEPALIVE_VALS
from bs4 import BeautifulSoup

# 파일을 로딩
# 원래는 f = open() f.read() 인데, 합쳐서 표현 (=> 메서드 체인)
page = open("c:\\work\\test01.html","rt",encoding="utf-8").read()
# 검색이 용이한 객체
soup = BeautifulSoup(page,"html.parser")
#print( soup.prettify() )

# 모든 <p> 검색
#print( soup.find_all("p") ) #list가 아닌 ResultSet이라는 형태
# 첫번째 <p> 검색
#print( soup.find("p") )
# <p class="outer-text"> 검색 : 조건을 주고 필터링
#print( soup.find_all("p", class_="outer-text") ) # 파이썬의 class와 충돌될까봐 _class
# 특정 ID 검색
#print( soup.find_all(id="first") )

# 태그 내부에 컨텐츠만 검색
for tag in soup.find_all("p"):
    title = tag.text.strip()            # text만 출력하고 strip으로 앞 뒤 빈칸 없앰
    title = title.replace("\n","")
    print(title)