import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Maze layout
# Maze layout
# Maze layout
maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
    [1, 2, 1, 1, 1, 1, 2, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1],
    [1, 2, 1, 1, 1, 1, 2, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1],
    [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
    [1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1],
    [1, 2, 2, 1, 2, 2, 2, 1, 2, 2, 4, 2, 2, 1, 2, 2, 2, 1, 2, 2, 1],
    [1, 1, 2, 1, 1, 1, 2, 1, 2, 1, 1, 1, 2, 1, 2, 1, 1, 1, 2, 1, 1],
    [1, 1, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1],
    [1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1],
    [1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1],
    [1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
    [1, 2, 1, 1, 1, 1, 2, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1],
    [1, 2, 1, 1, 1, 1, 2, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1],
    [1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
    [1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1],
    [1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 4, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1],
    [1, 2, 1, 1, 1, 1, 2, 1, 2, 1, 1, 1, 2, 1, 2, 1, 1, 1, 1, 2, 1],
    [1, 2, 1, 1, 1, 1, 2, 1, 2, 1, 1, 1, 2, 1, 2, 1, 1, 1, 1, 2, 1],
    [1, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

# Visual representation of the ghost house


GHOST_HOUSE = 5
PELLET = 2
POWER_PELLET = 3
POWER_UP_DURATION = 300

maze[6][10] = GHOST_HOUSE
maze[6][11] = GHOST_HOUSE
maze[7][10] = GHOST_HOUSE
maze[7][11] = GHOST_HOUSE

# Initialize high score
high_score = 0

# Try to load the high score from a file
try:
    with open("high_score.txt", "r") as f:
        file_content = f.read().strip()
        # Ensure the file content is not empty and is a digit before converting
        if file_content.isdigit():
            high_score = int(file_content)
        else:
            print("High score file is empty or contains non-numeric data.")
            high_score = 0
except FileNotFoundError:
    print("High score file not found. A new file will be created.")
    high_score = 0

# Set colors
WHITE = (255, 255, 255)
BLUE = (33, 33, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
PINK = (255, 184, 255)
CYAN = (0, 255, 255)
ORANGE =(255, 184, 82)

# Calculate maze dimensions
cell_size = 40
num_cols = 21
num_rows = 21
# Calculate window size
screen_width = num_cols * cell_size
screen_height = num_rows * cell_size
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pac-Man")

# Set up the display

# Score
score = 0
font = pygame.font.SysFont("arial", 24)

# Load Pac-Man image
pacman_img = pygame.image.load('pacman-icon.png').convert_alpha()
pacman_img = pygame.transform.scale(pacman_img, (cell_size, cell_size))

# Initialize Pac-Man position and speed
pacman_x = 12 * cell_size + cell_size // 2
pacman_y = 17 * cell_size + cell_size // 2

pacman_speed = 1  # Adjust Pac-Man speed

# Define Ghost class
class Ghost:
    def __init__(self, color, behavior):
        self.flashing = False
        self.color = color
        self.behavior = behavior
        self.speed = 1.5  # Adjust ghost speed
        self.direction = random.choice(['left', 'right', 'up', 'down'])
        self.x, self.y = self.find_valid_start_position()

    def find_valid_start_position(self):
        while True:
            x = random.randint(0, num_cols - 1) * cell_size + cell_size // 2
            y = random.randint(0, num_rows - 1) * cell_size + cell_size // 2
            if maze[y // cell_size][x // cell_size] != 1 and not (8 <= x // cell_size <= 12 and 8 <= y // cell_size <= 12):
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
        if self.flashing and powered_up:
            # Alternate between the ghost's color and white every 10 frames
            frame_count = pygame.time.get_ticks() // 100  # Adjust 100 to change flashing speed
            if frame_count % 2 == 0:
                draw_color = self.color
            else:
                draw_color = WHITE
        else:
            draw_color = self.color

        pygame.draw.circle(screen, draw_color, (int(self.x), int(self.y)), cell_size // 2)




# Create ghosts
ghosts = [Ghost(RED, 'chase'), Ghost(PINK, 'ambush'), Ghost(CYAN, 'random'), Ghost(ORANGE, 'scatter')]

blinky = Ghost(RED, 'chase')
pinky = Ghost(PINK, 'ambush')
inky = Ghost(CYAN, 'random')
clyde = Ghost(ORANGE, 'scatter')

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



def text_objects(text, font):
    text_surface = font.render(text, True, WHITE)
    return text_surface, text_surface.get_rect()

def quit_game():
    pygame.quit()
    sys.exit()

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

def restart_game():
    print ("restart")
    global score, pacman_x, pacman_y, powered_up, power_up_timer, pellet_timer, power_pellet_timer, ghost_eaten_timer, game_over, lives
    score = 0
    pacman_x = 12 * cell_size + cell_size // 2
    pacman_y = 17 * cell_size + cell_size // 2
    powered_up = False
    power_up_timer = 0
    pellet_timer = 0
    power_pellet_timer = 0
    ghost_eaten_timer = 0
    game_over = False  # Reset game_over to False
    lives = 3
    for ghost in ghosts:
        ghost.x, ghost.y = ghost.find_valid_start_position()


def draw_button_text(text, font):
    text_surface = font.render(text, True, WHITE)
    return text_surface, text_surface.get_rect()

# Inside the game over loop


while game_over:
    restart_button_text, restart_button_rect = draw_button_text("Restart", font)
    restart_button_rect.center = (screen_width // 2, screen_height // 2 + 60)
    quit_button_text, quit_button_rect = draw_button_text("Quit", font)
    quit_button_rect.center = (screen_width // 2, screen_height // 2 + 120)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if restart_button_rect.collidepoint(mouse_pos):
                restart_game()
                game_over = False
            elif quit_button_rect.collidepoint(mouse_pos):
                quit_game()
                print("Quit")
            screen.fill((0, 0, 0))
    print("Screen.fill")
    game_over_text = font.render("Game Over!", True, WHITE)
    screen.blit(game_over_text, (screen_width // 2 - 80, screen_height // 2 - 20))
    final_score_text = font.render("Final Score: " + str(score), True, WHITE)
    screen.blit(final_score_text, (screen_width // 2 - 100, screen_height // 2 + 20))
    restart_button_text = font.render("Restart", True, WHITE)
    draw_button("Restart", screen_width // 2 - 50, screen_height // 2 + 60, 100, 40, BLUE, GREEN, restart_game)
    quit_button_text = font.render("Quit", True, WHITE)
    draw_button("Quit", screen_width // 2 - 50, screen_height // 2 + 120, 100, 40, BLUE, GREEN, quit_game)
    pygame.display.flip()
    screen.fill((0, 0, 0))
    screen.blit(game_over_text, (screen_width // 2 - 80, screen_height // 2 - 20))
    screen.blit(final_score_text, (screen_width // 2 - 100, screen_height // 2 + 20))
    screen.blit(restart_button_text, restart_button_rect)
    screen.blit(quit_button_text, quit_button_rect)
    pygame.display.flip()

    
    
# Main game loop
# Main game loop
while True:
    
    running = True
    while running:
        # Displaying the high score

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Clear the screen
        screen.fill((0, 0, 0))

    
        
        # Draw the maze
        for row_index, row in enumerate(maze):
            for col_index, cell in enumerate(row):
                if cell == 1:
                    pygame.draw.rect(screen, BLUE, (col_index * cell_size, row_index * cell_size, cell_size, cell_size))
                elif cell == 2:  # Pellet
                    pygame.draw.circle(screen, WHITE, (col_index * cell_size + cell_size // 2, row_index * cell_size + cell_size // 2), 5)
                elif cell == 3:  # Power Pellet
                    pygame.draw.circle(screen, YELLOW, (col_index * cell_size + cell_size // 2, row_index * cell_size + cell_size // 2), 10)
                elif cell == GHOST_HOUSE:  # Ghost house
                    pygame.draw.rect(screen, GREEN, (col_index * cell_size, row_index * cell_size, cell_size, cell_size))

        # Handle Pac-Man movement
        keys = pygame.key.get_pressed()
        dx, dy = 0, 0
        if keys[pygame.K_LEFT]:
            dx -= pacman_speed
            pacman_direction = 'left'
        elif keys[pygame.K_RIGHT]:
            dx += pacman_speed
            pacman_direction = 'right'
        elif keys[pygame.K_UP]:
            dy -= pacman_speed
            pacman_direction = 'up'
        elif keys[pygame.K_DOWN]:
            dy += pacman_speed
            pacman_direction = 'down'
            
        if maze[pacman_y // cell_size][pacman_x // cell_size] == 1:
            pacman_x = max(0, min(pacman_x, screen_width - cell_size))
            pacman_y = max(0, min(pacman_y, screen_height - cell_size))



        # Calculate the new position
        new_x = pacman_x + dx
        new_y = pacman_y + dy

        # Check for wall collisions
        if maze[int(new_y // cell_size)][int(new_x // cell_size)] != 1:
            pacman_x = new_x
            pacman_y = new_y

        # Prevent Pac-Man from moving out of bounds
        pacman_x = max(cell_size // 2, min(pacman_x, screen_width - cell_size // 2))
        pacman_y = max(cell_size // 2, min(pacman_y, screen_height - cell_size // 2))

        # Update grid position
        grid_x = int(pacman_x // cell_size)
        grid_y = int(pacman_y // cell_size)

        # Draw Pac-Man with mouth animation
        rotated_pacman = pygame.transform.rotate(pacman_img, {
            'left': 180,
            'right': 0,
            'up': 90,
            'down': 270
        }[pacman_direction])
        screen.blit(rotated_pacman, (pacman_x - cell_size // 2, pacman_y - cell_size // 2))
        
        if maze[grid_y][grid_x] == 3:  # Check if Pac-Man overlaps with a power pellet
            maze[grid_y][grid_x] = 0  # Remove the power pellet
            powered_up = True  # Set powered up flag
            power_up_timer = POWER_UP_DURATION  # Set the duration of the power-up
            for ghost in ghosts:
                ghost.flashing = True  # Make the ghosts start flashing

        for ghost in ghosts:
            distance = ((pacman_x - ghost.x) ** 2 + (pacman_y - ghost.y) ** 2) ** 0.5
            if distance < cell_size:  # Adjust threshold as needed
                if powered_up:
                    # Pac-Man eats the ghost
                    ghost.x, ghost.y = ghost.find_valid_start_position()  # Reset ghost to start position
                    score += 200  # Increase score
                    eat_ghost_sound.play()  # Play eating sound effect
                    # Implement a delay before the ghost re-enters the game, if desired
                else:
                    # Game over logic
                    lives -= 1
                    if lives <= 0:
                        game_over = True
                        game_over_sound.play()  # Play game over sound effect
                    else:
                        # Reset Pac-Man and ghosts to initial positions
                        pacman_x, pacman_y = 12 * cell_size + cell_size // 2, 17 * cell_size + cell_size // 2
                        for ghost in ghosts:
                            ghost.x, ghost.y = ghost.find_valid_start_position()
                        pygame.time.delay(1000)  # Pause briefly after collision


         
        # Check for pellet consumption
        if 0 <= grid_x < num_cols and 0 <= grid_y < num_rows:
            cell_value = maze[grid_y][grid_x]
            if cell_value == 2:  # Regular pellet
                maze[grid_y][grid_x] = 0
                score += 10  # Increase score by 10 for regular pellets
                if pellet_timer == 0:
                    pellet_sound.play()
                    pellet_timer = 10  # Adjust timing
            elif cell_value == 3:  # Power pellet
                maze[grid_y][grid_x] = 0
                score += 50  # Increase score by 50 for power pellets
                powered_up = True
                power_up_timer = 300  # Set the power-up timer
                if power_pellet_timer == 0:
                    power_pellet_sound.play()
                    power_pellet_timer = 10  # Adjust timing

        for ghost in ghosts:
            distance = ((pacman_x - ghost.x) ** 2 + (pacman_y - ghost.y) ** 2) ** 0.5
            if distance < cell_size:  # Adjust threshold as needed
                # Pac-Man collides with ghost
                lives -= 1
                if lives == 0:
                    # Game over
                    game_over = True
                else:
                    # Reset Pac-Man and ghosts to initial positions
                    pacman_x, pacman_y = 12 * cell_size + cell_size // 2, 17 * cell_size + cell_size // 2
                    for ghost in ghosts:
                        ghost.x, ghost.y = ghost.find_valid_start_position()
                    pygame.time.delay(1000)  # Pause briefly after collision

            ghost.move()
            ghost.draw(screen)
            if powered_up and abs(pacman_x - ghost.x) < cell_size // 2 and abs(pacman_y - ghost.y) < cell_size // 2:
                ghosts.remove(ghost)
                eat_ghost_sound.play()
                if ghost_eaten_timer == 0:
                    eat_ghost_sound.play()
                    ghost_eaten_timer = 10  # Adjust timing
                score += 200  # Increase score for eating ghost

        # Check for collisions with ghosts
        for ghost in ghosts:
            if abs(ghost.x - pacman_x) < cell_size // 2 and abs(ghost.y - pacman_y) < cell_size // 2:
                if powered_up:
                    score += 200
                    ghost.x, ghost.y = ghost.find_valid_start_position()
                    powered_up = False
                    ghost_eaten_timer = pygame.time.get_ticks()
                    eat_ghost_sound.play()
                else:
                    # Game over
                    lives -= 1
                    if lives <= 0:
                        game_over = True
                        game_over_sound.play()
                    else:
                        pacman_x = 12 * cell_size + cell_size // 2
                        pacman_y = 17 * cell_size + cell_size // 2

        # Timer countdown for sound effects
        if pellet_timer > 0:
            pellet_timer -= 1
        if power_pellet_timer > 0:
            power_pellet_timer -= 1
        if ghost_eaten_timer > 0:
            ghost_eaten_timer -= 1

        lives_text = font.render("High Score: " + str(high_score), True, WHITE)
        screen.blit(lives_text, (50, 10))

        # Draw score
        score_text = font.render("Score: " + str(score), True, WHITE)
        screen.blit(score_text, (10, 10))

        # Draw lives
        lives_text = font.render("Lives: " + str(lives), True, WHITE)
        screen.blit(lives_text, (screen_width - 100, 10))

        # Update the display
        pygame.display.flip()

        # Check for game over condition
        if game_over:
            # Display game over screen
            while game_over:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_pos = pygame.mouse.get_pos()
                        if restart_button_rect.collidepoint(mouse_pos):
                            restart_game()
                            game_over = False
                        elif quit_button_rect.collidepoint(mouse_pos):
                            pygame.quit()
                            sys.exit()

                screen.fill((0, 0, 0))
                game_over_text = font.render("Game Over!", True, WHITE)
                screen.blit(game_over_text, (screen_width // 2 - 80, screen_height // 2 - 20))
                final_score_text = font.render("Final Score: " + str(score), True, WHITE)
                screen.blit(final_score_text, (screen_width // 2 - 100, screen_height // 2 + 20))
                restart_button_text = font.render("Restart", True, WHITE)
                quit_button_text = font.render("Quit", True, WHITE)
                restart_button_rect = restart_button_text.get_rect(center=(screen_width // 2, screen_height // 2 + 60))
                quit_button_rect = quit_button_text.get_rect(center=(screen_width // 2, screen_height // 2 + 120))
                screen.blit(restart_button_text, restart_button_rect)
                screen.blit(quit_button_text, quit_button_rect)
                lives_text = font.render("High Score: " + str(high_score), True, WHITE)
                screen.blit(lives_text, (50, 10))
                pygame.display.flip()
                if score > high_score:
                    high_score = score
            # Optionally, display a message or animation celebrating the new high score
        # Save the high score to a file
                    with open("high_score.txt", "w") as f:
                        f.write(str(high_score))
                        high_score_text = font.render("High Score: " + str(high_score), True, WHITE)
                        screen.blit(high_score_text, (300, 200))
                

