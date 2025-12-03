import pygame 
import random

pygame.init()

screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("레트로 게임")

WHITE = (255, 255, 255)
RED = (255, 0, 0)
Blue  = (0, 0, 255)
BLACK = (0, 0, 0)

game_font = pygame.font.SysFont(None, 40)
class Enemy:
    def __init__(self):
        self.x = 800
        self.y = random.randint(200, 300)
        self.speed = random.randint(10, 20)
        self.rect = pygame.Rect(self.x, self.y, 40, 40)

    def move(self):
        self.x -= self.speed
        self.rect.x = self.x

player_x = 50
player_y = 300
y_change = 0
jump_count = 0
score = 0

enemies = []

game_over = False
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if game_over:
                if event.key == pygame.K_r:
                    game_over = False
                    score = 0
                    enemies.clear()
                    player_y = 300
            elif event.key == pygame.K_SPACE:
                if jump_count < 2:
                    y_change = -15
                    jump_count += 1
    if not game_over:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            player_x -= 5
        
        if keys[pygame.K_RIGHT]:
            player_x += 5

        y_change += 1

        player_y += y_change

        if player_y > 300:
            player_y = 300
            y_change = 0
            jump_count = 0

        player_rect = pygame.Rect(player_x, player_y, 40, 40)

        if random.randint(1, 50) == 1:
            new_enemy = Enemy()
            enemies.append(new_enemy)

        for enemy in enemies:
            enemy.move()

            if player_rect.colliderect(enemy.rect):
                game_over = True

            if enemy.x < -40:
                enemies.remove(enemy)
                score += 10    
                pass

    screen.fill(WHITE)
    
    if not game_over:
        pygame.draw.rect(screen, RED, player_rect)
        for enemy in enemies:
            pygame.draw.rect(screen, Blue,enemy.rect)
    else:
        text = game_font.render("Gane over", True, BLACK)
        screen.blit(text,(250, 180))

    pygame.draw.rect(screen, RED, [player_x,player_y, 40, 40])

    for enemy in enemies:
        pygame.draw.rect(screen, Blue, enemy.rect)

    score_image = game_font.render(f'score: {score}', True, BLACK)

    screen.blit(score_image, (10, 10))

    pygame.display.flip()

    pygame.time.Clock().tick(60)

pygame.quit()