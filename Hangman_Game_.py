import numpy as np
import copy

words=['apple','banana','cherry','papaya','mango','watermelon','dragonfruit','pineapple']

com_guess=list(np.random.choice(words))
com_guess_copy=copy.copy(com_guess)
guess_disp=[]
len_w=len(com_guess)

diff=int(input("enter difficulty :\n1 : easy  2 : normal\n"))

select=np.random.randint(0,len(com_guess),size=diff)


for i in range(len(com_guess)):
    guess_disp.append("*")

guess_disp_copy=copy.copy(guess_disp)

for i in select :
    guess_disp_copy[i]=com_guess[i]

no_tries=len(com_guess)+3
game_score=0

print("\nguess word with {0} alphabets in {1} tries\n{2}\n\n".format(len(com_guess),no_tries," * "*len(com_guess)))

print('hint :',*guess_disp_copy,'\n')

while no_tries>0 :

    print("\nNo of tries left : ",no_tries,'\n')
    inp = input('guess a alphabet :')
    for i in range(len(com_guess)):
        if inp == com_guess[i]:
            com_guess[i]="#"
            guess_disp[i] = inp
            len_w =len_w-1
            print("correct guess")
            break

    no_tries=no_tries-1
    game_score = game_score + 1
    print('guess made :',*guess_disp)

    if  len_w==0:
        break

score=0
for i in range(len(guess_disp)):
    if guess_disp[i]==com_guess_copy[i]:
        score =score+1

if score==len(com_guess_copy):
    print("\nYou have successfully guessed the word 🎊 ✌🤩✌ 🎊 !!! in {0} tries".format(game_score))

else :
    print("\nYou have failed to guess the word 😭😭😭")





