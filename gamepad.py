

import pyvjoystick.vigem as vg
import win32api
import win32con
import time
import ctypes
import threading
import sys
sys.dont_write_bytecode = True

from pynput.mouse import Controller 
from pynput import keyboard as keyboard2
from pynput import mouse as mouse2
from keyhook import *



#gamepad = vg.VDS4Gamepad()

def include(filename):
    with open(filename, 'r') as f:
        exec(f.read(), sys._getframe(1).f_globals, sys._getframe(1).f_locals)

include("teste2.py") 
include("keys.py") 
#exec(open('inc_gui.py').read())
def on_press2(key, injected):
    try:
        print('alphanumeric key {} pressed; it was {}'.format(
            key.char, 'faked' if injected else 'not faked'))
    except AttributeError:
        print('special key {} pressed'.format(
            key))

def on_release2(key, injected):
    print('{} released; it was {}'.format(
        key, 'faked' if injected else 'not faked'))
    if key == keyboard2.Key.esc:
        # Stop listener
        return False
        
#recorded = keyboard.record(until='esc')
#print(recorded)

#gg = keyboard.read_event()
#keyboard.read_key(suppress=False)

#keyboard.on_press_key(key, callback, suppress=False)



#print(gg)

'''
listener2 = keyboard2.Listener(
    suppress=True,
    on_press=on_press,
    on_release=on_release)
listener2.start()
'''

wheelval = 0
def on_scroll(x, y, dx, dy):
    global wheelval
    direction = 'Down' if dy < 0 else 'Up'
    
    inc_wheel = spin_inc_wheel_var.get()
    dec_wheel = spin_dec_wheel_var.get()
 
    if (direction == 'Up'):
        wheelval = wheelval + int(inc_wheel)
    else:
        wheelval = wheelval - int(dec_wheel)
    
    if (wheelval > 255):
        wheelval = 255
    if (wheelval < 0):
        wheelval = 0
    #print(f"val: {wheelval} Scrolled {direction} at ({x}, {y})")
    combowheelval = combowheel.get()
    mousecenterposition = combomousecenterposition.get()
    x, y = win32api.GetCursorPos()
    #print(wheelval)
    if(combowheelval =='Left Trigger'):    
        gamepad.left_trigger(value=round(wheelval))
        gamepad.update()
    elif(combowheelval =='Right Trigger'):    
        gamepad.right_trigger(value=round(wheelval))
        gamepad.update()
    elif(combowheelval =='Center Mouse' and mousecenterposition =='X+Y'):  
        win32api.SetCursorPos((center_x, center_y))
        wheelval = 0
    elif(combowheelval =='Center Mouse' and mousecenterposition =='X'):  
        win32api.SetCursorPos((center_x, y))
        wheelval = 0
    elif(combowheelval =='Center Mouse' and mousecenterposition =='Y'):  
        win32api.SetCursorPos((x, center_y))
        wheelval = 0
    


def calibrate_loop():
    gamepadtype = combotype.get()
    x_int = y_int = 0
    while is_running:
        state = win32api.GetAsyncKeyState(0x02)
        if state < 0:
            win32api.SetCursorPos((center_x, center_y))
        x, y = win32api.GetCursorPos()
        x_value, y_value = mouse_to_joystick(x, y)
        count = threading.active_count()
        
        comboside = combo.get()
        xsens = x_sens_scale_var.get()
        ysens = y_sens_scale_var.get()
        deadz = deadzone_scale_var.get()
        if (use_integer.get() == 1):
            if (x_value > 0): x_value = int(32767 * x_value)
            else: x_value = int(32768 * x_value)
            if (y_value > 0): y_value = int(32767 * y_value)
            else: y_value = int(32768 * y_value)
      
        #print(f'[{count}] Dead: {deadz} X-Sens: {xsens} Y-Sens: {ysens} ## X: {str(x_value)}  Y: {str(y_value)}')
        print(f'[{count}] X: {str(x_value)}  Y: {str(y_value)}')
        #print(f'[{count}] X-Float: {str(x_value)}  X-Int: {str(x_value_int)} Y-Float: {str(y_value)} Y-Int: {str(y_value_int)}')
        
        
        time.sleep(0.01)
        

def main_loop():
    #if is_running:
    global gamepadtype
    global gamepad
    global keyh
    gamepadtype = combotype.get()
    mousefixed = combomousefixed.get()
    mouselimit = combomouselimit.get()
    limit_mouse_x = spin_limit_mouse_x_position_var.get()
    limit_mouse_y = spin_limit_mouse_y_position_var.get()
    
   
    if is_running:
        if (gamepadtype == 'Xbox 360'):
            gamepad = vg.VX360Gamepad()
            #gamepad.reset()
            #gamepad.left_joystick(x_value=0, y_value=0)
            #gamepad.right_joystick(x_value=0, y_value=0)
            #gamepad.update()
        elif (gamepadtype == 'DS4 (PS4)'):
            gamepad = vg.VDS4Gamepad()
        else:
            gamepad = vg.VDS4Gamepad()
       
    listener = mouse2.Listener(
        #on_move=on_move,
        #on_click=on_click,
        on_scroll=on_scroll
        #,suppress=True
        )
    listener.start()

   
    # Move to absolute X=500, Y=current
    if is_running:
        gamepad.left_joystick_float(x_value_float=0.0, y_value_float=0.0)
        gamepad.right_joystick_float(x_value_float=0.0, y_value_float=0.0)
        gamepad.update()
        gamepad.reset()
        
        keyboard.hook(key_on_off, suppress=True)
    keyh.pressed = []
    is_muted_key = False
    is_muted_joy = True
    while is_running:
       
        # NOT SEND KEYS TO JOY IF MUTED
        if (keyh.muted_joy == False):
            detectkeyboard(keyh.pressed)
            
        #SWTICH FOR MUTED JOY
        if (keyh.muted_joy == False and keyh.muted_joy != is_muted_joy):
            swtiches(lbl01_swtich,lbl01_var,'OFF')
        elif(keyh.muted_joy == True and keyh.muted_joy != is_muted_joy):
            swtiches(lbl01_swtich,lbl01_var,'ON')            
            
        #SWTICH FOR SUPRESS KEYBOARD
        if (keyh.muted_key == False and keyh.muted_key != is_muted_key):        
            swtiches(lbl0_swtich,lbl0_var,'OFF')
        elif (keyh.muted_key == True and keyh.muted_key != is_muted_key):
            swtiches(lbl0_swtich,lbl0_var,'ON')
            
        is_muted_key = keyh.muted_key
        is_muted_joy = keyh.muted_joy
        
        #print(30 in keyh.pressed)
        #print(mousefixed)
        #print(spin_mouse_x_position_var.get())
        
        # MOVE MOUSE
        #if (mousefixed == 'x'):
            #mouse2 = Controller()
            #current_y = mouse2.position[1]
            #mouse2.position = (spin_mouse_x_position_var.get(), current_y)
        
        # ANTIGO CENTER MOUSE
        #state = win32api.GetAsyncKeyState(0x02)
        #if state < 0:
        #    win32api.SetCursorPos((center_x, center_y))
            
            
        x, y = win32api.GetCursorPos()
        
        
        # MOUSE FIXED POSITION
        if (mousefixed == 'X' and ind_fixed_mouse==True):
            ctypes.windll.user32.SetCursorPos(spin_mouse_x_position_var.get(), y)
        elif (mousefixed == 'Y' and ind_fixed_mouse==True):
            ctypes.windll.user32.SetCursorPos(x, spin_mouse_y_position_var.get())
        elif (mousefixed == 'X+Y' and ind_fixed_mouse==True):
            ctypes.windll.user32.SetCursorPos(spin_mouse_x_position_var.get(), spin_mouse_y_position_var.get())
            
            
       
        #MOUSE LIMIT POSITION
        if (mouselimit == 'X' and x < limit_mouse_x and ind_limit_mouse==True):
            ctypes.windll.user32.SetCursorPos(limit_mouse_x, y)
        elif(mouselimit == 'X' and x > (width-limit_mouse_x) and ind_limit_mouse==True):
            ctypes.windll.user32.SetCursorPos((width-limit_mouse_x), y)
        elif (mouselimit == 'Y' and y < limit_mouse_y and ind_limit_mouse==True):
            ctypes.windll.user32.SetCursorPos(x, limit_mouse_y)
        elif (mouselimit == 'Y' and y > (height-limit_mouse_y) and ind_limit_mouse==True):
            ctypes.windll.user32.SetCursorPos(x, (height-limit_mouse_y))
        
        newlimitx = x
        newlimity = y
        if (mouselimit == 'X+Y' and x < limit_mouse_x):
            newlimitx = limit_mouse_x
        if (mouselimit == 'X+Y' and x > (width-limit_mouse_x)):
            newlimitx = (width-limit_mouse_x)  
        if (mouselimit == 'X+Y' and y < limit_mouse_y):
            newlimity = limit_mouse_y
        if (mouselimit == 'X+Y' and y > (height-limit_mouse_y)):
            newlimity = (height-limit_mouse_y)  
        
        if (mouselimit == 'X+Y' and (newlimitx != x or newlimity != y) and ind_limit_mouse==True):
            ctypes.windll.user32.SetCursorPos(newlimitx, newlimity)
        
        
        x_value, y_value = mouse_to_joystick(x, y)
        #count = threading.active_count()
        #print(f'[{count}] X: {str(x_value)} Y: {str(y_value)}')
        if (gamepadtype == 'Xbox 360'):
            y_value = y_value*-1

        comboside = combo.get()
        
        y_value_int = x_value_int = 0
        
        if (use_integer.get() == 1):
            if (x_value > 0): x_value_int = int(32767 * x_value)
            else: x_value_int = int(32768 * x_value)
            if (y_value > 0): y_value_int = int(32767 * y_value)
            else: y_value_int = int(32768 * y_value)
            
            x_value_int_full = (x_value-(-1))/(1-(-1))
     
        
        if (use_integer.get() == 0):
            if (comboside =='Left Stick'):
                gamepad.left_joystick_float(x_value_float=x_value, y_value_float=y_value)
                #gamepad.update()
            elif (comboside =='Left Stick-X'):
                gamepad.left_joystick_float(x_value_float=x_value, y_value_float=0.0)
            elif (comboside =='Left Stick-Y'):
                gamepad.left_joystick_float(x_value_float=0.0, y_value_float=y_value)
            elif(comboside =='Right Stick'):
                gamepad.right_joystick_float(x_value_float=x_value, y_value_float=y_value)
            elif (comboside =='Right Stick-X'):
                gamepad.right_joystick_float(x_value_float=x_value, y_value_float=0.0)
            elif (comboside =='Right Stick-Y'):
                gamepad.right_joystick_float(x_value_float=0.0, y_value_float=y_value)
            elif (comboside =='Left Stick-X + Left Trigger-Y'):
                gamepad.left_joystick_float(x_value_float=x_value, y_value_float=0.0)
                if (y_value > 0): y_value_trigger = int(255 * y_value)
                else: y_value_trigger = 0
                gamepad.left_trigger(value=round(y_value_trigger))
            elif (comboside =='Left Stick-X + Left Trigger-Y-Full'):
                gamepad.left_joystick_float(x_value_float=x_value, y_value_float=0.0)
                # PERCENT =  (ACTUAL_VALUE-MIN)/(MAX-MIN)
                y_value_trigger = (y_value-(-1))/(1-(-1))
                gamepad.left_trigger_float(value_float=y_value_trigger)
            elif (comboside =='Left Stick-X + Right Trigger-Y'):
                gamepad.left_joystick_float(x_value_float=x_value, y_value_float=0.0)
                if (y_value > 0): y_value_trigger = int(255 * y_value)
                else: y_value_trigger = 0
                gamepad.right_trigger(value=round(y_value_trigger))
            elif (comboside =='Left Stick-X + Right Trigger-Y-Full'):
                gamepad.left_joystick_float(x_value_float=x_value, y_value_float=0.0)
                y_value_trigger = (y_value-(-1))/(1-(-1))
                gamepad.right_trigger_float(value_float=y_value_trigger)
        else:
            if (comboside =='Left Stick'):
                gamepad.left_joystick(x_value=x_value_int, y_value=y_value_int)
            elif (comboside =='Left Stick-X'):
                gamepad.left_joystick(x_value=x_value_int, y_value=0)
            elif (comboside =='Left Stick-Y'):
                gamepad.left_joystick(x_value=0, y_value=y_value_int)
            elif(comboside =='Right Stick'):
                gamepad.right_joystick(x_value=x_value_int, y_value=y_value_int)
            elif (comboside =='Right Stick-X'):
                gamepad.right_joystick(x_value=x_value_int, y_value=0)
            elif (comboside =='Right Stick-Y'):
                gamepad.right_joystick(x_value=0, y_value=y_value_int)
            elif (comboside =='Left Stick-X + Left Trigger-Y'):
                gamepad.left_joystick(x_value=x_value_int, y_value=0)
                if (y_value > 0): y_value_trigger = int(255 * y_value)
                else: y_value_trigger = 0
                gamepad.left_trigger(value=round(y_value_trigger))
            elif (comboside =='Left Stick-X + Left Trigger-Y-Full'):
                gamepad.left_joystick(x_value=x_value_int, y_value=0)
                y_value_trigger = (y_value-(-1))/(1-(-1))
                gamepad.left_trigger_float(value_float=y_value_trigger)
            elif (comboside =='Left Stick-X + Right Trigger-Y'):
                gamepad.left_joystick(x_value=x_value_int, y_value=0)
                if (y_value > 0): y_value_trigger = int(255 * y_value)
                else: y_value_trigger = 0
                gamepad.right_trigger(value=round(y_value_trigger))
            elif (comboside =='Left Stick-X + Right Trigger-Y-Full'):
                gamepad.left_joystick(x_value=x_value_int, y_value=0)
                y_value_trigger = (y_value-(-1))/(1-(-1))
                gamepad.right_trigger_float(value_float=y_value_trigger)
              
       
        if(comboside =='Left Trigger-Y'):    
            if (y_value > 0): y_value = int(255 * y_value)
            else: y_value = 0
            gamepad.left_trigger(value=round(y_value))
        elif(comboside =='Right Trigger-Y'):    
            if (y_value > 0): y_value = int(255 * y_value)
            else: y_value = 0
            gamepad.right_trigger(value=round(y_value))
        elif(comboside =='Left Trigger-X'):    
            if (x_value > 0): x_value = int(255 * x_value)
            else: x_value = 0
            gamepad.left_trigger(value=round(x_value))
        elif(comboside =='Right Trigger-X'):    
            if (x_value > 0): x_value = int(255 * x_value)
            else: x_value = 0
            gamepad.right_trigger(value=round(x_value))
        
        #print(f'[{count}] X: {str(x_value)}   Y: {str(y_value)}')
        #gamepad.right_joystick_float(x_value_float=x_value, y_value_float=y_value)
        #if 'gamepad' in globals():
        gamepad.update()
        #time.sleep(0.01)  # Reduce CPU usage
        polling_time = spin_polling_time_var.get()
        time.sleep(polling_time)  # Reduce CPU usage
  
    gamepad = None
    listener.stop() 
    keyboard.unhook_all()
    #root.after(1, main_loop)
    #time.sleep(0.01)  # Reduce CPU usage

root = start_gui()



#root.after(1, main_loop)
root.mainloop()


'''
tabControl.select(1)
time.sleep(2)
tabControl.select(2)
tabControl.select(3)
tabControl.select(4)
tabControl.select(0)
'''