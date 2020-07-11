'''
Rock , paper, scissor

1. we have 2 players
2. there choices
3. compare choices
         -- result
               a.win
               b.lose
               c.tie

notes
rock beats scissor
paper beats rock
scissor beats paper
'''
import random
wins = 0
ties = 0
losses = 0
print("Welcome to the game of Rock,Paper and Scissors ")


computer = random.randint(1, 3)

user = int(input("[1] Rock   [2] Paper    [3] Scissor   [9] Quit:  "))
run = True
while run and user != 9:
    if user == 1:
        if computer == 1:
            print("Ties")
            ties += 1
            run = False
        elif computer == 2:
            print("Computer wins")
            losses += 1
        else:
            print("Player wins")
            wins += 1

    elif user == 2:
        if computer == 1:
            print("Player wins")
            wins += 1
        elif computer == 2:
            print("Ties")
            ties += 1
        else:
            print("Computer wins")
            losses += 1
    elif user == 3:
        if computer == 1:
            print("Lost")
            losses += 1
        elif computer == 2:
            print("Wins")
            wins += 1
        else:
            print("tie")
            ties += 1

print("Wins: %s, Ties: %s, Losses: %s" % (wins, ties, losses))
