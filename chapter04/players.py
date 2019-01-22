# slicing a list
players = ['Charles', 'Martina', 'Michael', 'Florence', 'Eli']
print(players[0:3])
print(players[1:3])
print(players[:3])
print(players[2:])
print(players[-3:])

[print(player.title()) for player in players[:3]]