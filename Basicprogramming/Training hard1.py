'''
count =0
while count<=2:
    guess=int(input("guess"))
    if guess==5:
        print("congratulations!")
        break
    else: count =count + 1

'''

count=0
flag=0
while count <= 2:
    guess = int(input("guess"))
    if guess == 5:
        print("congratulations!")
        flag=1
        break
    else:
        count = count + 1
        if flag ==0 and count==3:
            say=input("want to play")
            if say=='y' or 'Y':
                count =0
            else:
                break


