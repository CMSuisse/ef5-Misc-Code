import pygame

pygame.init()
display_size = (500, 500)
screen = pygame.display.set_mode(display_size)
screen.fill((200, 200, 200))
Clock = pygame.time.Clock()

origin = (display_size[0]/2, display_size[1]/2)

for x in display_size[0]:
    for y in display_size[1]:
        point_on_plane = complex(x/200, y/200)
        

active = True
while active:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            active = False

    Clock.tick(60)
    pygame.display.flip()

pygame.quit()