import json

with open("data.json", "r") as read_file:
    data=json.load(read_file)
print(data)
print("""Interface status
================================================================================""")
print("""DN                                             Description          Speed                      MTU """)
# for i, k in data["imdata"][0]['l1PhysIf']["attributes"].items():
#     if i=='dn':
#         print(k,end="                          ")
#     if i=='speed':
#         print(k,end="                                         ")
#     if i=='mtu':
#         print(k, end="                   ")

# for k in data["imdata"][i]['l1PhysIf']:
#         for j in data["imdata"][i]['l1PhysIf']["attributes"].items():
#             if k=='dn':
#                 print(j, end="                          ")
#             if k== 'speed':
#                 print(j, end="                                         ")
#             if k == 'mtu':
#                 print(j, end="                   ")
lenght=0
for i, k in data["imdata"][lenght]['l1PhysIf']["attributes"].items:
    if i == 'dn':
                print(k, end="                          ")
    if i== 'speed':
                print(k, end="                                         ")
    if i == 'mtu':
                print(k, end="                   ")
    lenght+=1