class Rectangle:
    def __init__(self,x=0,y=0,w=0,h=0,colorButton=(0,255,0)):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.colorButton = colorButton
    def draw(self,screen):
        pg.draw.rect(screen,self.colorButton,(self.x,self.y,self.w,self.h))

class Button(Rectangle):
    def __init__(self,x=0,y=0,w=0,h=0):
        Rectangle.__init__(self,x,y,w,h)

    def isMouseOn(self):
        mouse_x, mouse_y = pg.mouse.get_pos()
        if self.x <= mouse_x <= (self.x+self.w) and self.y <= mouse_y <= (self.y+self.h):
            return True
        else:
            return False
    def isMousePress(self):
        return pg.mouse.get_pressed()[0]

class InputBox:
    def __init__(self,x,y,w,h,text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):

        if event.type == pg.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = True
            else:
                self.active = False
             
            if self.active:
                self.color = COLOR_ACTIVE
            else:
                self.color = COLOR_INACTIVE

        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                self.txt_surface = FONT.render(self.text, True, self.color)

    def handle_event_num(self, event):

        if event.type == pg.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = True
            else:
                self.active = False
             
            if self.active:
                self.color = COLOR_ACTIVE
            else:
                self.color = COLOR_INACTIVE

        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    if chr(event.key).isnumeric():
                        self.text += event.unicode
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self,Screen):
        Screen.blit(self.txt_surface,(self.rect.x+5, self.rect.y+5))
        pg.draw.rect(Screen, self.color, self.rect, 2)
    
    def isMousePress(self):
        return pg.mouse.get_pressed()[0]

class Simulation:
    def __init__(self, compress_length, basket_distance):
        self.compress_length = compress_length
        self.basket_distance =basket_distance
        self.degree = 60
        self.g = -9.806
        self.u = math.sqrt(((self.compress_length**2)*832.8/0.398)+(2*self.g*self.compress_length*math.sin(math.radians(self.degree))))
        self.ux = self.u*math.cos(math.radians(self.degree))
        self.uy = self.u*math.sin(math.radians(self.degree))
        self.time = 0
        self.y_distance = -0.42
        self.x_distance = (-(2*(self.u**2)*(math.cos(math.radians(self.degree))**2)*math.tan(math.radians(self.degree))) - math.sqrt(((2*(self.u**2)*(math.cos(math.radians(self.degree))**2)*math.tan(math.radians(self.degree)))**2)-(4*(self.g)*(2*(5.3**2)*(math.cos(math.radians(self.degree))**2)*(self.y_distance*-1)))))/(2*(self.g))
        self.shooting_distance = self.x_distance - self.basket_distance -2
        self.Pos_x = 0
        self.Pos_y = 0
        self.path = []

class Shooting:
    def __init__(self,x=0,y=0,w=0,h=0,color=(0,0,0)):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color
    def draw(self,screen):
        pg.draw.rect(screen,self.color,(self.x,self.y,self.w,self.h))

class SquashBall:
    def __init__(self, x=0, y=0.77, r=1, color=(0,0,0)):
        self.x = x
        self.y = y
        self.r = r
        self.color = color
    def draw(self,screen):
        pg.draw.circle(screen,self.color,(self.x,self.y),self.r)

class Wall:
    def __init__(self,x=0,y=0,w=0,h=0,color=(0,0,0)):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color
    def draw(self,screen):
        pg.draw.rect(screen,self.color,(self.x,self.y,self.w,self.h))

class Basket:
    def __init__(self,x,y=0.35,w=0.13,h=0.35,color=(0,0,0)):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color
    def draw(self,screen):
        pg.draw.rect(screen,self.color,(self.x,self.y,self.w,self.h))


IStoPixel_x = 960/3.25 
IStoPixel_y = 720/2.4375 


import sys
import pygame as pg
import math

pg.init()
run = True
win_x, win_y = 960, 720
screen = pg.display.set_mode((win_x,win_y))

# ////////////////////////////////พื้นหลังข้อความ///////////////////////////////////////


# //////////////////////////////////////////////////////////////////////////////////

COLOR_INACTIVE = pg.Color(141,182,205) # ตั้งตัวแปรให้เก็บค่าสี เพื่อนำไปใช้เติมสีให้กับกล่องข้อความตอนที่คลิกที่กล่องนั้นๆอยู่
COLOR_ACTIVE = pg.Color(28,134,238)     # ^^^
FONT = pg.font.Font(None, 32)

font = pg.font.Font('freesansbold.ttf', 26)
text_compress_length = font.render('compress_length', True, 'black', (255,255,255))
text_basket_distance = font.render('basket_distance', True, 'black', (255,255,255))

wall_50 = Button(100, 450, 200, 32)
wall_50Press = False

wall_100 = Button(400, 450, 200, 32)
wall_100Press = False

summit = Button(100, 600, 200, 32)
summitPress = False

compress_length = InputBox(100, 70, 140, 32)
basket_distance = InputBox(100, 140, 140, 32)
input_boxes = [compress_length, basket_distance]
run = True
runSimulation = True
numrunsimu = 0

while(run):
    screen.fill((219,219,219))
    summit.draw(screen)
    wall_50.draw(screen)
    wall_100.draw(screen)
    screen.blit(text_compress_length, (100,40))
    screen.blit(text_basket_distance, (100,110))
    for box in input_boxes:
        box.update()
        box.draw(screen)

    if wall_50.isMouseOn():
        if wall_50.isMousePress():
            wall_50Press = True
            wall_100Press = False
    if wall_50Press:
        wall_50.colorButton = (128,0,128)
        wall_100.colorButton = (0,128,128)

    if wall_100.isMouseOn():
        if wall_100.isMousePress():
            wall_50Press = False
            wall_100Press = True
    if wall_100Press:
        wall_50.colorButton = (0,128,128)
        wall_100.colorButton = (128,0,128)
    
    if summit.isMouseOn():
        summit.colorButton = (128,128,128)
        if summit.isMousePress():
            summit.colorButton = (128,0,128)
            summitPress = True
    else:
        summit.colorButton = (0,255,0)
    if summitPress:
        screen.fill((255,255,255))
        if numrunsimu == 0:
            simu = Simulation(float(compress_length.text)/100, float(basket_distance.text)/100)
        pg.draw.line(screen,(255,0,0),(win_x*0.80/3.25,720),(win_x*0.80/3.25,720-(0.77*IStoPixel_y)),2)
        pg.draw.line(screen,(255,0,0),(win_x*2.80/3.25,720),(win_x*2.80/3.25,680),2)
        pg.draw.line(screen,(255,0,0),(win_x*(2.80+(0.25*math.sqrt(3)))/3.25,720),(win_x*(2.80+(0.25*math.sqrt(3)))/3.25,680),2)
        simu_shooting = Shooting((win_x*0.80/3.25)-(0.40*IStoPixel_x)-(simu.shooting_distance*IStoPixel_x),720-(0.77*IStoPixel_y),0.40*IStoPixel_x,0.77*IStoPixel_y,(255,0,0))
        simu_shooting.draw(screen)

        simu_wall = Wall(win_x*1.78/3.25,win_y-(1*IStoPixel_y),win_x*0.02/3.25,(1*IStoPixel_y),(124,71,0))
        simu_wall.draw(screen)

        simu_basket = Basket((win_x*2.80/3.25)+(((float(basket_distance.text)/100)-0.065)*IStoPixel_x),720-(0.35*IStoPixel_y),0.13*IStoPixel_x,0.35*IStoPixel_y,(255,0,0))
        simu_basket.draw(screen)
        if numrunsimu == 0:
            simu_squashBall = SquashBall(simu_shooting.x+(0.40*IStoPixel_x),720-(0.79*IStoPixel_y),0.02*IStoPixel_y,(255,0,0))

        simu.path.append((simu_squashBall.x,simu_squashBall.y))
        for i in simu.path:
            pg.draw.circle(screen,(0,255,0),i,1)
        simu_squashBall.draw(screen)

        simu.uy = simu.uy + (simu.g*simu.time)
        simu_squashBall.x += (simu.ux*simu.time)*IStoPixel_x
        simu_squashBall.y -= ((simu.uy*simu.time)-(0.5*simu.g*(simu.time**2)))*IStoPixel_y
        simu.time += 0.00001

        screen.blit(text_compress_length, (100,40))
        textnum_compress_length = font.render(str(simu.compress_length), True, 'black', (255,255,255))
        screen.blit(textnum_compress_length, (500,40))

        screen.blit(text_basket_distance, (100,110))
        textnum_basket_distance = font.render(str(simu.basket_distance), True, 'black', (255,255,255))
        screen.blit(textnum_basket_distance, (500,110))

        text_x_distance = font.render('x_distance', True, 'black', (255,255,255))
        screen.blit(text_x_distance, (100,180))
        textnum_x_distance = font.render(str(simu.x_distance), True, 'black', (255,255,255))
        screen.blit(textnum_x_distance, (500,180))

        text_shooting_distance = font.render('shooting_distance', True, 'black', (255,255,255))
        screen.blit(text_shooting_distance, (100,250))
        textnum_shooting_distance = font.render(str(simu.shooting_distance), True, 'black', (255,255,255))
        screen.blit(textnum_shooting_distance, (500,250))
        numrunsimu += 1

        

    for event in pg.event.get():
        for box in input_boxes:
            box.handle_event(event)
        if event.type == pg.QUIT:
            pg.quit()
            run = False

    pg.time.delay(1)
    pg.display.update()