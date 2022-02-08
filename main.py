import pygame

pygame.init()
WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((800,600))
background_color = (0,0,0)

game_over = False
pygame.key.set_repeat(10)

# Rackets - init
#                 orange colour
racket1_colour = (255,128,0)
racket1_pos_size = [50, 200, 20, 70]

racket2_colour = (171,139,237)
racket2_pos_size = [730, 200, 20, 70]

# Ball
ball_pos_size = [WIDTH / 2, HEIGHT / 2, 10]
game_clock = pygame.time.Clock()

racket1 = pygame.draw.rect(screen, racket1_colour, racket1_pos_size)
racket2 = pygame.draw.rect(screen, racket2_colour, racket2_pos_size)
ball    = pygame.draw.circle(screen, (255,255,255), ball_pos_size[:2],  ball_pos_size[2])
ball_dx = 1
ball_dy = 0

# Game Loop
while not game_over:
    # Process input and update state
    for event in pygame.event.get():

        # obtain input and update the state
        print(event)
        if event.type == pygame.QUIT:
            game_over = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_over = True
            elif event.key == pygame.K_w:
                if racket1_pos_size[1] > 0:
                    racket1_pos_size[1] -= 10
            elif event.key == pygame.K_s:
                if racket1_pos_size[1] + racket1_pos_size[3] < HEIGHT:
                    racket1_pos_size[1] += 10
            elif event.key == pygame.K_UP:
                if racket2_pos_size[1] > 0:
                  racket2_pos_size[1] -= 10
            elif event.key == pygame.K_DOWN:
                if racket2_pos_size[1] + racket2_pos_size[3] < HEIGHT:
                    racket2_pos_size[1] += 10

    ball_pos_size[0] = ball_pos_size[0] + ball_dx
    ball_pos_size[1] = ball_pos_size[1] + ball_dy

    if racket2.colliderect(ball):
        ball_dx = -1
    if racket1.colliderect(ball):
        ball_dx = 1


    # Render
    screen.fill(background_color)
    racket1 = pygame.draw.rect(screen, racket1_colour, racket1_pos_size)
    racket2 = pygame.draw.rect(screen, racket2_colour, racket2_pos_size)
    ball = pygame.draw.circle(screen, (255,255,255), ball_pos_size[:2],  ball_pos_size[2])
    pygame.display.update()
    game_clock.tick(50)


pygame.quit()
