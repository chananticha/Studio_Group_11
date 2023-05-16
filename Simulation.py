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
    
    def get(self):
        return self.text

IStoPixel_x = 960/325 
IStoPixel_y = 720/243.75 

class Simulation:
    def __init__(self,compress_length):
        self.degree = 60
        self.u = np.sqrt(((compress_length**2)*832.8/0.398)+(2*self.g*compress_length*np.sin(np.radians(self.degree))))
        self.ux = self.u*np.cos(np.radians(self.degree))
        self.uy = self.u*np.sin(np.radians(self.degree))
        self.g = 9.806
        self.time = 0
        self.x_distance = 0
        self.y_distance = 42
        self.Pos_x = 0
        self.Pos_y =0
        self.path = []
       


import sys
import pygame as pg
import numpy as np

pg.init()
run = True
win_x, win_y = 960, 720
screen = pg.display.set_mode((win_x,win_y))

COLOR_INACTIVE = pg.Color(141,182,205) # ตั้งตัวแปรให้เก็บค่าสี เพื่อนำไปใช้เติมสีให้กับกล่องข้อความตอนที่คลิกที่กล่องนั้นๆอยู่
COLOR_ACTIVE = pg.Color(28,134,238)     # ^^^
FONT = pg.font.Font(None, 32)

font = pg.font.Font('freesansbold.ttf', 26)
text_Compress_length = font.render('compress_length', True, 'black', (255,255,255))



compress_length = InputBox(100, 70, 140, 32)
wall_50 = Button(100, 450, 200, 32)
wall_50Press = False

wall_100 = Button(400, 450, 200, 32)
wall_100Press = False

summit = Button(100, 600, 200, 32)
summitPress = False

input_boxes = [compress_length]
run = True
runSimulation = True

while(run):
    screen.fill((255,255,255))
    summit.draw(screen)
    wall_50.draw(screen)
    wall_100.draw(screen)
    screen.blit(text_Compress_length, (100,40))
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
        pg.draw.line(screen,(255,0,0),(win_x*80/325,720),(win_x*80/325,680),2)
        pg.draw.line(screen,(255,0,0),(win_x*280/325,720),(win_x*280/325,680),2)
        pg.draw.line(screen,(124,71,0),(win_x*180/325,720),(win_x*180/325,720-(100*720/243.75)),10)
        

    for event in pg.event.get():
        for box in input_boxes:
            box.handle_event_num(event)
        if event.type == pg.QUIT:
            pg.quit()
            run = False

    pg.time.delay(1)
    pg.display.update()