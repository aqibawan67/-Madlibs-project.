guess1 = "*****"
guess2 = "*****"
guess3 = "******"
guess4 = "******"
name = "aqib"
game = "pubg"
place = 'pakpattan'
age = 19
guess_over = False
guess_count = 0
guess_limit = 1
while name != guess1 and game != guess2 and place != guess3 and age != guess4 and not guess_over:
    if guess_count < guess_limit:
        guess1 = input("name: ")
        guess2 = input("game: ")
        guess3 = input("place: ")
        guess4 = input("age ")

        guess_count = guess_count + 1
    else:
        guess_over = True
if guess_over:
    print('lose')
else:
    print("my name is " + guess1  + "  my favorite game is " + guess2 + "  my favorite place is " + guess3 +
           "my age is " + guess4, )
    print("   you won the game")
