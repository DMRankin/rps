from player import Player

name = input("Please enter your name: ")

def play_game():
    pass 

def player_choice():
    choice = input("Please Choose Rock, Paper or Scissors")
    return choice

def create_player(name, choice): 
    new_player = Player(name, choice)
    return new_player 

def create_computer_player():
    pass

def get_winner(player, computer): 
    pass 


