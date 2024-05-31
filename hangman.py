import random

graphics = ['''
                _______
                |/    |
                |    
                |    
                |     
                |    
                |
               _|___

            ''',
            '''
                _______
                |/    |
                |    (_)
                |    
                |     
                |    
                |
               _|___

            ''',
            '''
                _______
                |/    |
                |    (_)
                |     |
                |     |
                |     
                |
               _|___

            ''',
            '''
                _______
                |/    |
                |    (_)
                |     |
                |     |
                |      \ 
                |
               _|___

            ''',
            '''
                _______
                |/    |
                |    (_)
                |     |
                |     |
                |    / \  
                |
               _|___

            ''',
            '''
                _______
                |/    |
                |    (_)
                |     |/
                |     |
                |    / \ 
                |
               _|___

            ''',
            '''
                _______
                |/    |
                |    (_)
                |    \|/
                |     |
                |    / \ 
                |
               _|___

            '''
]



gameover = ''' GAMEOVER!!!!! :

                         _                                             
                        | |                                            
                        | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
                        | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
                        | | | | (_| | | | | (_| | | | | | | (_| | | | |
                        |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                                            __/ |                      
                                           |___/  
                                    
            '''
import random
word_list = ['hello','baby','horse','tiger','tomato','jeep','carrot','chicken']
word = random.choice(word_list)

#putting the string word in list
choosen_word = [ x for x in word ]

#print(choosen_word)



display = []

for item in range(0,len(choosen_word)) :
    display.append("_")


print(display)
count_ = 0

while "_" in display: #till all guess true it will run
    guess = input('Guess a letter\n').lower()
    if guess in choosen_word: 
        print("Correct")
        for item in range(0,len(choosen_word)) :
            if choosen_word[item] == guess:
                display[item] = guess
        print(display)
                
    if guess not in choosen_word:
        print("incorrect")
        print(graphics[count_])
        print(display)
        count_ +=1
    
    if count_ == len(graphics): #when all the graphics were shown it will break
        break



if "_" not in display:
    print("Congratulation!!!! You Won ")
if "_" in display:
    print(gameover)


