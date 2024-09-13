import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 640, 480
FPS = 60
PLAYER_SPEED = 5
ITEM_SIZE = 40

# Colors
BLACK = (0, 0, 0)
RETRO_GREEN = (0, 255, 0)
RETRO_RED = (255, 0, 0)
RETRO_YELLOW = (255, 255, 0)
RETRO_CYAN = (0, 255, 255)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Squirrel Finder")

# Load images
try:
    koala_img = pygame.image.load('koala.png').convert_alpha()
    koala_img = pygame.transform.scale(koala_img, (ITEM_SIZE, ITEM_SIZE))
    strawberry_img = pygame.image.load('strawberry.png').convert_alpha()
    strawberry_img = pygame.transform.scale(strawberry_img, (ITEM_SIZE, ITEM_SIZE))
    squirrel_img = pygame.image.load('squirrel.png').convert_alpha()
    squirrel_img = pygame.transform.scale(squirrel_img, (ITEM_SIZE, ITEM_SIZE))
except pygame.error as e:
    print("Error loading images. Make sure koala.png, strawberry.png, and squirrel.png are in the same directory.")
    sys.exit()

# Fonts
font = pygame.font.SysFont('Courier', 20)

# Clock
clock = pygame.time.Clock()

# Sprites
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = koala_img
        self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT // 2))

    def update(self, keys_pressed):
        if keys_pressed[pygame.K_LEFT]:
            self.rect.x -= PLAYER_SPEED
        if keys_pressed[pygame.K_RIGHT]:
            self.rect.x += PLAYER_SPEED
        if keys_pressed[pygame.K_UP]:
            self.rect.y -= PLAYER_SPEED
        if keys_pressed[pygame.K_DOWN]:
            self.rect.y += PLAYER_SPEED

        # Keep player on screen
        self.rect.clamp_ip(screen.get_rect())

class Strawberry(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = strawberry_img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - ITEM_SIZE)
        self.rect.y = random.randint(0, HEIGHT - ITEM_SIZE)
        self.vx = random.choice([-3, -2, -1, 1, 2, 3])
        self.vy = random.choice([-3, -2, -1, 1, 2, 3])

    def update(self):
        self.rect.x += self.vx
        self.rect.y += self.vy

        # Bounce off walls
        if self.rect.left <= 0 or self.rect.right >= WIDTH:
            self.vx *= -1
        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.vy *= -1

class Squirrel(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = squirrel_img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - ITEM_SIZE)
        self.rect.y = random.randint(0, HEIGHT - ITEM_SIZE)
        self.vx = random.choice([-4, -3, -2, 2, 3, 4])
        self.vy = random.choice([-4, -3, -2, 2, 3, 4])

    def update(self):
        self.rect.x += self.vx
        self.rect.y += self.vy

        # Bounce off walls
        if self.rect.left <= 0 or self.rect.right >= WIDTH:
            self.vx *= -1
        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.vy *= -1

def show_instructions():
    instructions = [
        "SQUIRREL FINDER",
        "",
        "Instructions:",
        "- You are the koala.",
        "- Use arrow keys to move quickly.",
        "- Avoid strawberries; they are deadly!",
        "- After 3 seconds, a squirrel appears.",
        "- Find and touch the squirrel to win.",
        "",
        "Press any key to start..."
    ]
    screen.fill(BLACK)
    y_offset = 100
    for line in instructions:
        text_surface = font.render(line, True, RETRO_GREEN)
        text_rect = text_surface.get_rect(center=(WIDTH // 2, y_offset))
        screen.blit(text_surface, text_rect)
        y_offset += 30
    pygame.display.flip()
    wait_for_key()

def wait_for_key():
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                waiting = False

def main():
    while True:
        show_instructions()
        game_loop()

def game_loop():
    # Initialize game variables
    player = Player()
    player_group = pygame.sprite.Group(player)
    strawberry_group = pygame.sprite.Group()
    squirrel_group = pygame.sprite.Group()

    strawberry_timer = 0
    squirrel_timer = 0
    game_time = 0

    running = True
    while running:
        dt = clock.tick(FPS) / 1000.0  # Amount of seconds between each loop
        game_time += dt
        strawberry_timer += dt
        squirrel_timer += dt

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Spawn strawberries every second
        if strawberry_timer >= 1:
            strawberry = Strawberry()
            strawberry_group.add(strawberry)
            strawberry_timer = 0

        # Spawn squirrel after 3 seconds
        if squirrel_timer >= 3 and len(squirrel_group) == 0:
            squirrel = Squirrel()
            squirrel_group.add(squirrel)

        keys_pressed = pygame.key.get_pressed()
        player_group.update(keys_pressed)
        strawberry_group.update()
        squirrel_group.update()

        # Check for collisions
        if pygame.sprite.spritecollideany(player, strawberry_group):
            # Player dies
            display_message("You were hit by a strawberry! You lose.")
            running = False
            continue

        if pygame.sprite.spritecollideany(player, squirrel_group):
            # Player wins
            display_message("You found the squirrel! You win!")
            running = False
            continue

        # Draw everything
        screen.fill(BLACK)
        player_group.draw(screen)
        strawberry_group.draw(screen)
        squirrel_group.draw(screen)

        # Draw "openai" text
        openai_text = font.render("openai", True, RETRO_CYAN)
        screen.blit(openai_text, (10, HEIGHT - 30))

        # Draw timer
        timer_text = font.render(f"Time: {int(game_time)}", True, RETRO_YELLOW)
        screen.blit(timer_text, (WIDTH - 100, 10))

        pygame.display.flip()

def display_message(message):
    screen.fill(BLACK)
    text_surface = font.render(message, True, RETRO_RED)
    text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(text_surface, text_rect)
    pygame.display.flip()
    pygame.time.wait(2000)  # Pause for 2 seconds

if __name__ == "__main__":
    main()
