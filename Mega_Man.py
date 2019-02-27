import pygame
import Sprite_Sheet
import Settings
vector = pygame.math.Vector2

class Player(pygame.sprite.Sprite):
    def __init__(self,x,y): # The self class used for the player "Mega-Man"
        super().__init__()
        self.move_x = 5 # The x moving section
        self.move_y = 5 # The y moving section for jumping
        # Arrays used to store the sprites for each animation moment
        self.moving_left = []
        self.moving_right = []
        self.not_moving = []
        self.direction = "Right"    # Start the game off moving to the right like traditional megaman
        self.shooting = "False"
        # All of the sprites where mega man is facing to the right
        sprite_sheet = Sprite_Sheet.SpriteSheet("mega_man_sprite_sheet.png")

        image = sprite_sheet.get_image(150, 0, 50, 50)
        self.moving_right.append(image)
        image = sprite_sheet.get_image(200, 0, 50, 50)
        self.moving_right.append(image)
        image = sprite_sheet.get_image(250, 0, 50, 50)
        self.moving_right.append(image)

        # All of the sprites where mega man is facing to the left

        image = sprite_sheet.get_image(150, 0, 50, 50)
        image = pygame.transform.flip(image, True, False)
        self.moving_left.append(image)
        image = sprite_sheet.get_image(200, 0, 50, 50)
        image = pygame.transform.flip(image, True, False)
        self.moving_left.append(image)
        image = sprite_sheet.get_image(250, 0, 50, 50)
        image = pygame.transform.flip(image, True, False)
        self.moving_left.append(image)

        # Not moving sprite indicator
        image = sprite_sheet.get_image(0,0,50,50)
        self.not_moving.append(image)

        # Need to different not moving images one for the left and one for the right
        image = sprite_sheet.get_image(0,0,50,50)
        image = pygame.transform.flip(image, True, False)
        self.not_moving.append(image)

        # Shooting sprites
        image = sprite_sheet.get_image(100,50,50,50)
        self.not_moving.append(image)
        image = sprite_sheet.get_image(100,50,50,50)
        image = pygame.transform.flip(image, True, False)
        self.not_moving.append(image)


        # sprite to start with
        self.image = self.not_moving[0]
        self.rect = self.image.get_rect()


    def update(self):   #This section will blit the correct sprite to the screen depending on which way megaman is moving and or if he is moving
        pos = self.rect.x


        if self.direction == "Right":
            frame = (pos // 30) % len(self.moving_right)
            self.image = self.moving_right[frame]

        elif self.direction == "Left":
            frame = (pos // 30) % len(self.moving_left)
            self.image = self.moving_left[frame]

        elif self.direction == "None-right":
            if self.shooting == "False":
                self.image = self.not_moving[0]
            elif self.shooting == "True":
                self.image = self.not_moving[2]


        elif self.direction == "None-left":
            if self.shooting == "False":
                self.image = self.not_moving[1]
            elif self.shooting == "True":
                self.image = self.not_moving[3]
