from ctypes.wintypes import SIZE
import time
import pygame as pygame
import random

class Snake():
    def __init__(self,grid_width,grid_height, grid_size, speed, headimg, bodyimg, bodyimg2, tailimg):
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
        self.default_speed = speed
        self.speed = self.default_speed
        self.headimg = pygame.transform.scale(headimg, (grid_size, grid_size))
        self.bodyimg = pygame.transform.scale(bodyimg, (grid_size, grid_size))
        self.bodyimg2 = pygame.transform.scale(bodyimg2, (grid_size, grid_size))
        self.tailimg = pygame.transform.scale(tailimg, (grid_size, grid_size))
        
        self.score = 0
        self.lives = 3

    def getObject(self):
        return [self.posx * self.size, self.posy* self.size, self.size, self.size]

    def reset(self):
        self.posx = self.grid_w//2
        self.posy = self.grid_h//2
        self.body = []
        self.body.append((self.posx, self.posy))
        self.length = 1
        self.speed = self.default_speed

        self.dx = 0
        self.dy = 0
        if (self.isDead()):
            self.lives = 3
            self.score = 0


    def crashed(self):
        if len(self.body)>=1:
            for i in range(1,len(self.body)):
                if self.body[0] == self.body[i]:
                    self.lives -= 1        
                    return True
        if (self.posx > self.grid_w
            or self.posx < 0
            or self.posy > self.grid_h
            or self.posy < 0):
            self.lives -= 1        
            return True
        else:
            return False
    
    def isDead(self):
        if self.lives <0:
            return True
        else:
            return False

    def testFood(self, food):
        if self.posx==food.posx and self.posy==food.posy:
            self.score +=1
            self.speed += 1
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
        
    def getPosition(self):
        return (self.posx*self.size, self.posy*self.size)

    def draw(self, display, color):
        message("%s%s" % ("Score:  ", self.score), blue, (10,10))
        message("%s%s" % ("Speed:  ", self.speed), blue, (10,25))
        message("%s%s" % ("Length: ", self.length), blue, (10,40))
        message("%s%s" % ("Lives: ", self.lives), blue, (10,55))
        for i in range(0,len(self.body)):
            rot = 0
            if i == 0: #head
                img = self.headimg
                if self.dy == 1:
                    rot = 180
                elif self.dy == -1:
                    rot = 0
                elif self.dx == 1:
                    rot = 270
                else:
                    rot = 90
            elif i == len(self.body)-1: #tail
                img = self.tailimg
                if (self.body[i-1][0] < self.body[i][0]):
                    rot = 90
                elif (self.body[i-1][0] > self.body[i][0]): 
                    rot = 270
                elif (self.body[i-1][1] < self.body[i][1]):
                    rot = 0
                else: 
                    rot = 180
            else: #body
                if ((self.body[i-1][0] == self.body[i+1][0]) or (self.body[i-1][1] == self.body[i+1][1])): #body straight
                    img = self.bodyimg
                    if (self.body[i-1][0] == self.body[i+1][0]): #horizontal
                        rot = 0
                    else:
                        rot = 90

                    
                else: # body turn
                    img = self.bodyimg2
                    if ((self.body[i-1][0] > self.body[i+1][0]) and (self.body[i-1][1] > self.body[i+1][1])):
                        if ((self.body[i-1][0] > self.body[i][0])):
                            rot = 0
                        else:
                            rot = 180
                    elif ((self.body[i-1][0] > self.body[i+1][0]) and (self.body[i-1][1] < self.body[i+1][1])):
                        if ((self.body[i-1][0] > self.body[i][0])):
                            rot = 270
                        else:
                            rot = 90
                    elif ((self.body[i-1][0] < self.body[i+1][0]) and (self.body[i-1][1] > self.body[i+1][1])):
                        if ((self.body[i-1][0] < self.body[i][0])):
                            rot = 90
                        else:
                            rot =270
                    else:
                        if ((self.body[i-1][0] < self.body[i][0])):
                            rot = 180
                        else:
                            rot =0

            #pygame.draw.rect(display, color,(bodypart[0]*self.size, bodypart[1]*self.size, self.size, self.size))
            display.blit(pygame.transform.rotate(img, rot), (self.body[i][0]*self.size, self.body[i][1]*self.size))

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
grid_w = 20
grid_h = 20
grid_size = 26
snake_speed = 5
dis_w = (grid_w + 1) * grid_size
dis_h = (grid_h + 1) * grid_size
dis=pygame.display.set_mode((dis_w,dis_h))
pygame.display.set_caption('Snake game by Martin')

foodimg = pygame.image.load(r'resources/food1.png')
headimg = pygame.image.load(r'resources/head1.png')
bodyimg = pygame.image.load(r'resources/body1.png')
bodyimg2 = pygame.image.load(r'resources/body2.png')
tailimg = pygame.image.load(r'resources/tail1.png')
snake = Snake(grid_w, grid_h, grid_size, snake_speed, headimg, bodyimg, bodyimg2, tailimg)
food = Food(grid_w, grid_h, grid_size, foodimg)

clock = pygame.time.Clock()

font_style = pygame.font.SysFont(None, 20)

def message(msg, color, pos):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, pos)


def you_died():
    message("You died!", red, (dis_w/2, dis_h/2))
    pygame.display.update()
    snake.reset()
    time.sleep(2)

def game_over():
    message("Game over!", red, (dis_w/4, dis_h/2-15))
    message("Press a key to restart, ESC to quit", red, (dis_w/4, dis_h/2))
    message("ESC to quit", red, (dis_w/4, dis_h/2+15))
    pygame.display.update()
    deadloop = True
    while deadloop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                else:
                   deadloop = False
                   snake.reset();

 



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
        if snake.crashed():
            if snake.isDead():
                game_over()
            else:
                you_died()
        snake.update()

        dis.fill(white)

        food.draw(dis, red)
        snake.draw(dis,black)

        pygame.display.update()

        clock.tick(snake.speed)


game_loop()

pygame.quit()
quit()
