import pygame

pygame.init()
screen = pygame.display.set_mode((800,600))

game_over = False

#                 orange colour
racket_colour = (255,128,0)
racket_pos_size = [50, 200, 20, 70]

background_color = (0,0,0)

# if the key is held, repeat its event every 10 milliseconds
pygame.key.set_repeat(10)

while not game_over:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            game_over = True


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_over = True
            elif event.key == pygame.K_w:
                racket_pos_size[1] -= 10
            elif event.key == pygame.K_s:
                racket_pos_size[1] += 10
    screen.fill(background_color)

    pygame.draw.rect(screen, racket_colour, racket_pos_size)
    pygame.display.update()


pygame.quit()
