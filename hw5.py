import random

def is_win(player, opponent):
 
    return (
        (player == 'r' and opponent == 's') or
        (player == 'p' and opponent == 'r') or
        (player == 's' and opponent == 'p')
       
    )
    return False
def play():
    user = input("What's your choice 'r' for rock, 'p' for paper, 's' for scissors: ")
    computer = random.choice(['r', 'p', 's'])
    print(f"Computer chose: {computer}")
    if user == computer:
        return 'tie'
    if is_win(user, computer):
        return 'you win'
    return 'you lose'
game = play()
print(game)