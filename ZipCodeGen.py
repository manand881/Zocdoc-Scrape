f=open("Zipcodes.txt","w+")
Zipcodes=list()
for x in range(35801,35816+1):
    Zipcodes.append(x)
for x in range(99501,99524+1):
    Zipcodes.append(x)
for x in range(85001,85055+1):
    Zipcodes.append(x)
for x in range(72201,72217+1):
    Zipcodes.append(x)
for x in range(94203,94209+1):
    Zipcodes.append(x)
for x in range(90001,90089+1):
    Zipcodes.append(x)
for x in range(90209,90213+1):
    Zipcodes.append(x)
for x in range(80201,80239+1):
    Zipcodes.append(x)
for x in range(6101,6112+1):
    x=str(0)+str(x)
    Zipcodes.append(x)
for x in range(19901,19905+1):
    Zipcodes.append(x)
for x in range(20001,20020+1):
    Zipcodes.append(x)
for x in range(32501,32509+1):
    Zipcodes.append(x)
for x in range(33124,33190+1):
    Zipcodes.append(x)
for x in range(32801,32837+1):
    Zipcodes.append(x)

for ZipCode in Zipcodes:
    f.writelines(str(ZipCode)+"\n")
