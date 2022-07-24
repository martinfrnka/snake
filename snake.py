import time
import pygame
pygame.init()

white=(255,255,255)
black=(0,0,0)
blue = (0,0,255)
red = (255,0,0)
dis_w = 800
dis_h = 600
dis=pygame.display.set_mode((dis_w,dis_h))
pygame.display.set_caption('Snake game by Martin')

game_over=False

x1 = dis_w/2
y1 = dis_h/2

snake_block = 10

x1_change = 0
y1_change = 0

clock = pygame.time.Clock()
snake_speed = 30

font_style = pygame.font.SysFont(None, 50)

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg,[dis_w/2, dis_h/2])

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -10
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = 10
                y1_change = 0
            elif event.key == pygame.K_UP:
                x1_change = 0
                y1_change = -10
            elif event.key == pygame.K_DOWN:
                x1_change = 0
                y1_change = 10
            elif event.key == pygame.K_ESCAPE:
                game_over = True

    x1 += x1_change
    y1 += y1_change
    if (x1>=dis_w-snake_block or x1<=0 or y1>=dis_h-snake_block or y1 <= 0):
        game_over = True
    dis.fill(white)
    pygame.draw.rect(dis,black,[x1,y1,snake_block,snake_block])
    pygame.display.update()

    clock.tick(snake_speed)

message("You lost!", red)
pygame.display.update()
time.sleep(2)
pygame.quit()
quit()
