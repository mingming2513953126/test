import re
words = ['gold',' Google','Sogu','Guess']

part = re.compile(r'.*g[^u]')#‘.’匹配任意一个字符，'*'匹配0个或多个字符，g后面不是u

for w in words:
    m = re.match(part,w)
    if m:
        print(w)
print ('a')
print("b")
print("c")
