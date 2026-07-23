import csv
data = [
    ['Name', 'Age', 'City'],  # Headers
    ['Anna', '28', 'Moscow'],
    ['Ivan', '35', 'Saint Petersburg'],
    ['Maria', '22', 'Kazan']
]

def main():
    try:
        with open("person.csv" , newline="" ,mode="w") as f:
            writer = csv.writer(f , delimiter=";")
            writer.writerows(data)
    except Exception as e:
        print("The Error is: " , e)    
    
    
    try:
        with open("person.csv" , mode="r") as f:
            reader = csv.reader(f)
    
            headers = next(reader)
            print(f"Headers : {headers}")
            for row in reader:
                print(f"{row[0]}")
    
    except Exception as e:
        print("The Error is: " , e)    


if __name__ == "__main__":
    main()