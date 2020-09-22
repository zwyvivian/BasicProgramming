'''
user=input("user")
matma=int(input("code"))
count=0
if user=="alex" and matma==123:
    print("sucess")
else:
    while count<3:
        user = input("user")
        matma = int(input("code"))
        if user == "alex" and matma == 123:
            print("sucess")
            break
        count +=1
'''
'''
count=1
while True:
    if count <6:
        count +=1
        print("*"*(count))
    else:
        count=count-1
        if count==5:
            continue
        print("*" * (count))

'''

good=[{"name":"computer",'price':4000},{"name":'mouse','price':200}]
for i,k in enumerate(good):
    print(i,k)