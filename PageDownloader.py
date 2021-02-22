from selenium import webdriver
from os import path
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

def check_if_page_visited(WorkingURL):
    f=open("URLsVisited.txt","r+")
    VisitedURLList=f.readlines()
    for x in VisitedURLList:
        if WorkingURL in x:
            return True

def DownloadHTMLPage(WorkingURL,FileName,driverno):
    driver=driverno
    g=open("URLsVisited.txt","a+")
    HTMLFileName=FileName+".html"
    if(check_if_page_visited(WorkingURL)):
        sys.stdout.write("\nAlready Visited "+WorkingURL)
    else:
        sys.stdout.write("\nOpening Page "+WorkingURL)
        try:
            driver.get(WorkingURL)
        except:
            g.close()
            time.sleep(10)
            DownloadHTMLPage(WorkingURL,FileName,driverno)
        f=open(HTMLFileName,'w+')
        f.writelines(driver.page_source)
        f.close()
        write_docprofile_to_txt(HTMLFileName,BaseURL[:-1]) 
        g.writelines(WorkingURL+"\n")
        g.close()
        
def write_docprofile_to_txt(HTMLFileName,BaseURL):
    f=open(HTMLFileName,"r")
    Elements=list()
    HTMLFile=f.readlines()
    for Line in HTMLFile:
        LineElements=Line.split(" ")
        for SplitElement in LineElements:
            Elements.append(SplitElement)
    Elements=list(dict.fromkeys(Elements))
    f.close()
    for Members in Elements:
        if 'href="/doctor/' in Members:
            Members=Members.split('"')
            Members=str(Members[1])
            if "?" in Members:
                Members=Members.split("?")
                Members=str(Members[0])
            BufferList.append(BaseURL+Members)

    os.remove(HTMLFileName)

def remove_duplicates():
    f=open("DoctorProfiles.txt","r")
    lines=f.readlines()
    sys.stdout.write("\nNo of Entries Before Removing Duplicates "+str(len(lines)))
    lines=list(dict.fromkeys(lines))
    sys.stdout.write("\nNo of Entries After Removing Duplicates "+str(len(lines)))
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
    members_buffer()

BufferList=list()
BaseURL="https://www.zocdoc.com/"
CategorySuffix="search?dr_specialty=153&address="
WorkingURL=BaseURL+CategorySuffix

create_csv()
driver1 = webdriver.Chrome()
driver2 = webdriver.Chrome()
driver3 = webdriver.Chrome()
driver4 = webdriver.Chrome()
driver5 = webdriver.Chrome()

remove_duplicates()

zips=open("Zipcodes.txt","r")
AreaList=zips.readlines()

def threadripper(driverno):
    AreaCode1=random.choice(AreaList)
    DownloadHTMLPage(WorkingURL+AreaCode1[:-1],AreaCode1[:-1],driverno)
    AreaList.remove(AreaCode1)
    try:
        threadripper(driverno)
    except Exception as e:
        if(len(AreaList)==0):
            return None
        sys.stdout.write("\nError Occured "+e)
        time.sleep(10)
        threadripper(driverno)

t1=threading.Thread(target=threadripper,args=(driver1,))
t2=threading.Thread(target=threadripper,args=(driver2,))
t3=threading.Thread(target=threadripper,args=(driver3,))
t4=threading.Thread(target=threadripper,args=(driver4,))
t5=threading.Thread(target=threadripper,args=(driver5,))
t6=threading.Thread(target=members_buffer)
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