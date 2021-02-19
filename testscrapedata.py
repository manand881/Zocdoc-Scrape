from selenium import webdriver
import time
import os
from os import path

def ScrapeInfo(DoctorProfileURL):
    driver = webdriver.Chrome()
    driver.get(DoctorProfileURL)
    try:
        Name=driver.find_element_by_xpath("/html/body/div/div/main/div/div/section/div/div/h1/span").text
    except:
        Name="NaN"
    
    try:
        NPINumber=driver.find_element_by_xpath("(/html/body/div/div/main/div/div/div/section/section/p)[2]").text
    except:
        NPINumber="Nan"
    
    try:
        Gender=driver.find_element_by_xpath("/html/body/div/div/main/div/div/div/section/section/p").text
    except:
        Gender="Nan"
    
    try:
        Specialities=driver.find_element_by_xpath("/html/body/div/div/main/div/div/div/section/section/ul").text
    except:
        Specialities="Nan"
    
    try:
        PracticeName=driver.find_element_by_xpath("(/html/body/div/div/main/div/div/div/section/section/ul)[2]").text
    except:
        PracticeName="Nan"
    
    try:    
        Hospital_affiliations=driver.find_element_by_xpath("(/html/body/div/div/main/div/div/div/section/section/ul)[3]").text
    except:
        Hospital_affiliations="Nan"
    
    try:    
        BoardCertifications=driver.find_element_by_xpath("(/html/body/div/div/main/div/div/div/section/section/ul)[4]").text
    except:
       BoardCertifications="Nan"
    
    try:
        EducationTraining=driver.find_element_by_xpath("(/html/body/div/div/main/div/div/div/section/section/ul)[5]").text
    except:
        EducationTraining="Nan"
    
    try:
        AwardsPublications=driver.find_element_by_xpath("(/html/body/div/div/main/div/div/div/section/section/ul)[6]").text
    except:
        AwardsPublications="Nan"
        
    try:
        Languages=driver.find_element_by_xpath("(/html/body/div/div/main/div/div/div/section/section/ul)[7]").text
    except:
        Languages="Nan"

    try:
        Location=driver.find_element_by_xpath("/html/body/div/div/main/div/div/div/section/section/div/div/div/div/div/div/div/span").text
    except:
        Location="Nan"

    try:
        Location=Location+driver.find_element_by_xpath("(/html/body/div/div/main/div/div/div/section/section/div/div/div/div/div/div/div/span)[2]").text
    except:
        pass

    try:
        Location=Location+driver.find_element_by_xpath("(/html/body/div/div/main/div/div/div/section/section/div/div/div/div/div/div/div/span)[3]").text
    except:
        pass

    try:
        About=driver.find_element_by_xpath("/html/body/div/div/main/div/div/div/section/section").text
    except:
        Location="Nan"

    driver.close()

    return Name,NPINumber,Gender,Specialities,PracticeName,Hospital_affiliations,BoardCertifications,EducationTraining,AwardsPublications,Languages,Location,About


def WriteScrapedInfoToCSV(DoctorProfileURL):
    f=open("ProfileData.csv","a+")
    Entry=(ScrapeInfo(DoctorProfileURL))
    for x in range(len(Entry)):
        if "\n" in Entry[x]:
            x=Entry[x].replace("\n",",")
            f.writelines('"'+x+'",')
        else:
            f.writelines('"'+Entry[x]+'",')
    f.writelines("\n") 
    f.close()
    time.sleep(1)

f=open("DoctorProfiles.txt","r")
lines=f.readlines()
for x in lines:
    WriteScrapedInfoToCSV(x)