from unicodedata import name
import csv

class categories:
    ledger=[] #Class attribute 
    #Attributes
    def __init__(self,name,income,dis):
        self.name=name
        self.income=income
        self.dis=dis

    #creating instances
    def create_instances():
        list=[]
        user=input("Enter your category:")
        user=categories(user,int(input("Enter your income:")),input("Enter discription:"))
        list.append(user.name)
        list.append(str(user.income))
        list.append(user.dis)
        categories.ledger.append(list)
        #Writing into a csv file
        categories.write()
        
    #For reading from csv 
    def reading():
        lis=[]
        name_list=[]
        amount_list=[]
        discription_list=[]
        with open('Data.csv','r') as f:
            reader=csv.DictReader(f)
            for i in reversed(list(reader)):
                name_list.append(i['name'])
                amount_list.append(i['amount'])
                discription_list.append(i['discription'])
                lis.append(i['name'])
                lis.append(i['amount'])
                lis.append(i['discription'])
                categories.ledger.append(lis)
                lis.clear()
        return name_list,amount_list,discription_list           
          
          
    #creating and writing to a csv file
    def write():
        header=["name","amount","discription"]
        with open('Data.csv','w') as f:
            writer=csv.writer(f)
            writer.writerow(header)
            writer.writerows(categories.ledger)  

    #for deposit
    def deposit():
        data_list=[]
        user_name=input("Enter name of category:")
        user_amount=input("Enter amount to be deposited:")
        user_dis=input("Enter discription for deposit:")
        names,amount,discription=categories.reading()
        for i in names:
            if i ==user_name:
               index=names.index(i)
               prev_amount=amount[index]
               new_amount=int(prev_amount)+int(user_amount)
               data_list.append(user_name)
               data_list.append(str(new_amount))
               data_list.append(user_dis)
        categories.ledger.append(data_list)
        categories.write()

    #for withdraw
    def withdraw():
        data_list=[]
        user_name=input("Enter name of category:")
        user_amount=input("Enter amount to be withdrawn:")
        user_dis=input("Enter discription for withdraw:")
        names,amount,discription=categories.reading()
        for i in names:
            if i ==user_name:
               index=names.index(i)
               prev_amount=amount[index]
               new_amount=int(prev_amount)-int(user_amount)
               data_list.append(user_name)
               data_list.append(str(new_amount))
               data_list.append(user_dis)
        categories.ledger.append(data_list)
        categories.write()
        
    #Transfer from one category to another
    def transfer():
        list_1=[]
        list_2=[] 
        first_name=input("Category name to transfer from: ")
        first_amount=input("Amount to be transfered:")    
        second_name=input("Category name to transfer to: ")
        names,amount,dis=categories.reading()
        for i in names:
            if i==first_name:
                index=names.index(i)
                new_amount=int(amount[index])-int(first_amount)
                first_dis=dis[index]
            if i==second_name:
                index=names.index(i)
                second_amount=int(amount[index])+int(first_amount)
                second_dis=dis[index]
        list_1.append(first_name)
        list_1.append(new_amount)
        list_1.append(first_dis)
        list_2.append(second_name)
        list_2.append(second_amount)
        list_2.append(second_dis)
        categories.ledger.append(list_1)        
        categories.ledger.append(list_2)
        categories.write()

    #check balance
    def check_balance():
        data_amount=[]
        data_discription=[]
        user_name=input("Enter name of category:")
        names,amount,discription=categories.reading()
        for i in names:
            if i==user_name:
                index=names.index(i)
                data_amount.append(amount[index])
                data_discription.append(discription[index])
                names[index]=""       
        initial_amount=data_amount[-1]
        print("*****"+user_name+"*****")
        print("initial amount:"+str(initial_amount))
        for j in data_amount:
            if j!=initial_amount:
               ind=data_amount.index(j)
               amount_alter=int(initial_amount)-int(j)
               initial_amount=int(initial_amount)+amount_alter
               print(str(amount_alter)+"  "+data_discription[ind])
        print("Balance:"+str(initial_amount))
                        


#print main menu
def main():
        choice=1
        while choice!=0:
            print("1)Create category")
            print("2)Deposit amount")
            print("3)Withdraw amount")
            print("4)Transfer amount")
            print("5)Check balance")
            print("0)Exit")
            choice=int(input("Enter your choice number:"))
            if choice==1:
                categories.create_instances()
            elif choice==2:
                categories.deposit()
            elif choice==3:
                categories.withdraw()
            elif choice==4:
                categories.transfer()
            elif choice==5:
                categories.check_balance()


main()