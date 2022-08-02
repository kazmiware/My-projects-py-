import csv

class record:
    def __init__(self,name,phone,e_mail,add):
        self.name=name
        self.phone=phone
        self.e_mail=e_mail
        self.add=add

        # to create a file
    def create_file():
        header=["name","Phone number","e-mail","address"]
        with open("contact book.csv",'w') as f:
          writer=csv.writer(f)
          writer.writerow(header)

    def read(self):
        name=[]
        email=[]
        add=[]
        phone=[]
        with open("contact book.csv",'r') as f:
            reader=csv.DictReader(f)
            for i in reader:
                name.append(i['name'])
                email.append(i['e-mail'])
                phone.append(i['Phone number'])
                add.append(i['address'])
        return name,phone,email,add

    # to create a contact
    def create_contact():
        name=input("Enter name of contact:")
        phone = input("Enter phone number of contact:")
        email = input("Enter email of contact:")
        add = input("Enter address of contact:")
        contact=record(name,phone,email,add)
        l1,l2,l3,l4=contact.read()
        contact.append(contact)

    #to write data in file
    def append(self,data):
        lst=[data.name,data.phone,data.e_mail,data.add]
        with open("contact book.csv","a") as f:
           writer=csv.writer(f)
           writer.writerow(lst)

    #to delete a contact
    def delete_contact():
        del_data=[]
        name = input("Enter name of contact:")
        contact = record(name,None,None,None)
        l1,l2,l3,l4=contact.read()
        for i in l1:
            if name==i:
                index = l1.index(i)
                l1.remove(i)
                l2.remove(l2[index])
                l3.remove(l3[index])
                l4.remove(l4[index])
        contact.write(l1,l2,l3,l4)

    #To edit a contact
    def edit_contact():
        edit_data=[]
        name = input("Enter name of contact:")
        contact = record(name, None, None, None)
        l1,l2,l3,l4=contact.read()
        new_name=input("Enter new name:")
        new_ph = input("Enter new phone number:")
        new_email = input("Enter new email:")
        new_add = input("Enter new address:")
        for i in l1:
            if name==i:
                index = l1.index(i)
                l1[index]=new_name
                l2[index]=new_ph
                l3[index]=new_email
                l4[index]=new_add
        edit_data=l1+l2+l3+l4
        contact.write(edit_data)

    def view():
        with open("contact book.csv",'r') as f:
            reader=csv.DictReader(f)
            for i in reader:
                print (i)

    def write(self,name,phone,email,address):
        header = ["name", "Phone number", "e-mail", "address"]
        d=[name,phone,email,address]
        data=zip(name,phone,email,address)
        with open("contact book.csv", 'w') as f:
            writer = csv.writer(f)
            writer.writerow(header)
            for i in data:
                writer.writerow(i)




# printing the main menu
def print_menu():
    choice=5
    print("Main menu:")
    print("1) Create a contact \n2) Delete a contact\n3) Edit a contact\n4) View a contact\n0) Exit")
    choice = input("Enter your choice:")
    if choice=="1":
        record.create_contact()
        print_menu()
    elif choice=="2":
        record.delete_contact()
        print_menu()
    elif choice=="3":
        record.edit_contact()
        print_menu()
    elif choice=="4":
        record.view()
        print_menu()

record.create_file()
print_menu()