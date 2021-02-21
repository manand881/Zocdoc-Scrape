def CheckIfPageVisited(WorkingURL):
    f=open("URLsVisited.txt","r+")
    VisitedURLList=f.readlines()
    for x in VisitedURLList:
        if WorkingURL in x:
            return True

print(CheckIfPageVisited("https://www.zocdoc.com/search?dr_specialty=153&address=00544"))
print(CheckIfPageVisited("https://www.zocdoc.com/search?dr_specialty=153&address=00544"))
print(CheckIfPageVisited("https://www.zocdoc.com/search?dr_specialty=153&address=00544"))
print(CheckIfPageVisited("https://www.zocdoc.com/primary-care-doctors/10"))
