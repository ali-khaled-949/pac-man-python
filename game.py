import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Maze layout
maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
    [1, 2, 1, 1, 1, 1, 2, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1],
    [1, 2, 1, 1, 1, 1, 2, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1],
    [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
    [1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1],
    [1, 2, 2, 1, 2, 2, 2, 1, 2, 2, 0, 2, 2, 1, 2, 2, 2, 1, 2, 2, 1],
    [1, 1, 2, 1, 1, 1, 2, 1, 2, 1, 1, 1, 2, 1, 2, 1, 1, 1, 2, 1, 1],
    [1, 1, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1],
    [1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1],
    [1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1],
    [1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
    [1, 2, 1, 1, 1, 1, 2, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1],
    [1, 2, 1, 1, 1, 1, 2, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1],
    [1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
    [1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1],
    [1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1],
    [1, 2, 1, 1, 1, 1, 2, 1, 2, 1, 1, 1, 2, 1, 2, 1, 1, 1, 1, 2, 1],
    [1, 2, 1, 1, 1, 1, 2, 1, 2, 1, 1, 1, 2, 1, 2, 1, 1, 1, 1, 2, 1],
    [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

# Set colors
WHITE = (255, 255, 255)
BLUE = (33, 33, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MENU = 0
PLAYING = 1
GAME_OVER = 2
game_state = MENU

# Calculate maze dimensions
num_rows = len(maze)
num_cols = len(maze[0])

# Set cell size
cell_size = 40

# Calculate window size
screen_width = num_cols * cell_size
screen_height = num_rows * cell_size

# Set up the display
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pac-Man")

# Score / Scoreboard
score = 0
font = pygame.font.SysFont("arial", 24)

# Load Pac-Man image
pacman_img = pygame.image.load('pacman-icon.png').convert_alpha()  # Make sure the filename is correct
pacman_img = pygame.transform.scale(pacman_img, (cell_size, cell_size))
# Initialize Pac-Man position and speed
pacman_x = (num_cols // 2) * cell_size + cell_size // 2
pacman_y = (num_rows // 2) * cell_size + cell_size // 2

pacman_center_x = pacman_x - (cell_size // 2)
pacman_center_y = pacman_y - (cell_size // 2)
screen.blit(pacman_img, (pacman_center_x, pacman_center_y))
# Initialize Pac-Man position and speed
pacman_x = 12 * cell_size + cell_size // 2
pacman_y = 17 * cell_size + cell_size // 2

pacman_speed = 1  # Adjust Pac-Man speed

WAITING_FOR_DECISION = 3

# Define Ghost class
class Ghost:
    def __init__(self, color):
        self.color = color
        self.speed = 1.5  # Adjust ghost speed
        self.direction = random.choice(['left', 'right', 'up', 'down'])
        self.x, self.y = self.find_valid_start_position()

    def find_valid_start_position(self):
        while True:
            x = random.randint(0, num_cols - 1) * cell_size + cell_size // 2
            y = random.randint(0, num_rows - 1) * cell_size + cell_size // 2
            if maze[y // cell_size][x // cell_size] != 1:
                return x, y

    def move(self):
        dx, dy = 0, 0
        if self.direction == 'up':
            dy -= self.speed
        elif self.direction == 'down':
            dy += self.speed
        elif self.direction == 'left':
            dx -= self.speed
        elif self.direction == 'right':
            dx += self.speed

        # Calculate new position
        new_x = int(self.x + dx)  # Convert to integer
        new_y = int(self.y + dy)  # Convert to integer

        # Check if the new position is valid
        if self.is_valid_position(new_x, new_y):
            self.x = new_x
            self.y = new_y
        else:
            # Change direction randomly if the new position is invalid
            self.direction = random.choice(['left', 'right', 'up', 'down'])

    def is_valid_position(self, x, y):
        # Check if the new position is within the maze boundaries and not a wall
        return 0 <= x < screen_width and 0 <= y < screen_height and maze[y // cell_size][x // cell_size] != 1

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), cell_size // 2)

# Create ghosts
ghosts = [Ghost(RED), Ghost(BLUE)]

# Sound effects
pellet_sound = pygame.mixer.Sound('pellet.wav')
power_pellet_sound = pygame.mixer.Sound('power_pellet.wav')
eat_ghost_sound = pygame.mixer.Sound('eat_ghost.wav')
eat_pellet_sound = pygame.mixer.Sound('eat_pellet.wav')
game_over_sound = pygame.mixer.Sound('game_over.wav')

# Adjusting sound volume
game_over_sound.set_volume(0.5)  
pellet_sound.set_volume(0.5)
power_pellet_sound.set_volume(0.5)  
eat_ghost_sound.set_volume(0.5)  

# Main game loop
running = True
grid_x = pacman_x // cell_size
grid_y = pacman_y // cell_size

powered_up = False
power_up_timer = 0

# Adjust timing of sound effects
pellet_timer = 0
power_pellet_timer = 0
ghost_eaten_timer = 0
pacman_direction = 'right'  # or any default direction you prefer
game_over = False

lives = 3

def draw_button(text, x, y, width, height, inactive_color, active_color, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + width > mouse[0] > x and y + height > mouse[1] > y:
        pygame.draw.rect(screen, active_color, (x, y, width, height))
        if click[0] == 1 and action is not None:
            action()
    else:
        pygame.draw.rect(screen, inactive_color, (x, y, width, height))

    small_text = pygame.font.Font(None, 20)
    text_surf, text_rect = text_objects(text, small_text)
    text_rect.center = ((x + (width / 2)), (y + (height / 2)))
    screen.blit(text_surf, text_rect)

def text_objects(text, font):
    text_surface = font.render(text, True, WHITE)
    return text_surface, text_surface.get_rect()

def quit_game():
    global game_state
    game_state = MENU
    pygame.quit()
    sys.exit()

def restart_game():
    global score, pacman_x, pacman_y, powered_up, power_up_timer, pellet_timer, power_pellet_timer, ghost_eaten_timer, game_over, lives, game_state
    game_state = PLAYING
    score = 0
    pacman_x = 12 * cell_size + cell_size // 2
    pacman_y = 17 * cell_size + cell_size // 2
    powered_up = False
    power_up_timer = 0
    pellet_timer = 0
    power_pellet_timer = 0
    ghost_eaten_timer = 0
    game_over = False
    lives = 3

def start_playing():
    global game_state
    game_state = PLAYING

while running:
    
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            quit_game()

        # Handle keyboard input
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if maze[(grid_y - 1)][grid_x] != 1:  # Check if the next position is not a wall
                    pacman_direction = 'up'
            elif event.key == pygame.K_DOWN:
                if maze[(grid_y + 1)][grid_x] != 1:
                    pacman_direction = 'down'
            elif event.key == pygame.K_LEFT:
                if maze[grid_y][(grid_x - 1)] != 1:
                    pacman_direction = 'left'
            elif event.key == pygame.K_RIGHT:
                if maze[grid_y][(grid_x + 1)] != 1:
                    pacman_direction = 'right'


    if game_state == MENU:
        draw_button("Play", 150, 450, 100, 50, GREEN, (0, 255, 0), start_playing)
        draw_button("Quit", 550, 450, 100, 50, RED, (255, 0, 0), quit_game)

    elif game_state == PLAYING:
        # Handle Pac-Man movement
        if pacman_direction == 'up':
            if maze[(grid_y - 1)][grid_x] != 1:
                pacman_y -= pacman_speed
        elif pacman_direction == 'down':
            if maze[(grid_y + 1)][grid_x] != 1:
                pacman_y += pacman_speed
        elif pacman_direction == 'left':
            if maze[grid_y][(grid_x - 1)] != 1:
                pacman_x -= pacman_speed
        elif pacman_direction == 'right':
            if maze[grid_y][(grid_x + 1)] != 1:
                pacman_x += pacman_speed


        grid_x = pacman_x // cell_size
        grid_y = pacman_y // cell_size

        # Check for collision with pellets
        if maze[grid_y][grid_x] == 2:
            maze[grid_y][grid_x] = 0
            score += 10
            pellet_sound.play()
            pellet_timer = pygame.time.get_ticks()

        # Check for collision with power pellets
        elif maze[grid_y][grid_x] == 3:
            maze[grid_y][grid_x] = 0
            powered_up = True
            power_up_timer = pygame.time.get_ticks()
            power_pellet_sound.play()
            for ghost in ghosts:
                ghost_eaten_timer = pygame.time.get_ticks()

        # Check for collision with ghosts
        for ghost in ghosts:
            if abs(pacman_x - ghost.x) < cell_size // 2 and abs(pacman_y - ghost.y) < cell_size // 2:
                if powered_up:
                    score += 200
                    ghost.x, ghost.y = ghost.find_valid_start_position()
                    eat_ghost_sound.play()
                    ghost_eaten_timer = pygame.time.get_ticks()
                else:
                    lives -= 1
                    game_over_sound.play()
                    if lives == 0:
                        game_over = True
                        game_state = GAME_OVER
                    else:
                        pacman_x = 12 * cell_size + cell_size // 2
                        pacman_y = 17 * cell_size + cell_size // 2
                        pacman_direction = 'right'
                        break

        # Draw maze
        for y in range(num_rows):
            for x in range(num_cols):
                if maze[y][x] == 1:
                    pygame.draw.rect(screen, BLUE, (x * cell_size, y * cell_size, cell_size, cell_size))
                elif maze[y][x] == 2:
                    pygame.draw.circle(screen, WHITE, (x * cell_size + cell_size // 2, y * cell_size + cell_size // 2), 4)

        # Draw pellets
        for y in range(num_rows):
            for x in range(num_cols):
                if maze[y][x] == 2:
                    pygame.draw.circle(screen, WHITE, (x * cell_size + cell_size // 2, y * cell_size + cell_size // 2), 4)

        # Draw power pellets
        for y in range(num_rows):
            for x in range(num_cols):
                if maze[y][x] == 3:
                    pygame.draw.circle(screen, YELLOW, (x * cell_size + cell_size // 2, y * cell_size + cell_size // 2), 6)

        # Draw Pac-Man
        screen.blit(pacman_img, (pacman_x - cell_size // 2, pacman_y - cell_size // 2))

        # Move ghosts
        for ghost in ghosts:
            ghost.move()

        # Draw ghosts
        for ghost in ghosts:
            ghost.draw(screen)

        # Draw score
        score_text = font.render(f'Score: {score}', True, WHITE)
        screen.blit(score_text, (10, 10))

        # Draw lives
        for i in range(lives):
            pygame.draw.circle(screen, YELLOW, (i * 30 + 20, screen_height - 20), 10)

        # Check if all pellets are eaten
        if all(maze[y][x] != 2 for y in range(num_rows) for x in range(num_cols)):
            game_over = True
            game_state = GAME_OVER

    elif game_state == GAME_OVER:
        # Game over screen
        text = font.render("Game Over", True, WHITE)
        text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2))
        screen.blit(text, text_rect)
        draw_button("Play Again", 150, 450, 150, 50, GREEN, (0, 255, 0), restart_game)
        draw_button("Quit", 550, 450, 100, 50, RED, (255, 0, 0), quit_game)

    pygame.display.flip()
