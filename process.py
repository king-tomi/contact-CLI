import sqlite3
import sys
from contact import Contact

database = sqlite3.connect("contact.db")
cursor = database.cursor()



def save_contact(name: str,number: int):
    cursor.execute(f"""INSERT INTO Contacts
                       VALUES ({name}, {number});""")


def delete_contact(name: str):
    contact = cursor.execute(f"""SELECT name, number
                      FROM Contacts where name = {name}""")
    if contact:
        cursor.execute(f"""DELETE FROM Contacts 
                      WHERE name = {name};""")
    else:
        return "contact not found", None

def view_contact(name: str) -> str:
    contact = cursor.execute(f"""SELECT name, number
                      FROM Contacts where name = {name}""")
    if contact:
        return str(contact)
    return "contact not found", None


def process():
    print("HELLO THERE!")
    inputs = sys.argv[1]
    if inputs is None:
        raise Exception("No arguments provided. What is the name of your contact book?")
    print("What do you wish to do? save a new contact(enter s)? delete a contact(enter d)? view contact list(enter v)?")
    answer = input(">>>")
    if answer == "s":
        name = input("enter conctact's name: ")
        number = input("enter contact's number: ")
        save_contact(name,number)
        print("Contact saved successfully")
    elif answer == "d":
        name = input("Enter the name of the contact you wish to delete: ")
        delete_contact(name)
    elif answer == "v":
        print(view_contact(name))



 

if __name__ == "__main__":
    save_contact("name",754)