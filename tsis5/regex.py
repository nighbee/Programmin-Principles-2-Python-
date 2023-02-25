import re
# divides to patterm
# pattern- rule of search
# text - where we gonna search
# pattern ='[a-b]'
# text= 'abba'
# m= re.search(pattern, text)
# print(m)

#1 match string that has 'a' followeb by 0 or more 'b'
t1='abbb'
pattern1=r'a[b]*'
r1=re.match(pattern1,t1)
print(r1)
#2 match 'a' followed by 2/3 'b'
pattern2=r'a[b]{2,3}'
t2='abbb'
r2=re.match(pattern2,t2)
print(r2)
#3 matches in string underscore
pattern3= r'[a-z]+_[a-z]+'
t3='this_is_a_test_string'
r3=re.match(pattern3, t3)
print(r3)
#4 one uppercase followed by lower case
pattern4=r'[A-Z][a-z]+'
t4='Almaz Toktassin kbtu sHit PP2'
r4=re.findall(pattern4,t4)
print(r4)
#5 has 'a' followed by anything ending with 'b'
pattern5=r'a.*b$'
t5='ashitb'
r5=re.match(pattern5,t5)
print(r5)
# 6 replace dot, comma, space => colon
t6='Almaz toktasin.kbtu,kz'
r6= re.sub(r'[ ,.]',  ':', t6)
print(r6)
# 8 split by uppercase
t8='AlmazToktasinPp2malwaRehubShit'
r8= re.split(r'[A-Z]', t8)
print(r8)
# 9 insert space before cap letter
t9='AlmazToktasinKbtusHit'
r9=re.sub(r"(\w)([A-Z])", r"\1 \2", t9)
print(r9)
#10 to convert camel string to snake case
def camelToSnake(t10):
    words=re.findall(r'[A-Za-z][a-z]*',t10)
    return '_'.join(words).lower()
pattern10= r'[A-Za-z][a-z]*'
t10='CamelStringToSnakeCase'
snake_case=camelToSnake(t10)
print(snake_case)
# r10=re.findall(pattern10,t10)
# print(r10)

