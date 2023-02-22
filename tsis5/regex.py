import re
# divides to patterm
# pattern- rule of search
# text - where we gonna search
# pattern ='[a-b]'
# text= 'abba'
# m= re.search(pattern, text)
# print(m)
#
# 6 replace dot, comma, space => colon
t6='Almaz toktasin.kbtu,kz'
r6= re.sub(r'[ ,.]',  ':', t6)
print(r6)
# 8 split by uppercase
t8='AlmazToktasinPp2malwaRehubShit'
r8= re.split(r'[A-Z]', t8)
print(r8)
# 9 insert space before cap letter
t9='AlmazToktasinKBTUsHit'
r9=re

