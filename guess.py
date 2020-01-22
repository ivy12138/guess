import random
r=random.randint(1,100)
count=0
while True:
    count=count+1
    num=int(input('enter a number:'))
    if num==r:
        print('Bingo')
        break
    elif num>r:
        print('larger')
    elif num<r:
        print('smaller')
    print('this is your',count,'guess')
