import time
import pygame

class Player():
    def __init__(self,x,y):
        self.posx = x
        self.posy = y
        self.dx = 0
        self.dy = 0
        self.size = 10
        self.speed = 30

    def getObject(self):
        return [self.posx, self.posy, self.size, self.size]

    
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

xx1 = dis_w/2
xy1 = dis_h/2
snake = Player(100,100)

xsnake_block = 10

xx1_change = 0
xy1_change = 0

clock = pygame.time.Clock()
xsnake_speed = 30

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
                snake.dx = -10
                snake.dy = 0
            elif event.key == pygame.K_RIGHT:
                snake.dx = 10
                snake.dy = 0
            elif event.key == pygame.K_UP:
                snake.dx = 0
                snake.dy = -10
            elif event.key == pygame.K_DOWN:
                snake.dx = 0
                snake.dy = 10
            elif event.key == pygame.K_ESCAPE:
                game_over = True

    snake.posx += snake.dx
    snake.posy += snake.dy
    if (snake.posx>=dis_w-snake.size
        or snake.posx<=0
        or snake.posy>=dis_h-snake.size
        or snake.posy <= 0):
        game_over = True
    dis.fill(white)
    pygame.draw.rect(dis,black,snake.getObject())
    pygame.display.update()

    clock.tick(snake.speed)

message("You lost!", red)
pygame.display.update()
time.sleep(2)
pygame.quit()
quit()
