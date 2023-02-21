################### Scope ####################

enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")


# local scope
def drink_potion():  # def is like a wall
  # something below can just access within the wall
  potion_strength = 2
  print(potion_strength)

drink_potion()
# print(potion_strength)  # this will cause an error


# global scope
player_health = 10
def drink_potion2():  # def is like a wall
  # something below can just access within the wall
  potion_strength = 2
  print(player_health)

drink_potion2()  # no error

def game():  # the game wall
  def drink_potion3():   # this wall is inside the game wall
    # something below can just access within the wall
    potion_strength = 2
    print(player_health)

# drink_potion3()  # this will cause an error, because out of the wall


# there is no block scope
game_level = 3
enemies = ["skeleteon", "zombie", "alien"]
if game_level < 5:
  new_enemy = enemies[0]

print(new_enemy)  # no error because new_enemy still in the same wall


# modifying global scope
enemies = 1
def increase_enemies3():
  print(f"enemies inside function3: {enemies}")  # still 1
  return enemies + 1

enemies3 = increase_enemies3()
print(f"enemies outside function3: {enemies3}")


def increase_enemies2():
  global enemies
  enemies += 1 # this will change the global variable value
  print(f"enemies inside function2: {enemies}")  # change to 2

increase_enemies2()
print(f"enemies outside function2: {enemies}")


def increase_enemies4():
  print(f"enemies inside function4: {enemies}")  # from 1 to 2
  return enemies + 1

enemies4 = increase_enemies4()
print(f"enemies outside function4: {enemies4}")


# global constant
PI = 3.14159  # we use uppercase for the global constant variable
URL = "https://google.com"

def circle_area(r):
  area = PI * r**2  # global constant can be used for function in the wall
  print(area)
circle_area(5)
circle_area(10)