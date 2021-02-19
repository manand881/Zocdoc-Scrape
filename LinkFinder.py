import os

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
