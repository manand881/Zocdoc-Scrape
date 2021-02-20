import zipcodes
import os

ziplist=list()
FileName=open("Zipcodes.txt","w+") 

for ZipCode in range(99999):
    ZipCode=str(ZipCode).zfill(5)
    if(zipcodes.is_real(ZipCode)):
        ziplist.append(ZipCode)
        FileName.writelines(ZipCode+"\n")
        print("'"+ZipCode+"'")

print("Ziplist Length",len(ziplist))
FileName.close()