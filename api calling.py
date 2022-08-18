


from os import link
import requests
import json
link=requests.get("https://api.merakilearn.org/courses")
res=link.json()
with open ("data.json","w")as file:
    json.dump(res,file,indent=2)
r=open("data.json","r")
read=r.read()
Data=json.loads(read)
print()    
i=0
while i<len(Data):
    print(i+1,".",Data[i]["name"],"-/",Data[i]["id"])
    i+=1
snumber=int(input("Enter the topic number: "))
print(Data[snumber-1]["name"]+Data[snumber-1]["id"])
print()
pr=Data[snumber-1]["name"]+Data[snumber-1]["id"]+".json"
link2="https://api.merakilearn.org/courses/"+Data[snumber-1]["id"]+"/exercises"
print(link2)
ur=requests.get(link2)
d=ur.json()
with open ("data2.json","w")as n:
    json.dump(d,n,indent=4)    
r1=open("data2.json","r")
read1=r1.read()
Data2=json.loads(read1)
# print(Data2)
# print(Data2["course"]["exercises"])
i=0
# for i in Data2["course"]["exercises"]:
#     print(i)
while i<len(Data2["course"]["exercises"]):
    print(str(i+1),".",Data2["course"]["exercises"][i]["name"])
    i+=1
topic=int(input("Enter the sub topic number: "))
topic-=1
i=0
while i <len(Data2["course"]["exercises"][topic]["content"]):
    print(str(i+1),Data2["course"]["exercises"][topic]["content"])
    print(str(i+1))
    i+=1
while topic <=len(Data2["course"]["exercises"]):
    navigation=input("PREVIOUS OR NEXT (n&p): ")
    if navigation=="p" and navigation!="n":
        topic-=1
        if navigation=="p" and topic>1:
            print(Data2["course"]["exercises"][topic]["name"],"\n")
            i=0
            while i<len(Data2["course"]["exercises"][topic]["content"]):
                print(str(i+1),Data2["course"]["exercises"][topic]["content"][i]["value"])
                i+=1
        else:
            i=0
            while i<len(Data2):
                print(str(i+1),Data2["course"]["exercises"][i]["name"])        
                i+=1
    elif navigation=="n" and topic!="p":  
        topic+=1
        if navigation=="n" and topic<len(Data2["course"]["exercises"]):
            print(Data2["course"]["exercises"][topic]["name"],"\n")
            i=0
            while i<len(Data2["course"]["exercises"][topic]["content"]):
                print(str(i+1),Data2["course"]["exercises"][topic]["content"][i]["value"])
                i+=1
        if topic+1==len(Data2["course"]["exercises"]):
            print("TOPIC IS COMPLEATE")
            break
    else:
        print("Wrong User input......")          
