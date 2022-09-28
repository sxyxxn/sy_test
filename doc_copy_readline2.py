# 정규표현식
import re 

# 원본 로그파일
f = open('c:\\work\\PV3.txt','rt')
# 복사본
g = open('c:\\work\\PV3_copy.txt','wt',encoding='utf-8')

#많은 라인의 파일이면 
#한번에 한줄씩 읽어서 처리한다.  
#파일의 EOF(End Of File)이 아니면 계속 읽도록 한다. 
line = f.readline()
while (line != ''): # line이 비어있지 않으면 계속읽는다.
# 읽은 라인에 숫자가 4개 연속으로 있으면 write
    if (re.search("\d{4}", line)):
    #if (re.search("error", line)): 
        g.write(line + "\n")
    line = f.readline()

f.close() 
g.close()








