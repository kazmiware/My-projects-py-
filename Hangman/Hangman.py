import random
word_list=["mustafa","pakistan","apple"]
def choose_word(word_list):
    num=random.randint(0,2)
    return word_list[num]

def board(word):
    length=len(word)
    for row in range(length):
        print("_ ",end="")
    return length
     
def display(correct,word):
    for letter in word:
        if letter in correct:
            print(letter,end="")
        else:
            print("_ ",end="") 

wrong=6
word=choose_word(word_list)
word_length=board(word)
guessed=" "
correct=" "
while wrong>0 and word_length>1:       
    guess=input("\nEnter your guess:")
    if guess not in guessed:
        if guess in word:
            print("\nYou chose correctly!")
            correct=correct+guess
            word_length=word_length-1
        else:
            print("wrong choice:")
            wrong=wrong-1
        guessed=guessed+guess    
        print(f"You have {wrong} guesses left")    
        print("Used letters:"+guessed)
        print(f"{word_length} letters left")           
        for letter in word:
            if letter in correct:
               print(letter,end="")
            else:
               print("_ ",end="")
    elif guess in guessed:
        print("you have used this word!")
if wrong==0:
    print("\nYou lose!") 
else:
    print("\nYou found the word,youn win!")           
