import re #regular expression

# . : 은 글자 하나를 의미
# ^ : 문자열의 시작을 의미
# $ : 문자열의 끝을 의미
# ? : 앞문자가 있어도 되고 없어도 됨  ex) appl?e=>apple , appe(o)
# (?!) : 대소문자를 구문하지 않는다.
# | : 다자 택일 (or)조건  a|bpple=>apple,bpple

#반복기호 : + (1번 이상을 의미)  ex) a+pple => apple, aapple,aaapple
#반복기호 : * (0번 이상을 의미)
#반복기호 : {m,n} m~n번 반복 ex) a{3} =>'aaa' \d{3}=>010,111,123,151 등등 {0,}=>0번이상을 의미 {1,}=>1번이상 {0,1} 0~1번 

#문자클래스 : [] ([]사이의 문자들과 매치)
#ex) [abc]pple => apple, bpple, cpple

#문자클래스 특수용도
#[0-9] => [0,1,2,3,4,5,6,7,8,9] ->숫자 매칭
#[a-z] => 알파벳 소문자와 매칭
#[a-zA-z] => 대소문자 가리지 않고 알파벳과 매칭
#[ㄱ-ㅎ|ㅏ-ㅣ|가-힣] => 한글 매칭
#[가-힣]=>한글 글자 하나 매칭
#\d => 모든 숫자와 매칭[0-9]과 같은 의미
#\D => 숫자 아닌것과 매칭 [^0-9]과 같은 의미
#\w => 문자 +숫자 매칭[a-zA-z0-9]
#\W => 문자 + 숫자 아닌것과 매칭 [^a-zA-z0-9]
#\s => whiteSpace 문자와 매치, [\t\n\r\f\v\ ]와 매칭
#\S =>  whiteSpace 아닌 문자와 매치, [^\t\n\r\f\v\ ]와 매칭

#정규표현식 (r'')
#\b => 단어의 경계 공백 탭 컴마 대시 등 과 매칭
#\B => 단어의 경계 공백 탭 컴마 대시 등 과 아닌것 매칭

#그룹 () : () 사이의 문자와 모두 매치

#파이썬 re 모듈의 함수
#(1) match : 문자열의 처음부터 정규식과 매치되는지 조사

#(2) search() : 문자열의 전체를 검색하여 정규식과 매치되는지 조사

#(3) findall() : 정규식과 매치되는 모든 문자열 리스트로 반환

#(4) split() : 정규식과 매치되는 문자열을 기준으로 파싱하여 리스트로 돌려준다.

#(5) sub() : 정규식과 매치되는 문자열을 다른 문자열로 바꿔준다.

text = "python"
p = re.compile('^..thon$')
m = p.match(text)
if(m!=None):
    print(m.group())
else:
    print("매치되지 않습니다.")

text = "program lang : python"
m = re.search("..thon",text)
print(m.group())

p = re.compile("..thon")
m = p.search(text)
print(m.group())

p = re.compile('ca.e')
m = p.search("Good care")
print(m.group())
m = re.search('ca.e', "Good care")
print(m.group())

print("일치하는 문자열 : ",m.group())
print("입력받은 문자열 : ",m.string)
print("일치하는 문자열의 시작인덱스", m.start())#int로 반환
print("일치하는 문자열의 끝인덱스", m.end())#int 로 반환
print("일치하는 문자열의 시작 끝 인덱스", m.span())#튜플로 반환


mList = re.findall('\w*berry',"berry 1berry apple strawberry")
print(mList)


#'line'과 일치하지만 line을 포함한 글자들은 매칭되지않음 모든정규식에는 r을 쓴다
mList = re.findall(r'\bline\b','outline linear line')
print(mList)


mList = re.findall(r'one|self|the', 'oneself is the one thing')
print(mList)

#그룹 캐처
m = re.search("\d{4}-(\d\d)-(\d\d)","2021-05-04")
print(m.group())
print(m.group(0))#일치하는 모든 값
print(m.group(1))#첫번째 괄호 값
print(m.group(2))#두번째 괄호 값

tr_tag = '<tr href="www.hello.com:, id="abc123", class="ddd">hello</tr>'

m = re.search(r'<tr.*id="(.*?)".*>(.*)</tr>',tr_tag)
print(m.group())
print(m.group(1))
print(m.group(2))

m = re.search(r"\d{1,3}?", "01010101010")
print(m.group())

# greedy : 최대 일치 검색
liTag = "<li>나이키</li><li>아디다스</li><li>퓨마</li>"

m= re.search(r'<li>.*</li>',liTag)
print(m.group())

# non-greedy : 최소 일치 검색
liTag = "<li>나이키</li><li>아디다스</li><li>퓨마</li>"

m= re.search(r'<li>.*?</li>',liTag)
print(m.group())


# 그룹캡처를 변수처럼활용
mList = re.findall(r'((\w)(\w)\2)',"ABC 토마토 aba xyxy")
print(mList)

#그룹캡처 기능 쓰고싶지 않을때
m = re.search(r'((?:ab)+),((?:123)+) is repetive','ababab,123123123 is repetive')

print(m.group(0))
print(m.group(1))
print(m.group(2))


#스플릿 함수
sList = re.split(",",'14.5,12,18,19,20')
print(sList)

sList = re.split("\s+",'14.5  12 18    19       20')
print(sList)


subStr = re.sub(r"\d{6}","******","845644-846486")
print(subStr)

subStr = re.sub(r"(\d{6})-\d{6}","\g<1>-******","845644-846486")
print(subStr)

subStr = re.sub(r"(\d{3}-\d{3,4}-\d{4}),(\w+)","이름:\g<2>, 전화번호 : \g<1>","010-1234-3989,임꺽정")
print(subStr)
# subStr = re.sub(r"\d+",lambda x:str(int(x.group())*10),"1 2 apple 3")
# print(subStr)



# #(1) cat을 포함하는 글자는 가져오지만,
# #cat 혹은 cat(.+), (.+)cat 가져오지 않도록 하시오
# #scatter 0, scat x , cat x , copycat x
# text = "cat catch copycat scatter"

# m = re.search(r'\b(\w+cat\w+)\b',text)
# print(m.group())



# #(2) txt, pdf, hwp, xls 파일의 확장자만 검색할수 있도록 정규표현식 완성하기[txt,pdf,hwp,xls]
# #abc.txt , python.ppt(x), java.xls(0), .hwp(x)
# fileText = "abc.txt dk_e.PDF apple.ppt asdf adsf .xls"

# m = re.findall(r'\w+\.(?i:txt|pdf|hwp|xls)',fileText)
# print(m)











