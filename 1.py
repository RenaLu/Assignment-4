#####################################################################
# Purpose: This program simulates the game "eenie meenie miney moe"
# Prerequisites: Arrays and modular indexing
# Programmer: Rena Lu
# Last modified: April 8, 2014
#####################################################################


#================ Inputs and Preparation ==================#

# Let the user input a rhyme and create array for the rhyme/phrase
phraseinput=input("Enter your rhyme: ")
phrase=phraseinput.split(' ')

print ("The rhyme is: ", end='')
for a in range (0, len(phrase)):
    print (phrase[a] + " ",end='')
    
print ()

# Let the user input the list of players and create array for the players
player=[]

playernum=int(input("Enter the number of players: "))
for a in range (0, playernum):
    individual=input("Enter the player: ")
    player.append(individual)
    
print ()
print ("The participating players are: " + str(player))
print ()

#========== Start to pick and eliminate players ===========#

# Program will run 1 times less than the total player number to give the winner

for i in range (0, playernum-1):
    
    for j in range (0, len(phrase)):
        
        n=j%len(player)

        # The first time the game runs, each phrase is assigned to a player in order
        if i == 0:
            print (phrase[j]+"="+player[n])
            index = n
            indexPrint = index

        # After the first time, the game starts with the player after the previous player elminated
        else:
            print (phrase[j]+"="+player[index])
            indexPrint = index

            # If the eliminated player is the last player in the list, start from the first player again
            if index == len(player)-1:
                index = 0
            else:
                index = index + 1
                
        
        # If the phrase reaches the last word, the player assigned to it is eliminated
        if phrase[j] == phrase[len(phrase)-1]:
            print ()
            print (player[indexPrint] + " is out" )
            player.remove(player[indexPrint])
            print ()
            
    if len(player)>1:
        print ("The remaining players are: " + str(player))
    else:
        print ("The remaining player is " + str(player))
    print ()

    # If the eliminated player is the last player in the list, start from the first player again
    if indexPrint == len(player):
        index = 0
    else:
        index = indexPrint
    
print ()
print ("The Winner is " + player[0]+ "!")

