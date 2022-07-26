from ctypes.wintypes import SIZE
import time
import pygame as pygame
import random

class Snake():
    def __init__(self,grid_width,grid_height, grid_size):
        self.grid_w = grid_width
        self.grid_h = grid_height
        self.posx = self.grid_w//2
        self.posy = self.grid_h//2
        self.body = []
        self.body.append((self.posx, self.posy))
        self.length = 1
        self.dx = 0
        self.dy = 0
        self.size = grid_size
        self.speed = 10
        
        self.score = 0

    def getObject(self):
        return [self.posx * self.size, self.posy* self.size, self.size, self.size]

    def reset(self):
        self.posx = self.grid_w//2
        self.posy = self.grid_h//2
        self.body = []
        self.body.append((self.posx, self.posy))
        self.length = 1
        self.speed = 10
        self.dx = 0
        self.dy = 0

    def crashed(self):
        if len(self.body)>=1:
            for i in range(1,len(self.body)):
                if self.body[0] == self.body[i]:
                    return True
        if (self.posx > self.grid_w
            or self.posx < 0
            or self.posy > self.grid_h
            or self.posy < 0):
            return True
        else:
            return False

    def testFood(self, food):
        if self.posx==food.posx and self.posy==food.posy:
            self.score +=1
            self.speed += 0
            self.length += 1
            self.body.append((-1,-1))
            food.isEdible = False

    def update(self):
        for i in range(len(self.body)-1, 0, -1):
            self.body[i] = self.body[i-1]
        self.posx += self.dx
        self.posy += self.dy
        self.body[0] = (self.posx, self.posy)
        return
        

    def draw(self, display, color):
        message("%s%s" % ("Score:  ", self.score), blue, (10,10))
        message("%s%s" % ("Speed:  ", self.speed), blue, (10,25))
        message("%s%s" % ("Length: ", self.length), blue, (10,40))
        for bodypart in self.body:
            pygame.draw.rect(display, color,(bodypart[0]*self.size, bodypart[1]*self.size, self.size, self.size))

class Food():
    def __init__(self,grid_width,grid_height, size, food_image):
        self.dis_w = grid_width
        self.dis_h = grid_height
        self.posx = -1
        self.posy = -1
        self.size = size
        self.isEdible = False
        self.food_img = pygame.transform.scale(food_image, (size, size))

    def placeFood(self):
        if not self.isEdible:
            self.posx = random.randint(1, self.dis_w-1)
            self.posy = random.randint(1, self.dis_h)
            self.isEdible = True;
        
    def getObject(self):
        return [self.posx*self.size, self.posy*self.size, self.size, self.size]
    
    def getPosition(self):
        return (self.posx*self.size, self.posy*self.size)

    def draw(self, display, color):
        #pygame.draw.rect(display, color,self.getObject())
        display.blit(self.food_img, self.getPosition())


pygame.init()

white=(255,255,255)
black=(0,0,0)
blue = (0,0,255)
red = (255,0,0)
grid_w = 15
grid_h = 15
grid_size = 20

dis_w = (grid_w + 1) * grid_size
dis_h = (grid_h + 1) * grid_size
dis=pygame.display.set_mode((dis_w,dis_h))
pygame.display.set_caption('Snake game by Martin')

foodimg = pygame.image.load(r'resources/food1.png')
snake = Snake(grid_w, grid_h, grid_size)
food = Food(grid_w, grid_h, grid_size, foodimg)

clock = pygame.time.Clock()

font_style = pygame.font.SysFont(None, 20)

def message(msg, color, pos):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, pos)


def menu_loop():
    message("You lost!", red, (dis_w/2, dis_h/2))
    pygame.display.update()
    snake.reset();
    time.sleep(2)


def game_loop():
    end_game = False
    while not end_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    snake.dx = -1
                    snake.dy = 0
                elif event.key == pygame.K_RIGHT:
                    snake.dx = 1
                    snake.dy = 0
                elif event.key == pygame.K_UP:
                    snake.dx = 0
                    snake.dy = -1
                elif event.key == pygame.K_DOWN:
                    snake.dx = 0
                    snake.dy = 1
                elif event.key == pygame.K_ESCAPE:
                    end_game = True
                 

        food.placeFood()
        snake.testFood(food)
        snake.update()
        if snake.crashed():
            menu_loop()

        dis.fill(white)

        food.draw(dis, red)
        snake.draw(dis,black)

        pygame.display.update()

        clock.tick(snake.speed)


game_loop()

pygame.quit()
quit()
