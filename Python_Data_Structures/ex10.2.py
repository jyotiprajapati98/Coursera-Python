"""
10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
"""

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

hcount = dict()                #empty dictionary
hlist = []                     # empty list                      

for line in handle:
    
    words = line.split()
    
    if len(words) > 2 and words[0] == 'From': 
        
        hr = words[5].split(':')   
        
        hcount[hr[0]] = hcount.get(hr[0], 0) + 1    
    else:
        continue

for k,v in hcount.items():                         
    hlist.append((k,v))                               

hlist.sort()                                         
for k,v in hlist:                                   
    print(k,v)  
