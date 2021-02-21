from selenium import webdriver
from os import path
import os
import re
import requests
import time
import threading
import random

def CreateCSV():
    if(path.exists("ProfileData.csv")):
        print("ProfileData csv already exists")
    else:
        print("ProfileData csv created")
        f=open("ProfileData.csv","w+")
        f.writelines("Name,NPINumber,Gender,Specialities,Practice Name,Hospital affiliations,BoardCertifications,Education Training,Awards Publications,Languages,Location,About\n")
        f.close()

def CheckIfPageVisited(WorkingURL):
    f=open("URLsVisited.txt","r+")
    VisitedURLList=f.readlines()
    for x in VisitedURLList:
        if WorkingURL in x:
            return True

def DownloadHTMLPage(WorkingURL,FileName,driverno):
    driver=driverno
    g=open("URLsVisited.txt","a+")
    HTMLFileName=FileName+".html"
    if(CheckIfPageVisited(WorkingURL)):
        print(WorkingURL,"Already Visited")
    else:
        print("Opening Page",WorkingURL)
        try:
            driver.get(WorkingURL)
        except:
            g.close()
            time.sleep(10)
            DownloadHTMLPage(WorkingURL,FileName,driverno)
        f=open(HTMLFileName,'w+')
        f.writelines(driver.page_source)
        f.close()
        writedocprofiletotxt(HTMLFileName,BaseURL[:-1]) 
        g.writelines(WorkingURL+"\n")
        g.close()
        

def writedocprofiletotxt(HTMLFileName,BaseURL):
    f=open(HTMLFileName,"r")
    LineElements=list()
    Elements=list()
    HTMLFile=f.readlines()
    for Line in HTMLFile:
        LineElements=Line.split(" ")
        for SplitElement in LineElements:
            Elements.append(SplitElement)
    Elements=list(dict.fromkeys(Elements))
    f.close()
    g=open("DoctorProfiles.txt","a+")
    for Members in Elements:
        if 'href="/doctor/' in Members:
            Members=Members.split('"')
            Members=str(Members[1])
            if "?" in Members:
                Members=Members.split("?")
                Members=str(Members[0])
            g.writelines(BaseURL+Members+"\n")

    g.close()
    os.remove(HTMLFileName)

def removeduplicates():
    f=open("DoctorProfiles.txt","r")
    lines=f.readlines()
    print("No of Entries Before Removing Duplicates",len(lines))
    lines=list(dict.fromkeys(lines))
    print("No of Entries After Removing Duplicates",len(lines))
    f.close()
    f=open("DoctorProfiles.txt","w")
    f.writelines(lines)
    f.close()

BaseURL="https://www.zocdoc.com/"
CategorySuffix="search?dr_specialty=153&address="
WorkingURL=BaseURL+CategorySuffix

CreateCSV()
driver1 = webdriver.Chrome()
driver2 = webdriver.Chrome()
driver3 = webdriver.Chrome()
driver4 = webdriver.Chrome()
driver5 = webdriver.Chrome()

zips=open("Zipcodes.txt","r")
AreaList=zips.readlines()
print(AreaList)
print(len(AreaList))
def threadripper(driverno):
    AreaCode1=random.choice(AreaList)
    DownloadHTMLPage(WorkingURL+AreaCode1[:-1],AreaCode1[:-1],driverno)
    AreaList.remove(AreaCode1)
    print(len(AreaList))
    if(len(AreaList)>0):
        threadripper(driverno)

t1=threading.Thread(target=threadripper,args=(driver1,))
t2=threading.Thread(target=threadripper,args=(driver2))
t3=threading.Thread(target=threadripper,args=(driver3))
t4=threading.Thread(target=threadripper,args=(driver4))
t5=threading.Thread(target=threadripper,args=(driver5))
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t1.join()
t2.join()
t3.join()
t4.join()
t5.join()

removeduplicates()

print("Finished Downloading HTML Pages")