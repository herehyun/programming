import pygame
import random

pygame.init()

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("똥 피하기")

clock = pygame.time.Clock()

background = pygame.image.load("/Users/gihyunyeo/Desktop/programming/python_game/pygame_basic/background.jpeg")

# 주인공 불러오기
character = pygame.image.load("/Users/gihyunyeo/Desktop/programming/python_game/pygame_basic/dog.jpeg")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width)
character_y_pos = screen_height - character_height

to_x = 0

character_speed = 0.6

#똥 만들기
ddong = pygame.image.load("/Users/gihyunyeo/Desktop/programming/python_game/pygame_basic/ddong.jpeg")
ddong_size = ddong.get_rect().size
ddong_width = ddong_size[0]
ddong_height = ddong_size[1]
ddong_x_pos = random.randint(0, screen_width - ddong_width)
ddong_y_pos = 0
ddong_speed = 10



running = True
while  running:
    dt = clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0

# 게임 캐릭터 위치 정의
    character_x_pos += to_x * dt

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    ddong_y_pos += ddong_speed

    if ddong_y_pos > screen_height:
        ddong_y_pos = 0
        ddong_x_pos = random.randint(0, screen_width- ddong_width)


    character_rect = character.get_rect()
    character_rect.left = character_x_pos

    ddong_rect = ddong.get_rect()
    ddong_rect.left = ddong_x_pos
    ddong_rect.top = ddong_y_pos

    # 4. 충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    ddong_rect = ddong.get_rect()
    ddong_rect.left = ddong_x_pos
    ddong_rect.top = ddong_y_pos



    if character_rect.colliderect(ddong_rect):
        print("똥 맞았습니다.")
        running = False


    screen.blit(background, (0, 0)) # 배경 그리기
    screen.blit(character, (character_x_pos, character_y_pos)) # 캐릭터 그리기
    screen.blit(ddong, (ddong_x_pos, ddong_y_pos)) #적 그리기

    pygame.display.update()

pygame.quit()
