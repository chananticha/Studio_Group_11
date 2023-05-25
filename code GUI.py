import pygame as pg
pg.init()





class Rectangle:
    def __init__(pos,x = 0,y = 0,w = 0,h = 0,r = 0,g = 0,b = 0):
        pos.x = x # Position X
        pos.y = y # Position Y
        pos.w = w # Width
        pos.h = h # Height
        pos.R = r
        pos.G = g
        pos.B = b
    def draw(self,screen):
       pg.draw.rect(screen,(self.R,self.G,self.B),(self.x,self.y,self.w,self.h),3,12)

    def isMouseOn(self):
        mouse_x , mouse_y = pg.mouse.get_pos()
        if mouse_x > self.x and mouse_x <= self.x + self.w and mouse_y >= self.y and mouse_y <= self.y + self.h:
            return True
        else :
            return False
        pass

    def isclick(self):
        if pg.mouse.get_pressed()[0] :
            return True
        else :
            return False
    

class Button(Rectangle):
    def __init__(self, x=0, y=0, w=0, h=0,r = 0,g = 0,b = 0):
        Rectangle.__init__(self, x, y, w, h, r, g, b)
    
    def isMouseOn(self):
        mouse_x , mouse_y = pg.mouse.get_pos()
        if mouse_x > self.x and mouse_x <= self.x + self.w and mouse_y >= self.y and mouse_y <= self.y + self.h:
            return True
        else :
            return False
        pass

    def isclick(self):
        if pg.mouse.get_pressed()[0] :
            return True
        else :
            return False
    
    def draw(self,screen):
       pg.draw.rect(screen,(self.R,self.G,self.B),(self.x,self.y,self.w,self.h),0,12)

        
class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        
        
        if event.type == pg.MOUSEBUTTONDOWN:# ทำการเช็คว่ามีการคลิก Mouse หรือไม่
            if self.rect.collidepoint(event.pos): #ทำการเช็คว่าตำแหน่งของ Mouse อยู่บน InputBox นี้หรือไม่
                # Toggle the active variable.
                self.active = True
            else:
                self.active = False
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE # เปลี่ยนสีของ InputBox
            
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
                # else:
                    
                #     self.text += event.unicode
                    
                # # Re-render the text.
                # self.txt_surface = FONT.render(self.text, True, self.color)

    # def handle_event_num(self, event):

    #     if event.type == pg.MOUSEBUTTONDOWN:
    #         if self.rect.collidepoint(event.pos):
    #             self.active = True
    #         else:
    #             self.active = False
             
    #         if self.active:
    #             self.color = COLOR_ACTIVE
    #         else:
    #             self.color = COLOR_INACTIVE

    #     if event.type == pg.KEYDOWN:
    #         if self.active:
    #             if event.key == pg.K_RETURN:
    #                 print(self.text)
    #                 self.text = ''
    #             elif event.key == pg.K_BACKSPACE:
    #                 self.text = self.text[:-1]
    #             else:
    #                 if chr(event.key).isnumeric():
    #                     self.text += event.unicode
    #             self.txt_surface = FONT.render(self.text, True, self.color)
    
    # def recollect(self):
    #     return self.keep
    
    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, Screen):
        # Blit the text.
        Screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pg.draw.rect(Screen, self.color, self.rect, 1, 10)

    def isclick(self):
        if pg.mouse.get_pressed()[0] :
            return True
        else :
            return False

IStoPixel_x = 960/325 
IStoPixel_y = 720/243.75 



run = True
win_x, win_y = 960, 720
screen = pg.display.set_mode((win_x, win_y))

# ////////////////////////////////พื้นหลังข้อความ///////////////////////////////////////

BackgroundWhite = Button(50, 50, 860, 620, 255, 255, 255) # สร้าง Object จากคลาส Rectangle ขึ้นมา
START_BackgroundBox = Button(385, 525, 180, 80, 188, 229, 185)
Back_BackgroundBox = Button(10, 10, 85, 40, 255, 255, 255)
ShowBar_BackgroundBox = Button(120, 10, 800, 90, 219, 219, 219)
Sping_BackgroundBox = Button(180, 250, 200, 32, 219, 219, 219)
Basket_BackgroundBox = Button(180, 400, 200, 32, 219, 219, 219)
ChoiceWall_1_BackgroundBox = Button(620, 340, 32, 32, 219, 219, 219)
ChoiceWall_2_BackgroundBox = Button(750, 340, 32, 32, 219, 219, 219)
ShowRecoilSpring_BackgroundBox = Button(160, 60, 95, 30, 255, 255, 255)
ShowHeighWall_BackgroundBox = Button(345, 60, 95, 30, 255, 255, 255)
ShowBasketPosition_BackgroundBox = Button(535, 60, 95, 30, 255, 255, 255)
ShowMachinePosition_BackgroundBox = Button(745, 60, 95, 30, 255, 255, 255)


FONT = pg.font.Font(None, 32)

# ////////////////////////////////กรอบข้อความ///////////////////////////////////////

SIMULATION_EdgeBox = Rectangle(300, 75, 365, 70, 76, 74, 89) # สร้าง Object จากคลาส Button ขึ้นมา
START_EdgeBox = Rectangle(385, 525, 180, 80, 76, 74, 89)
Back_EdgeBox = Rectangle(10, 10, 85, 40, 76, 74, 89)
ShowBar_EdgeBox = Rectangle(120, 10, 800, 90, 76, 74, 89)
ReSimulation_EdgeBox = Rectangle(380, 110, 200, 40, 76, 74, 89)
ShowRecoilSpring_EdgeBox = Rectangle(160, 60, 95, 30, 76, 74, 89)
ShowHeighWall_EdgeBox = Rectangle(345, 60, 95, 30, 76, 74, 89)
ShowBasketPosition_EdgeBox = Rectangle(535, 60, 95, 30,76, 74, 89)
ShowMachinePosition_EdgeBox = Rectangle(745, 60, 95, 30, 76, 74, 89)

COLOR_INACTIVE = pg.Color(179, 179, 179) # ตั้งตัวแปรให้เก็บค่าสี เพื่อนำไปใช้เติมสีให้กับกล่องข้อความตอนที่คลิกที่กล่องนั้นๆอยู่
COLOR_ACTIVE = pg.Color(0, 0, 0)   

# ///////////////////////////////กล่องใส่ข้อมูล////////////////////////////////////////

input_box1 = InputBox(180, 250, 140, 32)
input_box2 = InputBox(180, 400, 140, 32)

input_boxes = [input_box1, input_box2] # เก็บ InputBox ไว้ใน list เพื่อที่จะสามารถนำไปเรียกใช้ได้ง่าย

# ///////////////////////////////ขนาดฟอนต์////////////////////////////////////////

font = pg.font.Font('freesansbold.ttf', 15)
font1 = pg.font.Font('freesansbold.ttf', 20)
font2 = pg.font.Font('freesansbold.ttf', 25)
font3 = pg.font.Font('freesansbold.ttf', 50)
font4 = pg.font.Font('freesansbold.ttf', 40)

# ////////////////////////////////ข้อความ///////////////////////////////////////

text_SIM = font3.render('SIMULATION', True, (0,0,0), (255,255,255)) # (text,is smooth?,letter color,background color)
textRect_SIM = text_SIM.get_rect() # text size
textRect_SIM.center = (win_x // 2, 110)

text2 = font2.render('Recoil spring (cm)', True, (0,0,0), (255,255,255)) # (text,is smooth?,letter color,background color)
textRect2 = text2.get_rect() # text size
textRect2.center = (290, 230)

text3 = font2.render('Basket position (cm)', True, (0,0,0), (255,255,255)) # (text,is smooth?,letter color,background color)
textRect3 = text3.get_rect() # text size
textRect3.center = (300, 380)

text_HeightWall = font2.render('Height of the Wall (cm)', True, (0,0,0), (255, 255, 255))
textRect_HeightWall = text_HeightWall.get_rect()
textRect_HeightWall.center = (700, 295)

text_ChoiceWall_1 = font1.render('50 cm', True, (0,0,0), (255, 255, 255))
textRect_ChoiceWall_1 = text_ChoiceWall_1.get_rect()
textRect_ChoiceWall_1.center = (635, 390)

text_ChoiceWall_2 = font1.render('100 cm', True, (0,0,0), (255, 255, 255))
textRect_ChoiceWall_2 = text_ChoiceWall_2.get_rect()
textRect_ChoiceWall_2.center = (770, 390)

text_START = font4.render('START', True, (0,0,0), (188,229,185)) # (text,is smooth?,letter color,background color)
textRect_START = text_START.get_rect() # text size
textRect_START.center = (475, 565)

text_RecoilSpring = font1.render('Recoil spring', True, (0,0,0), (219, 219, 219))
textRect_RecoilSpring = text_RecoilSpring.get_rect()
textRect_RecoilSpring.center = (210, 40)


text_HeighWall = font1.render('Height of the Wall', True, (0,0,0), (219, 219, 219))
textRect_HeighWall = text_HeighWall.get_rect()
textRect_HeighWall.center = (390, 40)

text_BasketPosition = font1.render('Basket position', True, (0,0,0), (219, 219, 219))
textRect_BasketPosition = text_BasketPosition.get_rect()
textRect_BasketPosition.center = (590, 40)

text_MachinePosition = font1.render('Machine position', True, (0,0,0), (219, 219, 219))
textRect_MachinePosition = text_MachinePosition.get_rect()
textRect_MachinePosition.center = (790, 40)

text_RESIMMULATION = font1.render('RESIMMULATION', True, (0,0,0), (255,255,255))
textRect_RESIMMULATION = text_RESIMMULATION.get_rect()
textRect_RESIMMULATION.center = (480, 130)

text_Back = font2.render('Back', True, (0,0,0), (255,255,255)) # (text,is smooth?,letter color,background color)
textRect_Back = text_Back.get_rect() # text size
textRect_Back.center = (53, 30)

# ///////////////////////////////////////////////////////////////////////


START_BackgroundBox_press = False
Back_BackgroundBox_press = True
while(run):
    if Back_BackgroundBox_press == True:
        screen.fill((219, 219, 219))
        BackgroundWhite.draw(screen)

        SIMULATION_EdgeBox.draw(screen)
        screen.blit(text_SIM, textRect_SIM)

        START_BackgroundBox.draw(screen)
        START_EdgeBox.draw(screen)
        screen.blit(text_START, textRect_START)

        Sping_BackgroundBox.draw(screen)
        screen.blit(text2, textRect2)

        Basket_BackgroundBox.draw(screen)
        screen.blit(text3, textRect3)

        screen.blit(text_HeightWall, textRect_HeightWall)
        ChoiceWall_1_BackgroundBox.draw(screen)
        screen.blit(text_ChoiceWall_1, textRect_ChoiceWall_1)
        ChoiceWall_2_BackgroundBox.draw(screen)
        screen.blit(text_ChoiceWall_2, textRect_ChoiceWall_2)
        
    
   
        for box in input_boxes: # ทำการเรียก InputBox ทุกๆตัว โดยการ Loop เข้าไปยัง list ที่เราเก็บค่า InputBox ไว้
            box.update() # เรียกใช้ฟังก์ชัน update() ของ InputBox
            box.draw(screen) 
    
    if START_BackgroundBox.isMouseOn():
        if START_BackgroundBox.isclick():
            Back_BackgroundBox_press = False
            START_BackgroundBox_press = True
        
        if START_BackgroundBox_press == True:
            screen.fill((255,255,255))
            Back_BackgroundBox.draw(screen)
            Back_EdgeBox.draw(screen)
            screen.blit(text_Back, textRect_Back)
            ShowBar_BackgroundBox.draw(screen)
            ShowBar_EdgeBox.draw(screen)
            ShowRecoilSpring_BackgroundBox.draw(screen)
            ShowRecoilSpring_EdgeBox.draw(screen)
            screen.blit(text_RecoilSpring, textRect_RecoilSpring) 
            ShowHeighWall_BackgroundBox.draw(screen)
            ShowHeighWall_EdgeBox.draw(screen)
            screen.blit(text_HeighWall, textRect_HeighWall)
            ShowBasketPosition_BackgroundBox.draw(screen)
            ShowBasketPosition_EdgeBox.draw(screen)
            screen.blit(text_BasketPosition, textRect_BasketPosition)
            ShowMachinePosition_BackgroundBox.draw(screen)
            ShowMachinePosition_EdgeBox.draw(screen)
            screen.blit(text_MachinePosition, textRect_MachinePosition)
            ReSimulation_EdgeBox.draw(screen)
            screen.blit(text_RESIMMULATION, textRect_RESIMMULATION)
            pg.draw.line(screen,(255,0,0),(win_x*80/325,720),(win_x*80/325,720-(77*IStoPixel_y)),2)
            pg.draw.line(screen,(255,0,0),(win_x*280/325,720),(win_x*280/325,680),2)
            pg.draw.line(screen,(124,71,0),(win_x*180/325,720),(win_x*180/325,720-(100720/243.75)),10)
            

    pg.display.update()
    for event in pg.event.get():
        if Back_BackgroundBox.isMouseOn():
                if Back_BackgroundBox.isclick():
                    Back_BackgroundBox_press = True
                    START_BackgroundBox_press = False
                    
        for box in input_boxes:
            box.handle_event(event)
        if event.type == pg.QUIT:
            pg.quit()
            run = False

    pg.time.delay(1)
    pg.display.update()