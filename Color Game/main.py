import pygame, sys, random

pygame.init()
CLOCK = pygame.time.Clock()
FPS = 60
W, H = 900, 600
SCREEN = pygame.display.set_mode((W, H)) # make pygame window
TITLE = pygame.display.set_caption("Color Game")
ICON = pygame.image.load("assets\images\icon.png")
pygame.display.set_icon(ICON)


colors = {
    "white" : (255, 255, 255),
    "gray" : (20, 20, 20),
    "lightgray" : (150, 150, 150),
    "black" : (0, 0, 0),

    "red": (255, 0, 0),
    "orange": (255, 95, 31),
    "yellow": (255, 255, 0),
    "green": (0, 255, 0),
    "blue": (0, 0, 255),
    "purple": (128, 0, 128),
    "pink": (255, 0, 255)
}

colors_inv = dict(map(reversed, colors.items()))


user_text = ""
mistakes = 0
time = 10

colors_list = ["red", "orange", "yellow", "green", "blue", "purple", "pink"]
for i in range(len(colors_list)):
    colors_list[i] = colors_list[i].upper()

font = pygame.font.Font("assets\\fonts\consolas.ttf", 20)
font_mid = pygame.font.Font("assets\\fonts\consolas.ttf", 32)
font_big = pygame.font.Font("assets\\fonts\consolas.ttf", 48)
info_text_surf = font.render("Enter the color of the text: ", True, colors["lightgray"])
info_text_rect = info_text_surf.get_rect(center = (W/2, H/4))
time_text_surf = font.render("Time:", True, colors["white"])
time_text_rect = time_text_surf.get_rect(midbottom = (W/2, H - 24))

game_over_text_surf = font_big.render("GAME OVER!", True, colors["white"])
game_over_text_rect = game_over_text_surf.get_rect(midbottom = (W/2, H/2))
restart_text_surf = font.render("Press Enter to play again", True, colors["lightgray"])
restart_text_rect = restart_text_surf.get_rect(midtop = (W/2, H/2))

x_surf = pygame.transform.scale(pygame.image.load("assets\\images\\x.png"), (60, 60))


class Timebar:
    def __init__(self):
        self.width = 0
        self.height = 18
        self.surf = pygame.surface.Surface((W, self.height))
        self.surf.fill(colors["white"])
        self.rect = self.surf.get_rect(bottomright = (W, H))
    
    def draw(self): # both drawing and animating
        if self.rect.left < W:
            self.rect.left += (W/time) / FPS
        else:
            global mistakes
            mistakes += 1

        SCREEN.blit(self.surf, self.rect)
        pygame.draw.aaline(SCREEN, colors["white"], (0, H-self.height), (W, H-self.height))
timebar = Timebar()

class Score:
    def __init__(self):
        self.value = 0
        self.surf = font.render("Score:", True, colors["white"])
        self.rect = self.surf.get_rect(midbottom = (W/10*9, H/2 - 48))
        self.value_surf = font_mid.render(str(self.value), True, colors["white"])
        self.value_rect = self.value_surf.get_rect(midtop = (self.rect.midbottom))

    def draw(self):
        self.value_surf = font_mid.render(str(self.value), True, colors["white"])
        SCREEN.blit(self.surf, self.rect)
        SCREEN.blit(self.value_surf, self.value_rect)
score = Score()


def def_main_text():
    global color2, main_text_rect
    color1 = colors_list[random.choice(range(len(colors_list)))]
    color2 = colors[colors_list[random.choice(range(len(colors_list)))].lower()]

    main_text_surf = font_big.render(color1, True, color2)
    main_text_rect = main_text_surf.get_rect(midbottom = (W/2, H/2))

    info_text_rect.bottom = main_text_rect.top - 10

    return main_text_surf, main_text_rect

def gameover():
    global mistakes, time
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    mistakes = 0
                    time = 10
                    timebar.rect.left = 0
                    main()
            
        SCREEN.fill(colors["gray"])

        score.draw()

        x1_rect = (x_surf.get_rect(center = (W/10, H/2 - 24))) # mid
        x2_rect = (x_surf.get_rect(midbottom = x1_rect.midtop)) # top
        x3_rect = (x_surf.get_rect(midtop = x1_rect.midbottom)) # bottom
        SCREEN.blit(x_surf, x1_rect)
        SCREEN.blit(x_surf, x2_rect)
        SCREEN.blit(x_surf, x3_rect)

        SCREEN.blit(game_over_text_surf, game_over_text_rect)
        SCREEN.blit(restart_text_surf, restart_text_rect)
    
        CLOCK.tick(FPS)
        pygame.display.update()

def main():
    global user_text, mistakes, time
    main_text = def_main_text()
    FPS_count = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                else:
                    user_text += event.unicode
                if event.key == pygame.K_RETURN:
                    if not str(user_text[:-1].lower()) == str(colors_inv[color2]):
                        mistakes += 1
                    else:
                        score.value += 1
                        time = round(time - 0.4 , 1)
                        print(time)

                    user_text = ""
                    timebar.rect.left = 0
                    main_text = def_main_text()

        SCREEN.fill(colors["gray"])
        SCREEN.blit(info_text_surf, info_text_rect)
        SCREEN.blit(time_text_surf, time_text_rect)
        SCREEN.blit(main_text[0], main_text[1])

        user_text_surf = font_mid.render(str(user_text.upper()), True, colors["white"])
        user_text_rect = user_text_surf.get_rect(midtop = (W/2, H/2))
        SCREEN.blit(user_text_surf, user_text_rect)

        timebar.draw()
        score.draw()

        # lets call it type cursor for example
        if FPS_count < FPS/2:
            pygame.draw.aaline(SCREEN, colors["white"], user_text_rect.topright, user_text_rect.bottomright)

        if mistakes == 1:
            x_rect = x_surf.get_rect(center = (W/10, H/2 - 24))
            SCREEN.blit(x_surf, x_rect)
        if mistakes == 2:
            x1_rect = x_surf.get_rect(midbottom = (W/10, H/2 - 5 - 24)) # top
            x2_rect = x_surf.get_rect(midtop = (W/10, H/2 + 5 - 24)) # bottom
            SCREEN.blit(x_surf, x1_rect)
            SCREEN.blit(x_surf, x2_rect)
        if mistakes >= 3:
            gameover()


        FPS_count += 1 
        if FPS_count >= FPS:
            FPS_count = 0

        CLOCK.tick(FPS)
        pygame.display.update()

main()