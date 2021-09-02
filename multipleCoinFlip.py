import random, os, math, time



def startGame():
    
    flipCoinQuestion = input("Do you want to Flip the Coin? ")
    
    if flipCoinQuestion == "n":
        quit()
    else:
        Flips_Num = input("Number of Flips  \n > ")
        if Flips_Num == '':
            print('Enter a number')
        else:
            CoinFlip(int(Flips_Num))



def CoinFlip(Flips_Num):
    heads_amount = 0
    tails_amount = 0
    heads_percent = 0
    tails_percent = 0
    for i in range(Flips_Num):
        rand = random.randint(1,2)
        if rand == 1:
            tails_amount += 1
            print('Tails', tails_amount)
        else:
            heads_amount += 1
            print('Heads', heads_amount)
    
    heads_percent = heads_amount / Flips_Num *100
    tails_percent = tails_amount / Flips_Num *100


    if heads_amount == 1:
        print('\nHeads flipped', heads_amount, 'time.')
        print('\nHeads percentage', heads_percent,'%')
    else:
        print('\nHeads flipped', heads_amount, 'times.')
        print('\nHeads percentage', heads_percent,'%')


    if tails_amount == 1:
        print('\nTails flipped', tails_amount, 'time.')
        print('\nTails percentage', tails_percent,'%')
    else:
        print('\nTails flipped', tails_amount, 'times.')
        print('\nTails percentage', tails_percent,'%')



    
    

startGame()
print('\n\n')
os.system("pause")