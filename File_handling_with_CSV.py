import csv
data = [
    ['Name', 'Age', 'City'],  # Headers
    ['Anna', '28', 'Moscow'],
    ['Ivan', '35', 'Saint Petersburg'],
    ['Maria', '22', 'Kazan']
]

with open("person.csv" , newline="" ,mode="w") as f:
    writer = csv.writer(f , delimiter=";")
    writer.writerows(data)
    
with open("person.csv" , mode="r") as f:
    reader = csv.reader(f)
    
    headers = next(reader)
    print(f"Headers : {headers}")
    for row in reader:
        print(f"{row[0]}")
