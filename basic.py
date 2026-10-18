import pygame
import random 

pygame.init() #start by initialising 

clock = pygame.time.Clock()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # width and height 

class Player(pygame.sprite.Sprite): 
    def __init__(self):
        super().__init__()
        self.surf = pygame.image.load("jet.png").convert() # default x and y axis, then size = height, width
        self.surf.set_colorkey((255, 255, 255))
        self.rect = self.surf.get_rect()
        self.rect.center = (100, 300)

    def update(self, pressed_keys):
        if pressed_keys[pygame.K_UP]:
                self.rect.y -= 5
        if pressed_keys[pygame.K_DOWN]:
                self.rect.y += 5
        if pressed_keys[pygame.K_RIGHT]:
                self.rect.x += 5
        if pressed_keys[pygame.K_LEFT]:
                self.rect.x -= 5
        if self.rect.left < 0: 
                self.rect.left = 0 
        if self.rect.right > 800:
                self.rect.right = 800
        if self.rect.top < 0: 
                self.rect.top = 0
        if self.rect.bottom > 600:
                self.rect.bottom = 600

class Enemy(pygame.sprite.Sprite): 
      def __init__(self):
            super().__init__()
            self.surf = pygame.image.load("missile.png").convert() # default x and y axis, then size = height, width
            self.surf.set_colorkey((255, 255, 255))
            self.rect = self.surf.get_rect()
            self.rect.center = (
                  SCREEN_WIDTH + 10, 
                  random.randint(0, SCREEN_HEIGHT)
            )
            self.speed = random.randint(5, 20)

      def update(self):
            self.rect.x -= self.speed
            if self.rect.left < 0: 
                  self.kill()

player = Player()
enemies = pygame.sprite.Group()
add_enemy = pygame.USEREVENT + 1
pygame.time.set_timer(add_enemy, 200) # milisecond

running = True 

while running: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False 
        elif event.type == add_enemy:
            new_enemy = Enemy()
            enemies.add(new_enemy)

    screen.fill((100, 100, 125))

    
    pressed_keys = pygame.key.get_pressed()

    player.update(pressed_keys) # player.up/right/top/bottom define how far the rectangle can travel
    screen.blit(player.surf, player.rect) # where, color and the defined player from earlier
    enemies.update()
    for enemy in enemies: 
          screen.blit(enemy.surf, enemy.rect)

    if pygame.sprite.spritecollideany(player, enemies):
          player.kill()
          running = False
    pygame.display.flip() # update the display

    clock.tick(120) # frames per second 

pygame.quit() #ends by quitting the pygame 
