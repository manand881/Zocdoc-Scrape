import zipcodes
import os

ziplist=list()
f=open("USZipCodes","w+") 
f.writelines("hello")

def NumberGenerator():
    for ZipCode in range(1500):
        yield str(ZipCode).zfill(5)
        ZipCode += 1

for x in NumberGenerator():
    if(zipcodes.is_real(x)):
        ziplist.append(x)
        f.writelines(x)
        print("'"+x+"'")

print("Ziplist Length",len(ziplist))
