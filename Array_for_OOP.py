# Mimic IntegerList 

class IntegerList:
    def __init__(self , size):
        self.size = size
        self.list = []
          
          
    def __str__(self):
         return str(self.list)  
     
         
    def addElement(self , value):
        self.list.append(value)   
     
    def deleteElement(self , value):
        for ele in self.list:
            if ele == value:
                self.list.remove(value)   
     
    def sort(self):
        arr = self.list.copy()
        n = len(arr)
        for i in range(n):
          for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # swap
                arr[j], arr[j + 1] = arr[j + 1], arr[j] 
        return arr   
                 
     
    def reverse(self):
        arr = self.list.copy()
        n = len(arr) 
        for i in range(0 , n//2):
            # swap
            arr[i], arr[n - i - 1 ] = arr[n - i - 1 ], arr[i]
        return arr   
            
    def getSize(self):
        return self.size       
     
# Input the size of array     
n = int(input("Enter Size: "))

# Initalise Array of size n 
arr = IntegerList(n)

for i in range(n):
    ele = int(input("Value: "))
    arr.addElement(ele)
    

print(arr)    
print(arr.sort())    
print(arr.reverse())    
print(arr)    
print(arr.getSize())



     