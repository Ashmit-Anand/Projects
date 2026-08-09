def main():
    a=int(input('Enter the length of autobiographical number:'))
    b=a-4
    lis=[]
    if a==4:
        print(1210,2020)

    elif a==5:
        print(21200)

    elif a==7 or a==8 or a==9 or a==10:
        for i in range (a):
            lis.append(0)

        lis[0]=b
        lis[1]=2
        lis[2]=1
        lis[b]=1

    else:
        print('This autobiographical number does not exist.')

    for e in lis:
        print(e,end="")
main()



