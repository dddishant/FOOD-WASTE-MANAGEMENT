strct=0
nostr=int(input("enter the number of Strings: "))
for i in range(nostr):

    sstr=input("enter the string: ")
    if (len(sstr)>=2) and (sstr[0]==sstr[-1]):
        strct+=1
print("no. of strings whose first and last letter are same is " ,strct)
