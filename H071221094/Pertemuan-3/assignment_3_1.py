

x=int(input(''))
y=int(input(''))


# for a in range(y):
#     if (a+1)%x==0:
#         print(a+1 )
#     else:
#         print(a+1,end=' ')
a=0
while (a<y):
    if (a+1)%x==0:
        print(a+1)
    else:
        print(a+1, end=' ')
    a=a+1