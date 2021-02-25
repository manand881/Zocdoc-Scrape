from selenium import webdriver
from os import path
import numpy as np
import os
import re
import time
import threading
import random
import sys

def create_csv():
    if(path.exists("ProfileData.csv")):
        print("ProfileData csv already exists")
    else:
        print("ProfileData csv created")
        f=open("ProfileData.csv","w+")
        f.writelines("Name,NPINumber,Gender,Specialities,Practice Name,Hospital affiliations,BoardCertifications,Education Training,Awards Publications,Languages,Location,About\n")
        f.close()

def DownloadHTMLPage(WorkingURL,driverno):
    driver=driverno
    g=open("URLsVisited.txt","a+")
    sys.stdout.write("\nOpening Page    "+WorkingURL)
    try:
        driver.get(WorkingURL)
    except:
        time.sleep(10)
        DownloadHTMLPage(WorkingURL,driverno)
    write_docprofile_to_txt(BaseURL[:-1],driver.page_source) 
    g.writelines(WorkingURL+"\n")
    g.close()       
        
def write_docprofile_to_txt(BaseURL,page_source):
    Elements=list()
    HTMLFile=page_source.split("\n")
    for Line in HTMLFile:
        LineElements=Line.split(" ")
        for SplitElement in LineElements:
            Elements.append(SplitElement)
    Elements=list(dict.fromkeys(Elements))
    for Members in Elements:
        if 'href="/doctor/' in Members:
            Members=Members.split('"')
            Members=str(Members[1])
            if "?" in Members:
                Members=Members.split("?")
                Members=str(Members[0])
            BufferList.append(BaseURL+Members)

def remove_duplicates():
    f=open("DoctorProfiles.txt","r")
    lines=f.readlines()
    sys.stdout.write("\nNo of Entries Before Removing Duplicates "+str(len(lines)))
    lines=list(dict.fromkeys(lines))
    lines.sort()
    sys.stdout.write("\nNo of Entries After  Removing Duplicates "+str(len(lines)))
    f.close()
    f=open("DoctorProfiles.txt","w")
    f.writelines(lines)
    f.close()

def members_buffer():
    g=open("DoctorProfiles.txt","a+")
    for x in BufferList:
        g.writelines(x+"\n")
        BufferList.remove(x)
    g.close()
    time.sleep(60)
    remove_duplicates()
    if t1.is_alive() or t2.is_alive() or t3.is_alive() or t4.is_alive() or t5.is_alive():
        members_buffer()

BufferList=list()
BaseURL="https://www.zocdoc.com/"
CategorySuffix="search?dr_specialty=153&address="
WorkingURL=BaseURL+CategorySuffix

create_csv()

zips=open("Zipcodes.txt","r")
AreaList=zips.read()
AreaList=AreaList.split("\n")

def remove_visited_before_start(AreaList):
    f=open("URLsVisited.txt","r+")
    VisitedURLList=f.read()
    VisitedURLList=VisitedURLList.split("\n")
    VisitedZipList=list()
    TempList=list()
    print("Total number of searchable zipcodes in the US:",len(AreaList))
    print("Total number of URLs Already Visited:         ",len(VisitedURLList))
    for x in (VisitedURLList):
        VisitedZipList.append(x[-5:])
    VisitedZipList.sort()
    TempList=np.setdiff1d(AreaList, VisitedZipList)
    AreaList.clear()
    AreaList=TempList
    print("Total number of remaining zipcodes to search: ",len(AreaList))
    return AreaList

AreaList=list(remove_visited_before_start(AreaList))

def threadripper(driverno,stackoverflow):
    if stackoverflow<800:
        stackoverflow+=1
        AreaCode1=random.choice(AreaList)
        DownloadHTMLPage(WorkingURL+AreaCode1,driverno)
        AreaList.remove(AreaCode1)
        try:
            threadripper(driverno,stackoverflow)
        except Exception as e:
            if(len(AreaList)==0):
                return None
            sys.stdout.write("\nError Occured "+str(e))

os.system('taskkill /IM "chromedriver.exe" /F')
os.system('taskkill /IM "chrome.exe" /F')
driver1 = webdriver.Chrome()
driver2 = webdriver.Chrome()
driver3 = webdriver.Chrome()
driver4 = webdriver.Chrome()
driver5 = webdriver.Chrome()

stackoverflow=0
t1=threading.Thread(target=threadripper,args=(driver1,stackoverflow,))
t2=threading.Thread(target=threadripper,args=(driver2,stackoverflow,))
t3=threading.Thread(target=threadripper,args=(driver3,stackoverflow,))
t4=threading.Thread(target=threadripper,args=(driver4,stackoverflow,))
t5=threading.Thread(target=threadripper,args=(driver5,stackoverflow,))
t6=threading.Thread(target=members_buffer)

for stack in range(99):
    stackoverflow=0
    try:
        t1.join()
        t2.join()
        t3.join()
        t4.join()
        t5.join()
        t6.join()
    except:
        pass
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    t6.join()

print("Finished Downloading HTML Pages")