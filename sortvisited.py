import os

def sort_visited_urls():
    
    f=open("URLsVisited.txt","r")
    visited=f.readlines()
    print("Length of Visited URL List before sorting and deletion of duplicates",len(visited))
    visited=list(dict.fromkeys(visited))
    visited.sort()
    print("Length of Visited URL List after  sorting and deletion of duplicates",len(visited))
    f.close()
    f=open("URLsVisited.txt","w")
    for line in visited:
        f.writelines(line)
    
sort_visited_urls()
