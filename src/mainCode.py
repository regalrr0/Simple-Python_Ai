from PIL import ImageGrab, ImageOps
import os
import time
import win32api, win32con
from numpy import *

y_pad = 213
x_pad = 304

foodOnHand = {'shrimp':5,
              'rice':10,
              'nori':10,
              'roe':10,
              'salmon':5,
              'unagi':5}


def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    print "Click"
    
def leftDown():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    print "left down"
    
def leftUp():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    time.sleep(.1)
    print "left up"
    
def mousePos(cord):
    win32api.SetCursorPos((x_pad + cord[0], y_pad + cord[1]))
    
def get_cords():
    x,y = win32api.GetCursorPos()
    x = x-x_pad
    y=y-y_pad
    print x, y

def screenGrab(): 
    b1 = (x_pad+1, y_pad+1, x_pad+640, y_pad+480)
    im = ImageGrab.grab(b1)
    #im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.png', 'PNG')
    return im
    
def startGame():
    #first menu
    mousePos((342, 192))
    leftClick()
    time.sleep(.1)
    
    #second menu
    mousePos((396, 386))
    leftClick()
    time.sleep(.1)
    
    #third menu
    mousePos((565, 452))
    leftClick()
    time.sleep(.1)
    
    #fourth menu
    mousePos((404, 380))
    leftClick()
    time.sleep(.1)
    
class Cord:
    f_shrimp = (41, 330)
    f_rice = (100,333)
    f_nori = (29, 381)
    f_roe = (96, 381)
    f_salmon = (34, 444)
    f_unagi = (91, 447)
    
    #-- Phone Menu --
    
    phone = (577, 368)
    
    menu_toppings = (544, 270)
    t_shrimp = (544, 268)
    t_nori = (483, 224)
    t_roe = (578, 214)
    t_salmon = (494, 274)
    t_unagi = (582, 274)
    t_exit = (498, 335)
    
    menu_rice = (511, 294)
    buy_rice = (544, 281)
    
    delivery_norm = (485, 296)
    
    
# Plate cords:
def clear_tables():
    mousePos((93, 200))
    leftClick()
    
    mousePos((199, 210))
    leftClick()
    
    mousePos((296, 212))
    leftClick()
    
    mousePos((400, 213))
    leftClick()
    
    mousePos((498, 203))
    leftClick()
    
    mousePos((593, 208))
    leftClick()
    time.sleep(1)
    
def makeFood(food):
    if food == 'caliroll':
        print 'Rolling Caliroll'
        foodOnHand['rice'] -= 1
        foodOnHand['nori'] -= 1
        foodOnHand['roe'] -= 1
        mousePos(Cord.f_rice)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_nori)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_roe)
        leftClick()
        time.sleep(.1)
        foldMat()
        time.sleep(1.5)
        
    elif food == 'onigiri':
        print 'Rolling onigiri'
        foodOnHand['rice'] -= 2
        foodOnHand['nori'] -= 1
        mousePos(Cord.f_rice)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_rice)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_nori)
        leftClick()
        time.sleep(.1)
        foldMat()
        time.sleep(.1)
        
    elif food == 'gunkan':
        print 'Rolling a gunkan'
        foodOnHand['rice'] -= 1
        foodOnHand['nori'] -= 1
        foodOnHand['roe'] -= 2
        mousePos(Cord.f_rice)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_nori)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_roe)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_roe)
        leftClick()
        time.sleep(.1)
        foldMat()
        time.sleep(1.5)
        
    elif food == 'salmon':
        print 'Rolling salmon'
        foodOnHand['rice'] -= 1
        foodOnHand['nori'] -= 1
        foodOnHand['salmon'] -= 2
        mousePos(Cord.f_rice)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_nori)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_salmon)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_salmon)
        leftClick()
        time.sleep(.1)
        foldMat()
        time.sleep(1.5)
        
    elif food =='unagi':
        print 'Rolling unagi'
        foodOnHand['rice'] -= 1
        foodOnHand['nori'] -= 1
        foodOnHand['unagi'] -= 2
        mousePos(Cord.f_rice)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_nori)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_unagi)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_unagi)
        leftClick()
        time.sleep(.1)
        foldMat()
        time.sleep(1.5)
        
    elif food == 'dragon':
        print 'Rolling dragon'
        foodOnHand['rice'] -= 2
        foodOnHand['nori'] -= 1
        foodOnHand['roe'] -= 1
        foodOnHand['unagi'] -= 1
        mousePos(Cord.f_rice)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_rice)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_nori)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_roe)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_unagi)
        leftClick()
        time.sleep(.1)
        foldMat()
        time.sleep(1.5)
        
    elif food == 'combo':
        print 'Rolling combo'
        foodOnHand['rice'] -= 2
        foodOnHand['nori'] -= 1
        foodOnHand['roe'] -= 1
        foodOnHand['salmon'] -= 1
        foodOnHand['unagi'] -= 1
        foodOnHand['shrimp'] -= 1
        mousePos(Cord.f_rice)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_rice)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_nori)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_roe)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_salmon)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_unagi)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_shrimp)
        leftClick()
        time.sleep(.1)
        foldMat()
        time.sleep(1.5)
       
def buyFood(food):
    if food == 'rice':
        mousePos(Cord.phone)
        time.sleep(.1)
        leftClick()
        mousePos(Cord.menu_rice)
        time.sleep(.05)
        leftClick()
        s = screenGrab()
        if s.getpixel(Cord.buy_rice) != (109, 123, 127):
            print 'Rice is available'
            mousePos(Cord.buy_rice)
            time.sleep(.1)
            leftClick()
            mousePos(Cord.delivery_norm)
            foodOnHand['rice'] += 10
            time.sleep(.1)
            leftClick()
            time.sleep(2.5)
        else:
            print 'Rice is not available'
            mousePos(Cord.t_exit)
            leftClick()
            time.sleep(1)
            buyFood(food)
            
        if food == 'nori':
            mousePos(Cord.phone)
            time.sleep(.1)
            leftClick()
            mousePos(Cord.menu_toppings)
            time.sleep(.05)
            leftClick()
            s = screenGrab()
            time.sleep(.1)
            if s.getpixel(Cord.t_nori) != (67, 62, 23):
                print 'nori is available'
                mousePos(Cord.t_nori)
                time.sleep(.1)
                leftClick()
                mousePos(Cord.delivery_norm)
                foodOnHand['nori'] += 10
                time.sleep(.1)
                leftClick()
                time.sleep(2.5)
            else:
                print 'nori is not available'
                mousePos(Cord.t_exit)
                leftClick()
                time.sleep(.1)
                buyFood(food)
            
        if food == 'roe':
            mousePos(Cord.phone)
            time.sleep(.1)
            leftClick()
            mousePos(Cord.menu_toppings)
            time.sleep(.05)
            leftClick()
            s = screenGrab()
            time.sleep(.1)
            if s.getpixel(Cord.t_roe) != (203, 28, 28):
                print 'roe is available'
                mousePos(Cord.t_roe)
                time.sleep(.1)
                leftClick()
                mousePos(Cord.delivery_norm)
                foodOnHand['roe'] += 10
                time.sleep(.1)
                leftClick()
                time.sleep(2.5)
            else:
                print 'roe is not available'
                mousePos(Cord.t_exit)
                leftClick()
                time.sleep(.1)
                buyFood(food)
                
        if food == 'shrimp':
            mousePos(Cord.phone)
            time.sleep(.1)
            leftClick()
            mousePos(Cord.menu_toppings)
            time.sleep(.05)
            leftClick()
            s = screenGrab()
            time.sleep(.1)
            if s.getpixel(Cord.t_shrimp) != (255, 204, 182):
                print 'shrimp is available'
                mousePos(Cord.t_shrimp)
                time.sleep(.1)
                leftClick()
                mousePos(Cord.delivery_norm)
                foodOnHand['shrimp'] += 5
                time.sleep(.1)
                leftClick()
                time.sleep(2.5)
            else:
                print 'shrimp is not available'
                mousePos(Cord.t_exit)
                leftClick()
                time.sleep(.1)
                buyFood(food)
            
        if food == 'salmon':
            mousePos(Cord.phone)
            time.sleep(.1)
            leftClick()
            mousePos(Cord.menu_toppings)
            time.sleep(.05)
            leftClick()
            s = screenGrab()
            time.sleep(.1)
            if s.getpixel(Cord.t_salmon) != (255, 143, 96):
                print 'salmon is available'
                mousePos(Cord.t_salmon)
                time.sleep(.1)
                leftClick()
                mousePos(Cord.delivery_norm)
                foodOnHand['salmon'] += 5
                time.sleep(.1)
                leftClick()
                time.sleep(2.5)
            else:
                print 'salmon is not available'
                mousePos(Cord.t_exit)
                leftClick()
                time.sleep(.1)
                buyFood(food)    
        
        if food == 'unagi':
            mousePos(Cord.phone)
            time.sleep(.1)
            leftClick()
            mousePos(Cord.menu_toppings)
            time.sleep(.05)
            leftClick()
            s = screenGrab()
            time.sleep(.1)
            if s.getpixel(Cord.t_unagi) != (121, 60, 4):
                print 'unagi is available'
                mousePos(Cord.t_unagi)
                time.sleep(.1)
                leftClick()
                mousePos(Cord.delivery_norm)
                foodOnHand['unagi'] += 5
                time.sleep(.1)
                leftClick()
                time.sleep(2.5)
            else:
                print 'unagi is not available'
                mousePos(Cord.t_exit)
                leftClick()
                time.sleep(.1)
                buyFood(food)
                
def foldMat():
    mousePos((Cord.f_rice[0]+100, Cord.f_rice[1]))
    leftClick()
    time.sleep(.1)
    
def main():
    pass
    
if __name__ == '__main__':
    main()