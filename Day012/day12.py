def game():
    def drink_potion():
        potion_strength = 2
        print(potion_strength)

    drink_potion()

    # drink_potion() func can't be called outside of game()


# There is NO such thing as block scope in Python!!
# functions HAS boundaries - so if variable is created IN a func it can be called only within,
# BUT if it's created within IF statement it still can be called outside
game_level = 3
enemies = ['Skeleton', 'Zombie','Alien']
def create_enemy():
    new_enemy = "" # if not created before the IF, when printing it will be just empty value -
    # otherwise it's not a problem and it WILL be printed even if value was never assigned (so not go through IF statement)
    if game_level <5:
        new_enemy = enemies[0]

    print(new_enemy)

