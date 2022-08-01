import random

class Generator:
    alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','p','q','r','s','t','u','v','w','x','y','z']
    nums=[str(i) for i in range(0,10)]
    spe=['!','@','#','$','%','^','&','*',]

    def __init__(self,length,min_num,min_spe):
        self.length=length
        self.min_num=min_num
        self.min_spe=min_spe

    #Function to pick random alphabets
    def alphabets(self):
        return random.choice(self.alpha)

    #Function to pick random numbers
    def numbers(self):
        return random.choice(self.nums)

    #Function to pick random speacial characters
    def special(self):
        return random.choice(self.spe)

    def generator(self):
        password=""
        while len(password)!=self.length:
            rand_num=random.randint(0,2)
            if rand_num==0 :
               password=password+self.alphabets()
            elif rand_num==1:
               password=password+self.numbers()
            else:
               password=password+self.special()

        print("Your new password:"+password)

p1=Generator(8,2,2)
p1.generator()
