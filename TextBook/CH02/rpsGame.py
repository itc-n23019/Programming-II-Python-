import random

print('ROCK, PAPER, SCISSORS')

wins, losses, ties = 0, 0, 0
moves = ['ROCK', 'PAPER', 'SCISSORS']

while True:
    print(f'{wins} Wins, {losses} Losses, {ties} Ties')
    print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
    player_move = input().lower()
    if player_move == 'q':
        break
    if player_move not in ['r', 'p', 's']:
        print('Type one of r, p, s, or q.')
        continue

    print(moves['rps'.find(player_move)] + ' versus...')

    computer_move = random.randint(0, 2)
    print(moves[computer_move])

    if player_move == 'r' and computer_move == 2 or \
       player_move == 'p' and computer_move == 0 or \
       player_move == 's' and computer_move == 1:
        print('You win!')
        wins += 1
    elif player_move == 'r' and computer_move == 1 or \
         player_move == 'p' and computer_move == 2 or \
         player_move == 's' and computer_move == 0:
        print('You lose!')
        losses += 1
    else:
        print('It is a tie!')
        ties += 1

