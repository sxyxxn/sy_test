# coding:utf-8
from bs4 import BeautifulSoup
import urllib.request
import re 

# 요즘은 웹봇을 금지하는 사이트(매크로) ---> 'User-agent'가 비어있지만 않으면 됨(사람인척 행동)
#User-Agent를 조작하는 경우(아이폰에서   사용하는 사파리 브라우져의 헤더) 
hdr = {'User-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/603.1.23 (KHTML, like Gecko) Version/10.0 Mobile/14E5239e Safari/602.1'}

f = open("c:\\work\\clien.txt","wt",encoding="utf-8")
for n in range(0,10):
        #클리앙의 중고장터 주소 
        data ='https://www.clien.net/service/board/sold?&od=T31&po=' + str(n)
        #웹브라우져 헤더 추가 
        req = urllib.request.Request(data, \
                                    headers = hdr) # headers가 빠지면 막히는 경우도 있음
        data = urllib.request.urlopen(req).read()
        # 한글이 깨지는 경우는 디코딩 (한글이 깨져도 무시(ignore))
        page = data.decode('utf-8', 'ignore')
        soup = BeautifulSoup(page, 'html.parser')
        # 속성들(attrs) (class_ 대신 사용)
        list = soup.find_all('span', attrs={'data-role':'list-title-text'})

		# <span class="subject_fixed" data-role="list-title-text" title="맥북프로 2020 13인치 터치바 판매합니다">
		# 맥북프로 2020 13인치 터치바 판매합니다
		# </span>

        for item in list:
                try:
                        title = item.text.strip()
                        # print(title)
                        # #<a class='list_subject'><span>text</span><span>text</span>
                        # span = item.contents[1]
                        # span2 = span.nextSibling.nextSibling #옆에 있는 값
                        # title = span2.text 
                        if (re.search('맥북', title)):
                                print(title.strip())
                                f.write(title.strip() + "\n")
                        
                except:
                        pass
f.close()
        
