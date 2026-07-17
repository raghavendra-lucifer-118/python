import json
person = {
    "name": "Anna",
    "age": 28,
    "city": "Moscow",
    "languages": ["Python", "JavaScript"]
}

json_string = json.dumps(person,ensure_ascii=False,indent=2)
print(json_string)

data = json.loads(json_string)
print(data , type(data))

with open("person.json" , "w") as f:
    json.dump(person , f , ensure_ascii=False , indent=2)
    
with open("person.json" , "r") as f:
     print(json.load(f))