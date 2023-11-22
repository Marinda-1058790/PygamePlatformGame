import pygame
from pygame.locals import *
import os

pygame.init()

clock = pygame.time.Clock()
fps = 240

# draw screen
screen_width = 800
screen_height = 800


screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('The Blue Alien')

# define game variables
tile_size = 40
game_over = 0
main_menu = True
milisecs = 0
secs = 0
mins = 0
score = 0

time = [{mins}, {secs}, {milisecs}]

# save highscore in file
if os.path.exists('score.txt'):
    with open('score.txt', 'r') as file:
        high_score = int(file.read())
else:
    high_score = 80


# load images
planet_1_img = pygame.image.load('images/planet_1.png')
planet_2_img = pygame.image.load('images/planet_2.png')
planet_3_img = pygame.image.load('images/planet_3.png')
planet_4_img = pygame.image.load('images/planet_4.png')
background_img = pygame.image.load('images/Background_image.png')
restart_img = pygame.image.load('images/Restart.png')
start_img = pygame.image.load('images/Start_2.png')
quit_img = pygame.image.load('images/Quit_2.png')
logo_img = pygame.image.load('images/Logo.PNG')

# function for drawing High score

#       Marinda
class Button:
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.clicked = False

    def draw(self):
        action = False

#       get mouse position
        pos = pygame.mouse.get_pos()
        
#       check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                action = True
                self.clicked = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
                
#        draw button
        screen.blit(self.image, self.rect)

        return action

#       Yamal


class Portal:
    def __init__(self, x, y):

        self.images_portal = []
        self.index = 0
        self.counter = 0
        for num in range(1, 5):
            img_portal = pygame.image.load(f'images/Portal_{num}.png')
            img_portal = pygame.transform.scale(img_portal, (120, 120))
            self.images_portal.append(img_portal)
        self.image = self.images_portal[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()

#       Draw portal onto screen
    def update(self):

        screen.blit(self.image, self.rect)

#            Charaylis

# if game_over == 0:
#     cupcake_running = True
#     while True:
class Cupcake(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('images/Cupcake_1.png')
        self.image = pygame.transform.scale(img, (60 // 2, 60 // 2))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

 
                    

#           Yamal


class Player:
    def __init__(self, x, y):
        #           Marinda
        self.reset(x, y)

#            Aron
    def update(self, game_over):

        dx = 0
        dy = 0
        walk_cooldown = 3

        if game_over == 0:
            #       get keypresses
            key = pygame.key.get_pressed()
            if key[pygame.K_SPACE] and self.jumped == False and self.in_air == False:
                self.vel_y = - 67
                self.jumped = True
            if key[pygame.K_SPACE] is False:
                self.jumped = False
#                multiplided by 3 because of framerate.
            if key[pygame.K_LEFT]:
                dx -= 16
                self.counter += 1
                self.direction = -1
            if key[pygame.K_RIGHT]:
                dx += 16
                self.counter += 1
                self.direction = 1
            if key[pygame.K_LEFT] is False and key[pygame.K_RIGHT] is False:
                self.counter += 1
                self.direction = 0

#       reset animation
        if self.counter > walk_cooldown:
            self.counter = 0
            self.index += 1
            if self.index >= len(self.images_right):
                self.index = 0
#            adding directional sprites for keypresses
            if self.direction == 1:
                self.image = self.images_right[self.index]
            if self.direction == -1:
                self.image = self.images_left[self.index]
            if self.direction == 0:
                self.image = self.images_idle[self.index]


#            add gravity (made bigger because of frame rate)
            self.vel_y += 17
            if self.vel_y > 2:
                self.vel_y = 20

            dy += self.vel_y


#           check for collision made with the help from the tutorial stated on line 5
            self.in_air = True
            for tile in world.tile_list:
                # check for collision in x direction
                if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                    dx = 0
#                check for collision in y direction
                if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                    # check if below the ground i.e. jumping
                    if self.vel_y < 0:
                        dy = tile[1].bottom - self.rect.top
                        self.vel_y = 0
#                    check if above the ground i.e. falling
                    elif self.vel_y >= 0:
                        dy = tile[1].top - self.rect.bottom
                        self.vel_y = 0
                        self.in_air = False

            if self.rect.bottom > screen_height:
                game_over = -1

                print(game_over)
            
#            collision with spaceship Celeste
            collision_with_spaceship = pygame.sprite.spritecollide(self, spaceship_group, False)
            if collision_with_spaceship:
                #           show win text
                font = pygame.font.SysFont('didot.ttc', 100)
                img = font.render('CONGRATULATIONS!', True, (0, 250, 0))
                screen.blit(img, (37, 300)), quit_button.draw(), restart_button.draw()
                dx = 0
                dy = 0
                game_over = 1

#            update player coordinates
            self.rect.x += dx
            self.rect.y += dy

        elif game_over == -1:
            self.image = self.dead_image
            if self.rect.y > 400:
                self.rect.y -= 2

        elif game_over == 1:
            self.image = self.rocket_image
            self.rect.y -= 2

#        draw player onto screen
        screen.blit(self.image, self.rect)

        return game_over

#            Marinda
    def reset(self, x, y):

        # Yamal

        self.images_right = []
        self.images_left = []
        self.images_idle = []
        self.index = 0
        self.counter = 0
#        loading animation images into lists
        for num in range(1, 6):
            img_right = pygame.image.load(f'images/PlayerAnimations/R{num}.png')
            img_right = pygame.transform.scale(img_right, (30, 40))
            img_left = pygame.transform.flip(img_right, True, False)
            self.images_right.append(img_right)
            self.images_left.append(img_left)
        for num in range(1, 8):
            img_idle = pygame.image.load(f'images/PlayerAnimations/Idle{num}.png')
            img_idle = pygame.transform.scale(img_idle, (30, 40))
            self.images_idle.append(img_idle)
        self.image = self.images_idle[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.dead_image = pygame.image.load('images/Ghost.png')
        self.rocket_image = pygame.image.load('images/Spaceship_takeoff_1.png')
        self.rocket2_image = pygame.image.load('images/Spaceship_takeoff_2.png')
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.vel_y = 0
        self.jumped = False
        self.direction = 0


#           Yamal
#           Charaylis ( self.create_scene)
class World:
    def __init__(self, data):

        self.tile_list = []

        self.data = data
#        load images
        self.frame_img = pygame.image.load('images/Border_image.png')
        self.terrain_img = pygame.image.load('images/Platform_1.png')
        self.floor_img = pygame.image.load('images/Platform_2.png')
        self.create_scene()

    def create_scene(self):
        row_count = 0
        for row in self.data:
            col_count = 0
            for tile in row:
                if tile == 1:
                    img = pygame.transform.scale(self.frame_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 2:
                    img = pygame.transform.scale(self.floor_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 3:
                    img = pygame.transform.scale(self.terrain_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
#               Celeste
                if tile == 4:
                    spaceship = Spaceship(col_count * tile_size, row_count * tile_size)
                    spaceship_group.add(spaceship)
                if tile == 5:
                    cupcake = Cupcake(col_count * tile_size + (tile_size // 2),  row_count * tile_size + (tile_size // 2))
                    cupcake_group.add(cupcake)
                col_count += 1
            row_count += 1

    def draw(self):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])

#            Celeste


class Spaceship(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('images/Spaceship_empty.png')
        self.image = pygame.transform.scale(img, (120, 120))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()


spaceship_group = pygame.sprite.Group()


cupcake_group = pygame.sprite.Group()

#            Yamal

world_data = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 1],
    [1, 0, 0, 3, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0, 5, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 1],
    [1, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 1],
    [1, 3, 3, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 3, 0, 0, 1],
    [1, 0, 0, 0, 3, 0, 0, 0, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 3, 3, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 1],
    [1, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 0, 1],
    [1, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 3, 3, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 3, 3, 0, 3, 0, 0, 0, 0, 0, 0, 3, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 1],
    [1, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 1],
    [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1]
]


world = World(world_data)

portal = Portal(40, screen_height - 200)

player = Player(80, screen_height - 160)

#            Marinda

# create buttons
restart_button = Button(screen_width // 2 - 335, screen_height // 2, restart_img)
start_button = Button(screen_width // 2 - 320, screen_height // 2, start_img)
quit_button = Button(screen_width // 2 + 80, screen_height // 2, quit_img)

run = True
while run:

    clock.tick(fps)

#           Yamal
    screen.blit(background_img, (0, 0))
    screen.blit(planet_1_img, (400, 400))
    screen.blit(planet_2_img, (100, 100))
    screen.blit(planet_3_img, (200, 600))
    screen.blit(planet_4_img, (400, 700))

    font = pygame.font.Font(None, 40)
    text = font.render(f'HIGH SCORE: {high_score}', True, (255, 255, 255), (0, 0, 0))

#            Marinda
    if main_menu is True:
        screen.blit(logo_img, (200, 100))
        screen.blit(text, (300, 650))
        if quit_button.draw():
            run = False
        if start_button.draw():
            main_menu = False

    else:
        world.draw()
#         draw spaceship onto screen
        spaceship_group.draw(screen)

        # draw cupcake onto screen
        cupcake_group.draw(screen)

#          Celeste
#       add time to the game
        font = pygame.font.Font(None, 40)
        text = font.render("{}:{}".format(mins, secs, milisecs), True, (0, 250, 0), (0, 0, 0))
        textRect = text.get_rect()
        textRect.topleft = 10, 10

        clock.tick(60)
        if game_over == 0:
            milisecs += 1
            screen.blit(text, textRect)
            if milisecs == 60:
                milisecs = 0
                secs += 1
            if secs == 60:
                secs = 0
                milisecs = 0
                mins += 1
            text = font.render("{},{},{}".format(mins, secs, milisecs), True, (0, 250, 0), (0, 0, 0))
            time = secs
            if secs > 0:
                score = time

        font = pygame.font.Font(None, 40)
        text = font.render(f'HIGH SCORE: {high_score}', True, (0, 250, 0), (0, 0, 0))
        textRect = text.get_rect()
        screen.blit(text, (550, 10))

        if pygame.sprite.spritecollide(player, cupcake_group, True):
            secs -= 2

        portal.update()

        game_over = player.update(game_over)

#        if player has died
        if game_over == -1:
            font = pygame.font.SysFont('didot.ttc', 100)
            img = font.render('GAME OVER!', True, (255, 0, 0))
            screen.blit(img, (175, 250))
            secs = 0
            mins = 0
            hours = 0

#           Marinda
#           Charaylis ( world.create_scene)
            if quit_button.draw():
                run = False
            if restart_button.draw():
                player.reset(80, screen_height - 160)
                game_over = 0
                world.create_scene()
            
            
#        if player has completed the level
        if game_over == 1:
            font = pygame.font.SysFont('didot.ttc', 100)
            img = font.render('CONGRATULATIONS!', True, (0, 250, 0))
            font = pygame.font.SysFont('didot.ttc', 35)
            img2 = font.render(f'Your time is {"{}".format(mins)} minutes & {"{}".format(secs)} seconds', True, (0, 250, 0))
            screen.blit(img, (37, 300))
            screen.blit(img2, (200,  400))


#            update high score

            if score < high_score:
                high_score = score
                with open('score.txt', 'w') as file:
                    file.write(str(high_score))

                    print(high_score)

            if quit_button.draw():
                run = False
            if restart_button.draw():
                player.reset(80, screen_height - 160)
                game_over = 0
                secs = 0
                mins = 0
                hours = 0
                world.create_scene()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
