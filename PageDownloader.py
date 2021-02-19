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

def DownloadHTMLPage(WorkingURL,FileName):
    HTMLFileName=FileName+".html"
    if(path.exists(HTMLFileName)):
        print(HTMLFileName,"Already Exists")
    else:
        driver = webdriver.Chrome()
        print("Opening Page",WorkingURL)
        driver.get(WorkingURL)
        f=open(HTMLFileName,'w+')
        f.writelines(driver.page_source)
        driver.quit()
        f.close()
        writedocprofiletotxt(HTMLFileName,BaseURL[:-1])
        removeduplicates()
        time.sleep(2)

BaseURL="https://www.zocdoc.com/"
CategorySuffix="primary-care-doctors/"
WorkingURL=BaseURL+CategorySuffix

CreateCSV()

for PageNo in range(1,11):
    DownloadHTMLPage(WorkingURL+str(PageNo),str(PageNo))

zips=open("Zipcodes.txt","r")
AreaList=zips.readlines()
for AreaCode in AreaList:
    CategorySuffix="search?dr_specialty=153&address="
    WorkingURL=BaseURL+CategorySuffix
    DownloadHTMLPage(WorkingURL+AreaCode[:-1],AreaCode[:-1])

print("Finished Downloading HTML Pages")