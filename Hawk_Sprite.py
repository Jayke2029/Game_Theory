
import pygame #type: ignore

pygame.init()

screen = pygame.display.set_mode((800,600))


hawk_image = pygame.image.load('hawk.png')


class Hawk(pygame.sprite.Sprite):
    def_init_(self) :                   # type: ignore
        super()._init_()    #type:ignore
        self.image = hawk_image # type: ignore
        self.rect = self.image.get_rect() # type: ignore


hawk_group = pygame.sprite.Group()
hawk = Hawk()
hawk_group.add(Hawk)

running = True
while running :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255,255,255))

    hawk_group.draw(screen)

    pygame.display.flip()

pygame.quit()



