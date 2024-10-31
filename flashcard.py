class flashcard:
    def __init__(self,word,meaning):
        self.word =word
        self.meaning =meaning
        
    def __str__(self):
        return f"{self.word} ( {self.meaning} )"
    
flash =[]
print("welcome to flashcard application")

while(True):
    word = input("enter the word you want to add to the flashcard: ")
    meaning = input("enter the meaning of the word:  ")
    
    flash.append(flashcard(word,meaning))
    option = int(input("enter 0 if you want to add another flashcard otherwise add 1 : "))
    
    if(option):
        break
    
print("\nYour flashcards")
for i in flash:
    print(">",i)    
    