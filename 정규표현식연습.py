import re

with open('ROBOT.CON','r',encoding='utf8') as f:
    fileText = f.read()

section = 'Condition set'
taget = 'Playback mode'

p = re.compile(r'#\d+\s*' + section + r'\n([\w\W]+?)(?:$|#)')##?의 의미
m = p.search(fileText)
print(m.group(0))