def search(list,length,x):
    if x==list[int(length/2)]:
       print("The number is found")
       print("The number is atindex:"+str(list.index(x)))
    elif x>list[int(length/2)]:
        del list[0:length/2]
        search(list,length,x)
    elif x<list[int(length/2)]:
        del list[length:-1]
        search(list,length,x)

num=0
list=[0,20,40,60,80]
x=40
length=len(list)
search(list,length,x)