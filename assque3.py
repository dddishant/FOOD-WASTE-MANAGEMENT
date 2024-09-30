list1=[]
listsize=int(input("enter the length of list: "))
j=1
for i in range(listsize):
    item=input(f"enter element {j} in list: ")
    list1.append(item)
    j+=1
print(list1)
if len(list1)>0:
    if(len(list1)>=6):
        list1.pop(0)
        list1.pop(3)
        list1.pop(3)
        
        
    elif(len(list1)==5):
        list1.pop(0)
        list1.pop(3)
    elif(len(list1)<5):
        list1.pop(0)
    print(list1)

else:
    print("list is empty.")
