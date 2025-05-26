import math
import random
import pygame
from pygame import mixer

# Initialize pygame
pygame.init()

# Screen setup
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Background
background = pygame.image.load('background.png')

# Caption and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

# Player
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480
playerX_change = 0

def player(x, y):
    screen.blit(playerImg, (x, y))

# Enemy setup
enemyImg = pygame.image.load('enemy.png')
num_of_enemies = 6
enemyX = []
enemyY = []
enemyY_change = []
enemy_direction = 1
enemy_speed = 3

for _ in range(num_of_enemies):
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(50, 150))
    enemyY_change.append(40)

def enemy(x, y):
    screen.blit(enemyImg, (x, y))

# Bullet setup
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletY_change = 10
bullet_state = "ready"

def fire_bullet(x, y):
    screen.blit(bulletImg, (x + 16, y + 10))

def isCollision(ex, ey, bx, by):
    distance = math.hypot(ex - bx, ey - by)
    return distance < 27

def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def set_background():
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

def move_bullet():
    global bulletY, bullet_state
    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change
        if bulletY <= 0:
            bulletY = 480
            bullet_state = "ready"

def game_input():
    global running, playerX_change, bulletX, bulletY, bullet_state, playerX
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletSound = mixer.Sound('laser.wav')
                    bulletSound.play()
                    bulletX = playerX
                    bulletY = playerY
                    bullet_state = "fire"

        if event.type == pygame.KEYUP:
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                playerX_change = 0

    # Move player
    playerX += playerX_change
    playerX = max(0, min(playerX, 736))

def enemy_movement():
    global enemy_direction

    # Determine if any enemy hits screen edge
    move_down = False
    for i in range(num_of_enemies):
        if enemyX[i] <= 0 or enemyX[i] >= 736:
            move_down = True
            break

    # Reverse direction and move all down
    if move_down:
        enemy_direction *= -1
        for i in range(num_of_enemies):
            enemyY[i] += enemyY_change[i]

    # Move all enemies in current direction
    for i in range(num_of_enemies):
        enemyX[i] += enemy_speed * enemy_direction
        enemy(enemyX[i], enemyY[i])

def collision():
    global score_value, bulletY, bullet_state
    for i in range(num_of_enemies):
        if isCollision(enemyX[i], enemyY[i], bulletX, bulletY):
            explosionSound = mixer.Sound("explosion.wav")
            explosionSound.play()
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, 736)
            enemyY[i] = random.randint(50, 150)

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    clock.tick(60)  # Target 60 FPS
    set_background()
    game_input()
    move_bullet()
    enemy_movement()
    collision()
    player(playerX, playerY)
    show_score(textX, textY)
    pygame.display.update()