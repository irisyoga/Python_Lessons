
import random
game_map = [
    [None, None, None],
    [None, None, None],
    [None, None, None]
]

def main():                 # Если game_map_user выдает True, то ход передается боту, иначе повторяем ход юзера.
  print("Игра началась!")
  print("Первый ход за вами")
  game_map_dash()
  while True:
      while True:
          if game_map_user():
              break
      game_map_dash()
      state = check_state()  # Проверка игрового поля.
      if state is not None:
          break
      game_map_bot()
      game_map_dash()
      state = check_state()
      if state is not None:
          break
  print(f"Игра завершилась, результат: {state}")

def game_map_dash():               #отображение поля
    for i in range(3):
        for j in range(3):
            if game_map[i][j] is None:
                print("_", end = " ")
            else:
                print(game_map[i][j], end = " ")
        print("")

def game_map_user():
    y, x = input("Введите координаты: ").split()
    x = int(x)
    y = int(y)
    if not (0 <= x < 3 and 0 <= y < 3):
        return False
    if game_map[x][y] is not None:
        return False
    game_map[x][y] = "x"
    print(f"я сходил: {y} {x}")
    return True


def game_map_bot():
    empty_cells = [(i, j) for i in range(3) for j in range(3) if game_map[i][j] is None]
    if empty_cells:
        x, y = random.choice(empty_cells)
        game_map[x][y] = "O"
        print(f"Бот сходил: {y} {x}")

def check_state():
    is_full = True

    # Проверка строк
    for i in range(3):
        if all(cell == "x" for cell in game_map[i]):
            return "вы выиграли"
        if all(cell == "0" for cell in game_map[i]):
            return "выиграл бот"
        if None in game_map[i]:
            is_full = False

    # Проверка столбцов
    for j in range(3):
        if all(game_map[i][j] == "x" for i in range(3)):
            return "вы выиграли"
        if all(game_map[i][j] == "0" for i in range(3)):
            return "выиграл бот"

    # Проверка диагоналей
    if game_map[0][0] == game_map[1][1] == game_map[2][2] and game_map[0][0] is not None:
        return "вы выиграли" if game_map[0][0] == "x" else "выиграл бот"
    if game_map[0][2] == game_map[1][1] == game_map[2][0] and game_map[0][2] is not None:
        return "вы выиграли" if game_map[0][2] == "x" else "выиграл бот"

    # Проверка на ничью
    if is_full:
        return "ничья"
    return None


if __name__ == "__main__":
    main()
