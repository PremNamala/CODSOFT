import os, time, random
player1_score = 0
player2_score = 0
while(1):
    os.system('cls' if os.name == 'nt' else 'clear')
    if(player1_score == 3 or player2_score == 3):
        break
    else:
        print("---Rock Paper Scissors---\n")
        print("\nplayer1\t\tplayer2\n\n  ",player1_score,"\t\t  ",player2_score)
    player1 = input("\nYou : ")
    player1.lower()
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')
    player2 = random.choice(['rock','paper','scissors'])
    if player1 in ['rock','paper','scissors'] and player2 in ['rock','paper','scissors']:       
        #Rock
        if(player1 == 'rock' or player2 == 'rock'):
            if(player1 == 'rock' and player2 == 'rock'):
                print("You : ",player1,"\tComputer : ",player2)
                print("\n\t\tTie")
            elif(player1 == 'paper' or player2 == 'paper'):
                if(player1 == 'paper'):
                    print("You : ",player1,"\tComputer : ",player2)
                    print("\n\tYou won")
                    player1_score += 1
                else:
                    print("You : ",player1,"\tComputer : ",player2)
                    print("\n\tComputer Won")
                    player2_score += 1
            else:
                if(player1 == 'rock'):
                    print("You : ",player1,"\tComputer : ",player2)
                    print("\n\tYou won")
                    player1_score += 1
                else:
                    print("You : ",player1,"\tComputer : ",player2)
                    print("\n\tComputer Won")
                    player2_score += 1
        #Paper
        elif(player1 == 'paper' or player2 == 'paper'):
            if(player1 == 'paper' and player2 == 'paper'):
                print("You : ",player1,"\tComputer : ",player2)
                print("\n\t\tTie")
            elif(player1 == 'scissors' or player2 == 'scissors'):
                if(player1 == 'scissors'):
                    print("You : ",player1,"\tComputer : ",player2)
                    print("\n\tYou won")
                    player1_score += 1
                else:
                    print("You : ",player1,"\tComputer : ",player2)
                    print("\n\tComputer Won")
                    player2_score += 1
            else:
                if(player1 == 'paper'):
                    print("You : ",player1,"\tComputer : ",player2)
                    print("\n\tYou won")
                    player1_score += 1
                else:
                    print("You : ",player1,"\tComputer : ",player2)
                    print("\n\tComputer Won")
                    player2_score += 1
        #Scissors
        elif(player1 == 'scissors' or player2 == 'scissors'):
            if(player1 == 'scissors' and player2 == 'scissors'):
                print("You : ",player1,"\tComputer : ",player2)
                print("\n\t\tTie")
            elif(player1 == 'rock' or player2 == 'rock'):
                if(player1 == 'rock'):
                    print("You : ",player1,"\tComputer : ",player2)
                    print("\n\tYou won")
                    player1_score += 1
                else:
                    print("You : ",player1,"\tComputer : ",player2)
                    print("\n\tComputer Won")
                    player2_score += 1
            else:
                if(player1 == 'scissors'):
                    print("You : ",player1,"\tComputer : ",player2)
                    print("\n\tYou won")
                    player1_score += 1
                else:
                    print("You : ",player1,"\tComputer : ",player2)
                    print("\n\tComputer Won")
                    player2_score += 1
        
    #if end      
    else:
        print("Inavlid Choice")
    time.sleep(3)
