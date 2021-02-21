from selenium import webdriver
from LinkFinder import writedocprofiletotxt,removeduplicates
from os import path
import os
import re
import requests
import time

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

def DownloadHTMLPage(WorkingURL,FileName):
    g=open("URLsVisited.txt","a+")
    HTMLFileName=FileName+".html"
    if(CheckIfPageVisited(WorkingURL)):
        print(WorkingURL,"Already Visited")
    else:
        try:
            pass
        except:
            g.close()
            time.sleep(10)
            DownloadHTMLPage(WorkingURL,FileName)
        print("Opening Page",WorkingURL)
        try:
            driver.get(WorkingURL)
        except:
            g.close()
            time.sleep(10)
            DownloadHTMLPage(WorkingURL,FileName)
        f=open(HTMLFileName,'w+')
        f.writelines(driver.page_source)
        f.close()
        writedocprofiletotxt(HTMLFileName,BaseURL[:-1])
        removeduplicates()
        g.writelines(WorkingURL+"\n")
        g.close()

BaseURL="https://www.zocdoc.com/"
CategorySuffix="primary-care-doctors/"
WorkingURL=BaseURL+CategorySuffix

CreateCSV()
driver = webdriver.Chrome()

for PageNo in range(1,11):
    DownloadHTMLPage(WorkingURL+str(PageNo),str(PageNo))

zips=open("Zipcodes.txt","r")
AreaList=zips.readlines()
for AreaCode in AreaList:
    print(AreaList.index(AreaCode),"Of",len(AreaList))
    CategorySuffix="search?dr_specialty=153&address="
    WorkingURL=BaseURL+CategorySuffix
    DownloadHTMLPage(WorkingURL+AreaCode[:-1],AreaCode[:-1])

print("Finished Downloading HTML Pages")