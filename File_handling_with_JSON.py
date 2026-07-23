import json
person = {
    "name": "Anna",
    "age": 28,
    "city": "Moscow",
    "languages": ["Python", "JavaScript"]
}

def main():
    json_string = json.dumps(person,ensure_ascii=False,indent=2)
    print(json_string)

    data = json.loads(json_string)
    print(data , type(data))

    # Writing JSON to File
    try:
        with open("person.json" , "w") as f:
            json.dump(person , f , ensure_ascii=False , indent=2)
    except Exception as e:
        print("The Error is: " , e)   
    
         
    # Reading JSON from File
    try:
        with open("person.json" , "r") as f:
            print(json.load(f))
    except Exception as e:
        print("The Error is: " , e) 

if __name__ == "__main__" :
    main()       
               
    
    
