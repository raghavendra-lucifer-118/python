# Setting contacts structure
Contacts = []

# Functions for each action
# Adding a contact
def addContact():
    name = input("Enter Name: ")
    phno = int(input("Enter Phone Number: "))
    email = input("Enter Email: ")
    
    contact = {"name" : name,
               "phno" : phno,
               "mail" : email}
    
    Contacts.append(contact)
    print("Contact Added Successfully")
    
# View single the contact details
def viewContact(c):
    print(f"Name : {c["name"]}\nPhone Number : {c["phno"]}\nEmail : {c["mail"]}\n")    


# To View all contacts:
def viewContacts():
    for c in Contacts:
        viewContact(c)


# Search a single contact
def searchContact():
    searchcname = input("Enter Name: ")
    for c in Contacts:
        if (searchcname == c["name"]):
            print(f"Name : {c["name"]}\nPhone Number : {c["phno"]}\nEmail : {c["mail"]}\n")    


# Updating the contact
def updateContact():
    searchcname = input("Enter Name: ")
    updatecnumber = int(input("Enter New Phone Number: "))
    for c in Contacts:
        if (searchcname == c["name"]):
            c["phno"] = updatecnumber   


# Deleting the contact
def deleteContact():
    searchcname = input("Enter Name: ")
    for c in Contacts:
        if (searchcname == c["name"]):
            Contacts.remove(c)  
    print("Contact Added Successfully")
         
            
            

# Sort all contacts
def sortContacts():
    sorted_contact = sorted(Contacts , key=lambda c:c["name"].lower())
    for c in sorted_contact:
        viewContact(c)


       
# Menu for options
print("""1.Add Contact
2.View Contacts
3.Search Contact
4.Update Contact
5.Delete Contact
6.Sort Contact
7.exit""")       
            
while(True):
    choice = int(input("Enter Choice: "))
    match(choice):
        case 1 : addContact()
        case 2 : viewContacts()
        case 3 : searchContact()
        case 4 : updateContact()
        case 5 : deleteContact()
        case 6 : sortContacts()
        case 7 : exit()
        case c : print("choose the right choice:")
        
        
