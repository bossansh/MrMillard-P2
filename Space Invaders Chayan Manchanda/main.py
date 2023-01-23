# Author: Chayan Manchanda                                                                   #
# Period - 2                                                                                 #
# Title: Space invaders                                                                      #
# Description: Basic space invaders game with different levels                               #
#                                                                                            #
#                                                                                            #
#                                                                                            #
#                                                                                            #
##############################################################################################




import pygame
import os
import time
import random


# The font object needs to be initialized
pygame.font.init()

WIDTH, HEIGHT = 1000, 900
# Pygame surfice
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")

# Load images
RED_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_red_small.png"))
GREEN_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_green_small.png"))
BLUE_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_blue_small.png"))

# Player ship
YELLOW_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_yellow.png"))

# Lasers
RED_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_red.png"))
GREEN_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_green.png"))
BLUE_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_blue.png"))
YELLOW_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_yellow.png"))

# Backgorund
BG =  pygame.transform.scale(pygame.image.load(os.path.join("assets", "background-black.png")), (WIDTH, HEIGHT))

class Laser:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)


    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

    
    def move(self, velocity):
        self.y += velocity

    
    def off_screen(self, height):
        return not(0 <= self.y <= height)  


    def collision(self, obj):
        return collide(self, obj)

def collide(obj1, obj2):
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None


def random_y_position():
    return random.randrange(-1500, -100)


def random_x_position():
    return random.randrange(50, WIDTH - 100)


def random_ship_color():
    return random.choice(["green", "blue", "red"])



class Ship:
    COOLDOWN = 30
    LASER_VELOCITY = 4
     
    def __init__(self, x_position, y_position, health=100):
        self.x = x_position
        self.y = y_position
        self.health = health
        self.ship_img = None
        self.laser_img = None
        self.lasers = []
        self.cool_down_counter = 0
    
    
    def draw(self, window):
        window.blit(self.ship_img, (self.x, self.y))
        for laser in self.lasers:
            laser.draw(window)


    def move_lasers(self, obj):
        self.cooldown()
        for laser in self.lasers:
            laser.move(self.LASER_VELOCITY)
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)
            elif laser.collision(obj):
                obj.health -= 10
                if laser in self.lasers:
                    self.lasers.remove(laser)

    def cooldown(self):
        if self.cool_down_counter >= self.COOLDOWN:
            self.cool_down_counter = 0
        else:
            self.cool_down_counter += 1
    
    def shoot(self):
        if self.cool_down_counter == 0:
            laser = Laser(self.x, self.y, self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 1


    def get_width(self):
        return self.ship_img.get_width()

   
    def get_height(self):
        return self.ship_img.get_height()


class Player(Ship):
    PLAYER_VELOCITY = 5
    LASER_VELOCITY = -10

    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.ship_img = YELLOW_SPACE_SHIP
        self.laser_img = YELLOW_LASER
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health = health
    
    def move_lasers(self, objs):
        self.cooldown()
        for laser in self.lasers:
            laser.move(self.LASER_VELOCITY)
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)
            else:
                for object in objs:
                    if laser.collision(object):
                        objs.remove(object)
                        if laser in self.lasers:
                            self.lasers.remove(laser)
    
    def draw(self, window):
        super().draw(window)
        self.health_bar(window)
    
    def health_bar(self, window):
        pygame.draw.rect(window, (255, 0, 0), (self.x, self.y + self.ship_img.get_height() + 10, self.ship_img.get_width(), 10))
        life_width = self.ship_img.get_width() * (self.health / self.max_health)
        pygame.draw.rect(window, (0, 255, 0), (self.x, self.y + self.ship_img.get_height() + 10, life_width, 10))
    

    def move_right(self):
        if self.x + self.PLAYER_VELOCITY > WIDTH:
            self.x = 0
        else:
            self.x += self.PLAYER_VELOCITY

    def move_left(self):
        if self.x - self.PLAYER_VELOCITY < 0:
            self.x = WIDTH
        else:
            self.x -= self.PLAYER_VELOCITY

    def move_up(self):
        if self.y - self.PLAYER_VELOCITY  > 0:
            self.y -= self.PLAYER_VELOCITY

    def move_down(self):
        if self.y + self.PLAYER_VELOCITY + self.get_height() + 20 < HEIGHT:
            self.y += self.PLAYER_VELOCITY



class Enemy(Ship):
    ENEMY_VELOCITY = 1
    

    COLOR_MAP = {
        "red": (RED_SPACE_SHIP, RED_LASER),
        "green": (GREEN_SPACE_SHIP, GREEN_LASER),
        "blue": (BLUE_SPACE_SHIP, BLUE_LASER)
    }

    def __init__(self, x, y, color, health=100):
        super().__init__(x, y, health)
        self.ship_img, self.laser_img = self.COLOR_MAP[color]
        self.mask = pygame.mask.from_surface(self.ship_img)

    
    def move(self):
        self.y += self.ENEMY_VELOCITY

    def shoot(self):
        if self.cool_down_counter == 0:
            laser = Laser(self.x - 20, self.y, self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 1


def main():
    run = True
    lost = False
    FPS = 60
    level = 0
    lives = 1
    main_font = pygame.font.SysFont("comicsans", 50)
    lost_font = pygame.font.SysFont("comicsans", 80)

    lost_count = 0
    
    enemies = []
    wave_length = 5
    
    player_ship = Player(300, 300)

    clock = pygame.time.Clock()


    
    def redraw_window():
        # Starts  with the BG to fill the others images
        WINDOW.blit(BG, (0, 0))
        # Draw text 
        lives_label = main_font.render(f"Lives: {lives}", 1, (255, 255, 255))
        level_label = main_font.render(f"Level: {level}", 1, (255, 255, 255))

        WINDOW.blit(lives_label, (10, 10))
        WINDOW.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))
        
        player_ship.draw(WINDOW)

        for enemy in enemies:
            enemy.draw(WINDOW)

        

        if lost:
            lost_label = lost_font.render("You lost!", 1, (255, 255, 255))
            x_center = (WIDTH - lost_label.get_width()) /2
            y_center = (HEIGHT - lost_label.get_height()) / 2
            WINDOW.blit(lost_label, (x_center, y_center))
        
        pygame.display.update()
    

    while run:
        clock.tick(FPS)
        redraw_window()

        if lives <= 0 or player_ship.health <= 0:
            lost = True
            lost_count += 1
        
        if lost:
            if lost_count > FPS * 3:
                run = False
            else:
                continue

        if len(enemies) == 0:
            level += 1
            wave_length += 5
            for i in range(wave_length):
                enemy_ship = Enemy(random_x_position(), random_y_position(), random_ship_color())

                enemies.append(enemy_ship)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               pygame.quit()

        keys = pygame.key.get_pressed() # returns a dict of all the keys and tells weather they're pressed or not at the current time
        
        if (keys[pygame.K_a] or keys[pygame.K_LEFT]): 
            player_ship.move_left()

        if (keys[pygame.K_d] or keys[pygame.K_RIGHT]): 
            player_ship.move_right()

        if (keys[pygame.K_w] or keys[pygame.K_UP]): 
            player_ship.move_up()

        if (keys[pygame.K_s] or keys[pygame.K_DOWN]):
            player_ship.move_down()
        
        if keys[pygame.K_SPACE]:
            player_ship.shoot()
        
        for enemy in enemies[:]:
            enemy.move()
            enemy.move_lasers(player_ship)
            
            if random.randint(0, 10) == 1:
                enemy.shoot()

            
            if collide(enemy, player_ship):
                player_ship.health -= 10
                enemies.remove(enemy)
            
            elif enemy.y + enemy.get_height() > HEIGHT:
                lives -= 1
                enemies.remove(enemy)
            

        player_ship.move_lasers(enemies)


def main_menu():
    run = True
    title_font = pygame.font.SysFont("comicsans", 70)
    
    while run:
        WINDOW.blit(BG, (0,0))
        title_label = title_font.render("Press the mouse to begin...", 1, (255,255,255))
        WINDOW.blit(title_label, ((WIDTH - title_label.get_width()) / 2, (HEIGHT - title_label.get_height()) / 2))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                main()
        
    pygame.quit()


main_menu()