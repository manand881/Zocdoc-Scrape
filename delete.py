f=open("URLsVisited.txt","r+")
VisitedURLList=f.readlines()
print(len(VisitedURLList))
VisitedURLList=list(dict.fromkeys(VisitedURLList))
print(len(VisitedURLList))
f.close()
f=open("URLsVisited.txt","w+")
for x in VisitedURLList:
    f.writelines(x)

f.close()