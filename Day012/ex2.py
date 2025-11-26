enemies = 1


def increase_enemies():
    # this calls that somewhere OUTSIDE the func there is declared variable 'enemies'
    global enemies
    enemies +=1
    print(f"Enemies inside func {enemies}")


increase_enemies()
print(f"Enemies outside func {enemies}")


#if you want to modify it better approach:

def increase_enemies_better(enemy):
    print(f"Enemies inside func {enemies}")
    return enemy + 1

enemies =increase_enemies_better(enemies)
print(f"Enemies outside func {enemies}")