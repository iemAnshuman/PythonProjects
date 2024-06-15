import random 
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game = [rock, paper, scissors]

def play(player_input):
    bot = (random.choice(game))
    print(bot)
    if player_input.strip() == "rock":
        if bot == paper:
            print("You lost!")
        elif bot == scissors:
            print("You Won!")
        else:
            print("Draw!")
    elif player_input.strip() == "paper":
        if bot == scissors:
            print("You lost!")
        elif bot == rock:
            print("You Won!")
        else:
            print("Draw!")
    elif player_input.strip() == "scissor":
        if bot == rock:
            print("You lost!")
        elif bot == paper:
            print("You Won!")
        else:
            print("Draw!")
    else:
        print("invalid")

player_input = input("""
What would you like to play?
rock
paper
scissor
exit
""")

while player_input.strip() != "exit": 
    play(player_input)
    player_input = input("""
    What would you like to play?
    rock
    paper
    scissor
    exit
    """)
