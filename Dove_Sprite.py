
import pygame #type: ignore

pygame.init()

screen = pygame.display.set_mode((800,600))


dove_image = pygame.image.load('dove.png')


class Dove(pygame.sprite.Sprite):
    def_init_(self) :                   # type: ignore
        super()._init_()    #type:ignore
        self.image = dove_image # type: ignore
        self.rect = self.image.get_rect() # type: ignore


dove_group = pygame.sprite.Group()
dove = Dove()
dove_group.add(Dove)

running = True
while running :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255,255,255))

    dove_group.draw(screen)

    pygame.display.flip()

pygame.quit()



