import json
with open("C://Users//sandhya.c//Documents//words.json","r",encoding="utf-8") as word:
    json_data=word.read()
data=json.loads(json_data)#-->[{}{}{}]#string to json
#print(data)
data_dict={}
#count =0
for item in data:#[{word,meanings}{word}{word}]#home:{noun:[]},item["word"]=key,val=item[meannings]for val in meanings:
    #val[]
    value={}
    #data_dict.update(item)
    #print(item)
    #print("\n\n\n\n")
    #count=count+1
    key=item["word"]
   # print(key)
    temp=item["meanings"]
    
    for i in temp:
        lis=[]
        key2=i["partOfSpeech"]
        deff=i["definitions"]
        for d in deff:
            lis.append(d["definition"])
        value[key2]=lis
        print(value)
    data_dict[key]=value
print(data_dict)
with open("C://Users//sandhya.c//Documents//word_details.json","w") as details:
    details.write(json.dumps(data_dict, indent=2))
    



#print(count)

'''print(data_dict)
with open("C://Users//sandhya.c//Documents//con.json","w") as con:
    con.write("hello")
print(con)'''

