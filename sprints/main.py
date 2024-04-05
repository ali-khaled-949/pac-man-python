import pygame
import sys
import random
import heapq


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
# Assuming you have a 'maze' variable that represents your maze layout
# and that you've defined starting positions for each ghost
cell_size = 40
screen_width = len(maze[0]) * cell_size
screen_height = len(maze) * cell_size


# Create instances of Ghost with the necessary arguments


# Add them to your ghosts list


# Set colors
WHITE = (255, 255, 255)
BLUE = (33, 33, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
PINK = (255, 105, 180)  # RGB for Pink
ORANGE = (255, 165, 0)  # RGB for Orange
# Calculate maze dimensions
num_rows = len(maze)
num_cols = len(maze[0])

# Set cell size

# Calculate window size
#screen_width = num_cols * cell_size
#screen_height = num_rows * cell_size

# Set up the display
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pac-Man")

# Score
score = 0
font = pygame.font.SysFont("arial", 24)
WHITE, BLUE, RED, YELLOW, PINK, ORANGE = ...

# Load Pac-Man image
pacman_img = pygame.image.load('pacman-icon.png').convert_alpha()
pacman_img = pygame.transform.scale(pacman_img, (cell_size, cell_size))
pacman_x, pacman_y, pacman_speed, pacman_direction = 12 * cell_size, 17 * cell_size, 1, 'right'

# Initialize Pac-Man position and speed
pacman_x = 12 * cell_size + cell_size // 2
pacman_y = 17 * cell_size + cell_size // 2
pacman_speed = 1

pacman_direction = 'right'



# Define Ghost class
class Ghost:
    def __init__(self, color, start_pos, maze):
        self.color, self.x, self.y, self.maze, self.direction, self.speed = color, start_pos[0], start_pos[1], maze, 'left', 2
#        self.color = color
 #       self.x, self.y = start_pos
  #      self.maze = maze
   #     self.direction = 'left'
    #    self.speed = 2

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), cell_size // 2)

    def move(self):
        # Basic movement logic, can be overridden or extended in subclasses
        next_x, next_y = self.calculate_next_position()
        if self.is_valid_move(next_x, next_y):
            self.x = next_x
            self.y = next_y
        else:
            self.change_direction_randomly()

    def calculate_next_position(self):
        if self.direction == 'up':
            return self.x, self.y - self.speed
        elif self.direction == 'down':
            return self.x, self.y + self.speed
        elif self.direction == 'left':
            return self.x - self.speed, self.y
        elif self.direction == 'right':
            return self.x + self.speed, self.y

    def is_valid_move(self, x, y):
        if x < 0 or x >= screen_width or y < 0 or y >= screen_height:
            return False
        cell_type = self.maze[y // cell_size][x // cell_size]
        return cell_type != 1  # 1 represents wall

    def change_direction_randomly(self):
        self.direction = random.choice(['up', 'down', 'left', 'right'])
        
    def is_collision_with_pacman(self, pacman_x, pacman_y):
        # Calculate the distance between the ghost and Pac-Man
        distance = ((self.x - pacman_x) ** 2 + (self.y - pacman_y) ** 2) ** 0.5

        # Define a threshold for collision, for example, half the cell size
        collision_threshold = cell_size / 2

        # Check if the distance is less than the collision threshold
        return distance < collision_threshold

class Blinky(Ghost):
    def move(self, pacman_x, pacman_y, blinky_pos=None, pacman_direction=None):
        # Direct chase strategy: Move towards Pac-Man's current position
        if self.x < pacman_x:  # Pac-Man is to the right
            self.x += self.speed
        elif self.x > pacman_x:  # Pac-Man is to the left
            self.x -= self.speed

        if self.y < pacman_y:  # Pac-Man is below
            self.y += self.speed
        elif self.y > pacman_y:  # Pac-Man is above
            self.y -= self.speed

    def is_collision_with_pacman(self, pacman_x, pacman_y):
        # Collision detection logic specific to Blinky
        distance = ((self.x - pacman_x)**2 + (self.y - pacman_y)**2)**0.5
        return distance < (cell_size / 2)

class Pinky(Ghost):
    def move(self, pacman_x, pacman_y, pacman_direction):
        target_x, target_y = pacman_x, pacman_y
        
        # Pinky aims for 4 tiles in front of Pac-Man
        if pacman_direction == 'up':
            target_y -= 4 * cell_size
        elif pacman_direction == 'down':
            target_y += 4 * cell_size
        elif pacman_direction == 'left':
            target_x -= 4 * cell_size
        elif pacman_direction == 'right':
            target_x += 4 * cell_size
        
        # Simple chase towards the target
        if self.x < target_x:
            self.x += self.speed
        elif self.x > target_x:
            self.x -= self.speed

        if self.y < target_y:
            self.y += self.speed
        elif self.y > target_y:
            self.y -= self.speed
            
    def is_collision_with_pacman(self, pacman_x, pacman_y):
        # Collision detection logic specific to Pinky
        distance = ((self.x - pacman_x)**2 + (self.y - pacman_y)**2)**0.5
        return distance < (cell_size / 2)    

class Inky(Ghost):
    def move(self, pacman_x, pacman_y, blinky_x, blinky_y):
        # Inky's target is twice the vector from Blinky to 2 tiles in front of Pac-Man
        target_x = 2 * pacman_x - blinky_x
        target_y = 2 * pacman_y - blinky_y

        if self.x < target_x:
            self.x += self.speed
        elif self.x > target_x:
            self.x -= self.speed

        if self.y < target_y:
            self.y += self.speed
        elif self.y > target_y:
            self.y -= self.speed

class Clyde(Ghost):
    def move(self, pacman_x, pacman_y):
        distance = ((self.x - pacman_x) ** 2 + (self.y - pacman_y) ** 2) ** 0.5
        
        # Clyde chases if far from Pac-Man and scatters if too close
        if distance > 8 * cell_size:
            if self.x < pacman_x:
                self.x += self.speed
            elif self.x > pacman_x:
                self.x -= self.speed

            if self.y < pacman_y:
                self.y += self.speed
            elif self.y > pacman_y:
                self.y -= self.speed
        else:
            # Scatter to bottom-left corner
            if self.x > 0:
                self.x -= self.speed
            if self.y < screen_height - cell_size:
                self.y += self.speed

# Create ghosts
#ghosts = [Ghost(RED), Ghost(BLUE)]
# Example starting positions (you can choose appropriate ones based on your maze)
blinky_start_pos = (12 * cell_size, 17 * cell_size)  # Example position for Blinky
inky_start_pos = (14 * cell_size, 17 * cell_size)    # Example position for Inky

blinky = Blinky(RED, blinky_start_pos, maze)
inky = Inky(BLUE, inky_start_pos, maze)
pinky = Pinky(PINK, (12 * cell_size, 15 * cell_size), maze)  # You need to set Pinky's start pos
clyde = Clyde(ORANGE, (14 * cell_size, 15 * cell_size), maze)  # You need to set Clyde's start pos

ghosts = [blinky, inky, pinky, clyde]

# Main game loop
running = True
grid_x = pacman_x // cell_size
grid_y = pacman_y // cell_size

while running:
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

    # Handle Pac-Man movement with warp tunnels
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        pacman_direction = 'left'
    elif keys[pygame.K_RIGHT]:
        pacman_direction = 'right'
    elif keys[pygame.K_UP]:
        pacman_direction = 'up'
    elif keys[pygame.K_DOWN]:
        pacman_direction = 'down'


    if keys[pygame.K_LEFT]:
        pacman_x, pacman_y = 12 * cell_size, 17 * cell_size  # Initial position

        pacman_direction = 'left'
        
        score = 0
        
        if pacman_x - pacman_speed < 0:  # Warp tunnel on the left
            pacman_x = screen_width - cell_size  # Move to the right side
        elif maze[pacman_y // cell_size][(pacman_x - pacman_speed) // cell_size] != 1:
            pacman_x -= pacman_speed
    elif keys[pygame.K_RIGHT]:
        pacman_direction = 'right'
        if pacman_x + pacman_speed > screen_width:  # Warp tunnel on the right
            pacman_x = 0  # Move to the left side
        elif maze[pacman_y // cell_size][(pacman_x + pacman_speed) // cell_size] != 1:
            pacman_x += pacman_speed
    elif keys[pygame.K_UP]:
        pacman_direction = 'up'
        # Check if Pac-Man can move up
        if maze[(pacman_y - pacman_speed) // cell_size][pacman_x // cell_size] != 1:
            pacman_y -= pacman_speed
    elif keys[pygame.K_DOWN]:
        pacman_direction = 'down'
        # Check if Pac-Man can move down
        if maze[(pacman_y + pacman_speed) // cell_size][pacman_x // cell_size] != 1:
            pacman_y += pacman_speed

    # Update grid position
    grid_x = pacman_x // cell_size
    grid_y = pacman_y // cell_size

    rotated_pacman = pygame.transform.rotate(pacman_img, {
        'left': 180,
        'right': 0,
        'up': 90,
        'down': 270
    }[pacman_direction])
    screen.blit(rotated_pacman, (pacman_x - cell_size // 2, pacman_y - cell_size // 2))

    # Check for pellet consumption
    if 0 <= grid_x < num_cols and 0 <= grid_y < num_rows:
        cell_value = maze[grid_y][grid_x]
        if cell_value == 2:  # Regular pellet
            maze[grid_y][grid_x] = 0
            score += 10  # Increase score by 10 for regular pellets
        elif cell_value == 3:  # Power pellet
            maze[grid_y][grid_x] = 0
            score += 50  # Increase score by 50 for power pellets

    # Draw Pac-Man
    # screen.blit(pacman_img, (pacman_x - cell_size // 2, pacman_y - cell_size // 2))

    # Handle ghost movement
    for ghost in ghosts:
        if isinstance(ghost, Inky):
            # Pass Blinky's current position along with Pac-Man's position to Inky's move method
            ghost.move(pacman_x, pacman_y, blinky.x, blinky.y)
        else:
            ghost.move(pacman_x, pacman_y)  # For other ghosts that don't require Blinky's position
        ghost.draw(screen)


        if isinstance(ghost, Pinky):
            # Pass pacman_direction to Pinky's move method
            ghost.move(pacman_x, pacman_y, pacman_direction)
        else:
            # For other ghosts, not requiring pacman_direction
            ghost.move(pacman_x, pacman_y)  
        ghost.draw(screen)



        if ghost.is_collision_with_pacman(pacman_x, pacman_y):
            running = False  # Stop the game loop if collision detected
            
            


            
    # Display score on screen
    score_text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(score_text, (10, 10))  # Adjust position as needed

    # Update the display
    pygame.display.update()

# Cleanup
pygame.quit()

sys.exit()
