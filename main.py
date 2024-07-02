from maps import Maps
from answer import Answer


answer = Answer()
maps = Maps()
game_on = True
found = 0
while game_on:
    user = maps.user_input()
    if user == "exit":
        game_on = False
    else:
        cont, place, x_cor, y_cor = answer.place_answer(user)
        if cont:
            maps.place_on_map(place, x_cor, y_cor)
            found += 1
            maps.scores(found)
            if found == 50:
                maps.winner()
                game_on = False


maps.exit()
answer.left_answer()
