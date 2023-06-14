import json


def json_parsing():
    """
    json parsing: need to take parameter name, min value, max value avg_value from parameterlist dictionary
    """
    try:
        with open("C://Users//sandhya.c//Downloads//sample_data.json","r",encoding="utf-8") as f:
            data=json.load(f)
        data_dict=[]
        details=data["parametersList"]
        for parameterlist in details:
            dict_1={}
            dict_1['parametername']=parameterlist["parameterName"]
            dict_1['min_value']=parameterlist["min"]
            dict_1['max_value']=parameterlist["max"]
            dict_1['avg_value']=parameterlist["avg"]
            data_dict.append(dict_1)
        print(data_dict)
        with open("C://Users//sandhya.c//Documents//output.json","w") as details:
            details.write(json.dumps(data_dict, indent=2))
    except Exception as e:
        print("Failed to parse the data" + str(e))    
        


    
if __name__ == "__main__":
    json_parsing()