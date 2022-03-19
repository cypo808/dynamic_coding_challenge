import pygame, sys, random, time

"""
TODO
wanted to add animation, but cant get it somehow...
"""

pygame.init()
CLOCK = pygame.time.Clock()
FPS = 60
W, H = 480, 640
SCREEN = pygame.display.set_mode((W, H)) # make pygame window
TITLE = pygame.display.set_caption("Dice Rolling Simulator")
#ICON = pygame.image.load("assets\images\icon.png")
#pygame.display.set_icon(ICON)

backgrounds = [(110, 68, 255),
    (241, 80, 37),
    (100, 49, 115),
    (26, 27, 37),
    (71, 59, 240)
]

colors = {
    "white" : (255, 255, 255),
    "gray" : (20, 20, 20),
    "black" : (0, 0, 0),
    "background" : backgrounds[random.randint(0, len(backgrounds)-1)]}


font = pygame.font.Font("assets\\fonts\\YellowCandy.otf", int(W/10))
font2 = pygame.font.Font("assets\\fonts\\YellowCandy.otf", int(W/20))
font3 = pygame.font.Font("assets\\fonts\\YellowCandy.otf", int(W/4))
text_surf = font.render("Dice Rolling Simulator", True, colors["white"])
text_rect = text_surf.get_rect(midtop = (W/2, H/8))
info_surf = font2.render("Press Space", True, colors["white"])
info_rect = info_surf.get_rect(midbottom = (W/2, H/8*6.6))
questionmark_surf = font3.render("?", True, colors["white"])
questionmark_rect = questionmark_surf.get_rect(center = (W/2, H/2))


class Dice():
    def __init__(self, size, center, width):
        self.size = size
        self.center = center
        self.centerx = self.center[0]
        self.centery = self.center[1]
        self.width = width
        self.value = None
        self.dotsize = 16


    def outline(self):
        pygame.draw.polygon(SCREEN, colors["white"],
        (
            [self.centerx - self.size/2, self.centery - self.size/2],
            [self.centerx + self.size/2, self.centery - self.size/2],
            [self.centerx + self.size/2, self.centery + self.size/2],
            [self.centerx - self.size/2, self.centery + self.size/2]))
        pygame.draw.polygon(SCREEN, colors["background"],
        (
            [self.centerx - (self.size/2 - self.width), self.centery - (self.size/2 - self.width)],
            [self.centerx + (self.size/2 - self.width), self.centery - (self.size/2 - self.width)],
            [self.centerx + (self.size/2 - self.width), self.centery + (self.size/2 - self.width)],
            [self.centerx - (self.size/2 - self.width), self.centery + (self.size/2 - self.width)]))

    def draw(self):
        self.outline()
        if self.value == None:
            SCREEN.blit(questionmark_surf, questionmark_rect)
        elif self.value == 1:
            pygame.draw.circle(SCREEN, colors["white"], self.center, self.dotsize)
        elif self.value == 2:
            pygame.draw.circle(SCREEN, colors["white"], (self.centerx - self.size/4, self.centery - self.size/4), self.dotsize)
            pygame.draw.circle(SCREEN, colors["white"], (self.centerx + self.size/4, self.centery + self.size/4), self.dotsize)
        elif self.value == 3:
            pygame.draw.circle(SCREEN, colors["white"], (self.centerx - self.size/4, self.centery - self.size/4), self.dotsize)
            pygame.draw.circle(SCREEN, colors["white"], self.center, self.dotsize)
            pygame.draw.circle(SCREEN, colors["white"], (self.centerx + self.size/4, self.centery + self.size/4), self.dotsize)
        elif self.value == 4:
            pygame.draw.circle(SCREEN, colors["white"], (self.centerx - self.size/4, self.centery - self.size/4), self.dotsize)
            pygame.draw.circle(SCREEN, colors["white"], (self.centerx + self.size/4, self.centery - self.size/4), self.dotsize)
            pygame.draw.circle(SCREEN, colors["white"], (self.centerx + self.size/4, self.centery + self.size/4), self.dotsize)
            pygame.draw.circle(SCREEN, colors["white"], (self.centerx - self.size/4, self.centery + self.size/4), self.dotsize)
        elif self.value == 5:
            pygame.draw.circle(SCREEN, colors["white"], (self.centerx - self.size/4, self.centery - self.size/4), self.dotsize)
            pygame.draw.circle(SCREEN, colors["white"], (self.centerx + self.size/4, self.centery - self.size/4), self.dotsize)
            pygame.draw.circle(SCREEN, colors["white"], (self.centerx + self.size/4, self.centery + self.size/4), self.dotsize)
            pygame.draw.circle(SCREEN, colors["white"], (self.centerx - self.size/4, self.centery + self.size/4), self.dotsize)
            pygame.draw.circle(SCREEN, colors["white"], self.center, self.dotsize)
        elif self.value == 6:
            pygame.draw.circle(SCREEN, colors["white"], (self.centerx - self.size/4, self.centery - self.size/4), self.dotsize)
            pygame.draw.circle(SCREEN, colors["white"], (self.centerx + self.size/4, self.centery - self.size/4), self.dotsize)
            pygame.draw.circle(SCREEN, colors["white"], (self.centerx + self.size/4, self.centery + self.size/4), self.dotsize)
            pygame.draw.circle(SCREEN, colors["white"], (self.centerx - self.size/4, self.centery + self.size/4), self.dotsize)
            pygame.draw.circle(SCREEN, colors["white"], (self.centerx + self.size/4, self.centery), self.dotsize)
            pygame.draw.circle(SCREEN, colors["white"], (self.centerx - self.size/4, self.centery), self.dotsize)

    def roll(self):
        for i in range(20):
            self.value = random.randint(1, 6)
            self.draw()
            #time.sleep(0.05)

    def main(self):
        self.draw()
dice = Dice(W/3*2, (W/2, H/2), 16)


def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    dice.roll()

        SCREEN.fill(colors["background"])
        SCREEN.blit(text_surf, text_rect)
        SCREEN.blit(info_surf, info_rect)
        
        dice.main()

        CLOCK.tick(FPS)
        pygame.display.update()

main()
