import random
import pygame

pygame.init()
displayWidth = 500
displayHeight = 500
display = pygame.display.set_mode((displayWidth, displayHeight), pygame.NOFRAME)  # Размер экрана
pygame.display.set_caption("SNAKE")  # Название игры

# Color list
snakeColor = (153, 170, 56)
headColor = (245, 245, 0)
appleColor = (191, 1, 20)
background = (232, 235, 247)

cube = 10  # Cube
snakeSpeed = 15  # Speed

clock = pygame.time.Clock()
fontSize = 20
fontStyle = pygame.font.SysFont("bahnschrift", fontSize)


def your_score(score):
    value = fontStyle.render("Score: " + str(score), True, (26, 27, 37))
    display.blit(value, [0, 0])


def our_snake(cube, snake_list):
    for x in snake_list:
        pygame.draw.rect(display, snakeColor,
                         [x[0], x[1], cube, cube])


def message(text, color, height=display.get_height() / 2 - fontSize / 10):
    display.blit(fontStyle.render(text, True, color),
                 [display.get_width() / 2 - len(text) * fontSize * 0.23, height])


def game_loop():
    game_over = False
    game_lose = False

    # Start position
    x_snake = display.get_width() / 2
    y_snake = display.get_height() / 2

    x_change, y_change = 0, 0  # Changed position

    # Apple position
    x_apple = round(random.randrange(0, display.get_width() - cube) / 10.0) * 10
    y_apple = round(random.randrange(0, display.get_height() - cube) / 10.0) * 10

    snake_list = []
    length_snake = 1

    while not game_over:

        while game_lose:
            display.fill((0, 0, 0))
            message("GAME OVER! [Q]uit or [R]estart", (255, 255, 255))
            message("Score:" + str(length_snake - 1), (255, 255, 255), display.get_height() / 2 + fontSize)
            pygame.display.update()

            for click in pygame.event.get():
                if click.type == pygame.KEYDOWN:
                    if click.key == pygame.K_q:
                        game_over = True
                        game_lose = False
                    if click.key == pygame.K_r:
                        game_loop()

        for click in pygame.event.get():
            # Quit
            if click.type == pygame.QUIT:
                game_over = True

            # Controls
            if click.type == pygame.KEYDOWN:
                if click.key == pygame.K_RIGHT and x_change != -cube:
                    x_change = cube
                    y_change = 0
                elif click.key == pygame.K_LEFT and x_change != cube:
                    x_change = -cube
                    y_change = 0
                elif click.key == pygame.K_UP and y_change != cube:
                    x_change = 0
                    y_change = -cube
                elif click.key == pygame.K_DOWN and y_change != -cube:
                    x_change = 0
                    y_change = cube

        # Смерть о край экрана
        if x_snake < 0 or x_snake >= display.get_width() or y_snake < 0 or y_snake >= display.get_height():
            game_lose = True

        x_snake += x_change
        y_snake += y_change

        display.fill(background)
        pygame.draw.rect(display, appleColor, [x_apple, y_apple, cube, cube])
        snake_head = [x_snake, y_snake]
        snake_list.append(snake_head)

        if len(snake_list) > length_snake:
            del snake_list[0]

        # Смерть о хвост
        for x in snake_list[:-1]:
            if x == snake_head:
                game_lose = True

        our_snake(cube, snake_list)
        your_score(length_snake - 1)

        pygame.display.update()

        if x_snake == x_apple and y_snake == y_apple:
            print("Score:", length_snake - 1)
            x_apple = round(random.randrange(0, display.get_width() - cube) / 10.0) * 10
            y_apple = round(random.randrange(0, display.get_height() - cube) / 10.0) * 10
            length_snake += 1
        clock.tick(snakeSpeed)

    pygame.quit()
    quit()


game_loop()
