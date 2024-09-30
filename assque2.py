listlen=int(input(" Enter the Size of the list: "))
itemlst=[]
j=1
for i in range(listlen):
    
    item=input(f"enter element {j} in the list: ")
    itemlst.append(item)
    x=(list(set(itemlst)))
    j+=1
print("after remooving duplicate , the list is " ,x)
