fh = open( input("Enter the file name :-")+".txt",'r')
text = fh.readlines()
for i in text:
    for j in (i):
        print (j.upper(),end=" and ")
fh.close()
