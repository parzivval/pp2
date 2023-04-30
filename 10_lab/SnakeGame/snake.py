import pygame
import random
import time
# import database as db


pygame.init()

WINDOW_WIDTH, WINDOW_HEIGHT = 500, 500
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# COLORS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
WHITE_2 = (100, 100, 100)
BLUE = (0, 0, 200)
GREEN = (0, 150, 0)
RED = (150, 0, 0)
YELLOW = (255, 255, 0)

BLOCK_SIZE = 20

# lvl() is converter 0 1 3 --> easy medium hard
def lvl(n):
  if n == 0: return "Easy"
  elif n == 1: return "Medium"
  else: return "Hard"

# Greed 
def draw_grid():
  for i in range(0, WINDOW_WIDTH, BLOCK_SIZE):
    for j in range(0, WINDOW_HEIGHT, BLOCK_SIZE):
      pygame.draw.rect(screen, WHITE_2, (i, j, BLOCK_SIZE, BLOCK_SIZE), 1)

# WALL -----------------
class Wall:
  def __init__(self):
    self.body = []
    self.load_wall()
  
  def load_wall(self, level=0):
    with open(f'level{level}.txt', 'r') as f:
      wall_body = f.readlines()
    
    for i, line in enumerate(wall_body):
      for j, value in enumerate(line):
        if value == '#':
          self.body.append([j, i])
  
  def draw(self):
    for x, y in self.body:
      pygame.draw.rect(screen, RED, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
  
# FOOD -------------
class Food:
  def __init__(self):
      self.generate_random_pos_0lvl()
  
  def my_round(self, value, base=BLOCK_SIZE):
    return base * round(value / base)

  # for 0 lvl it have to generate random numbers between 0, 480
  def generate_random_pos_0lvl(self):
    self.x = self.my_round(random.randint(0, WINDOW_WIDTH - BLOCK_SIZE))
    self.y = self.my_round(random.randint(0, WINDOW_HEIGHT - BLOCK_SIZE))

  # for 1 lvl it have to generate random numbers between 60, 440
  def generate_random_pos_1lvl(self):
    self.x = self.my_round(random.randint(60, WINDOW_WIDTH - 40 - BLOCK_SIZE))
    self.y = self.my_round(random.randint(60, WINDOW_HEIGHT - 40 - BLOCK_SIZE))

  # for 2 lvl it have to generate random numbers between 100, 380
  def generate_random_pos_2lvl(self):
    self.x = self.my_round(random.randint(100, WINDOW_WIDTH - 100- BLOCK_SIZE))
    self.y = self.my_round(random.randint(100, WINDOW_HEIGHT - 100 - BLOCK_SIZE))

  def draw(self):
    self.color = BLUE
    pygame.draw.rect(screen, self.color, (self.x, self.y, BLOCK_SIZE, BLOCK_SIZE))


# SuperFood is the same Food class, diff between them is COLOR = YELLOW
class SuperFood:
  def __init__(self):
      self.generate_random_pos_0lvl()
  
  def my_round(self, value, base=BLOCK_SIZE):
    return base * round(value / base)
  
  def generate_random_pos_0lvl(self):
    self.x = self.my_round(random.randint(0, WINDOW_WIDTH - BLOCK_SIZE))
    self.y = self.my_round(random.randint(0, WINDOW_HEIGHT - BLOCK_SIZE))

  def generate_random_pos_1lvl(self):
    self.x = self.my_round(random.randint(60, WINDOW_WIDTH - 40 - BLOCK_SIZE))
    self.y = self.my_round(random.randint(60, WINDOW_HEIGHT - 40 - BLOCK_SIZE))

  def generate_random_pos_2lvl(self):
    self.x = self.my_round(random.randint(100, WINDOW_WIDTH - 100- BLOCK_SIZE))
    self.y = self.my_round(random.randint(100, WINDOW_HEIGHT - 100 - BLOCK_SIZE))

  def draw(self):
    self.color = YELLOW
    pygame.draw.rect(screen, self.color, (self.x, self.y, BLOCK_SIZE, BLOCK_SIZE))


# SNAKE ------------------
class Snake:
  def __init__(self):
      self.body = [[10, 10], [11, 10]]
      self.dx = 1
      self.dy = 0
      
  def draw(self):
    for i, (x, y) in enumerate(self.body):
      color = RED if i == 0 else GREEN
      pygame.draw.rect(screen, color, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
  
  def move(self):
    for i in range(len(self.body) - 1, 0, -1):
      self.body[i][0] = self.body[i - 1][0]
      self.body[i][1] = self.body[i - 1][1]

    self.body[0][0] += self.dx
    self.body[0][1] += self.dy

score = 0
level = 0

# Game over func
def game_over():
  # sql = ""
  # if db.acc == "yes":
  #   sql = f"update snake_game set user_score = {score} where username = '{db.username_yes}'; update snake_game set user_level = '{lvl(level)}' where username = '{db.username_yes}';"
  # if db.acc == "no":
  #   sql = f"update snake_game set user_score = {score} where username = '{db.username_no}'; update snake_game set user_level = '{lvl(level)}' where username = '{db.username_no}';"
  # db.cursor.execute(sql)
  # db.conn.commit()

  time.sleep(0.5)
  screen.fill(YELLOW)
  font = pygame.font.SysFont("comicsansms", 40)
  text = font.render('Game Over', True, GREEN)
  screen.blit(text, (WINDOW_WIDTH // 2 - 100, WINDOW_HEIGHT // 2 - 200))

  font2 = pygame.font.SysFont("comicsansms", 30)
  text2 = font2.render(f'Score: {score} || Level: {lvl(level)}', True, GREEN)
  screen.blit(text2, (WINDOW_WIDTH // 2 - 150, WINDOW_HEIGHT // 2 - 150))
  pygame.display.update()
  time.sleep(2)
  pygame.quit()



def main():
  # variables 
  snake = Snake()
  food = Food()
  wall = Wall()
  superfood = SuperFood()

  last_key = ""
  global score, level
  timer = 0

  clock = pygame.time.Clock()
  FPS = 5

  running = True
    # main loop
  while running:
    for event in pygame.event.get():
      if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
        running = False

  # turns ----------------------------------      
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT and last_key != "left":
          last_key = "right"
          snake.dx = 1
          snake.dy = 0
        if event.key == pygame.K_LEFT and last_key != "right":
          last_key = "left"
          snake.dx = -1
          snake.dy = 0
        if event.key == pygame.K_UP and last_key != "down":
          last_key = "up"
          snake.dx = 0
          snake.dy = -1
        if event.key == pygame.K_DOWN and last_key != "up":
          last_key = "down"
          snake.dx = 0
          snake.dy = 1
        if event.key == pygame.K_SPACE:
          snake.body.append([0, 0])
          score += 1
  # --------------------------------------------
    snake.move() 


  # Foods which are disappearing after some time(timer)
    timer += 1
    if timer == 30:
      if level == 0: superfood.generate_random_pos_0lvl()
      if level == 1: superfood.generate_random_pos_1lvl()
      if level == 2: superfood.generate_random_pos_2lvl()
      timer = 0
  #--------------------------


    # ---------------------------------------
    # these lines check boundaries
    if snake.body[0][0] * BLOCK_SIZE > 500:
        game_over()

    if snake.body[0][1] * BLOCK_SIZE > 500:
        game_over()
    
    if snake.body[0][0] < 0:
        game_over()
    
    if snake.body[0][1] < 0:
        game_over()
    # --------------------------------------  

    # Game Over-----------------------------  
    for i in range(1, len(snake.body)):
      if snake.body[i][0] == snake.body[0][0] and snake.body[i][1] == snake.body[0][1]:
        game_over()
        running = False
    #--------------------------------------

    screen.fill(BLACK)
    # draw --------------------------- 
    draw_grid()
    snake.draw()
    food.draw()
    wall.draw()
    # --------------------------------
    
    # if snake eates food --> 1 point ----------------
    if snake.body[0][0] * BLOCK_SIZE == food.x and snake.body[0][1] * BLOCK_SIZE == food.y:
      snake.body.append([0, 0])

      if level == 0: food.generate_random_pos_0lvl()
      if level == 1: food.generate_random_pos_1lvl()
      if level == 2: food.generate_random_pos_2lvl()

      score += 1
    # -------------------------------

    # if snake eates superfood --> 3 point ------------

    if snake.body[0][0] * BLOCK_SIZE == superfood.x and snake.body[0][1] * BLOCK_SIZE == superfood.y:
      snake.body.append([0, 0])

      if level == 0: superfood.generate_random_pos_0lvl()
      if level == 1: superfood.generate_random_pos_1lvl()
      if level == 2: superfood.generate_random_pos_2lvl()

      score += 3
    #-------------------------------------------------
    

    # Managing with level, score, FPS..-------------------
    if score >= 10 and score < 20:
      FPS = 10
      level = 1
      wall.load_wall(level)


    if score >= 20 and score < 40:
      FPS = 15
      level = 2
      wall.load_wall(level)

    if score < 70 and score >= 40:
      FPS = 20
    
    if score % 4 == 0:
      superfood.draw()
    # --------------------------------------------------
      

  # font to see Level, Score, FPS ---------------------
    font = pygame.font.SysFont("comicsansms", 20)
    text = font.render(f'Score: {score} || Level: {lvl(level)} || FPS: {FPS}', True, YELLOW)
    screen.blit(text, (20, 20))
  # --------------------------------------------------  
    pygame.display.update()
    clock.tick(FPS)

main()