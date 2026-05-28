import sys, os
import configparser
import pyvjoystick.vigem as vg
import keyboard
#import mouse
#from pynput import mouse
import time
from logic import *

sys.dont_write_bytecode = True

keymap = configparser.ConfigParser()
keymap.read('keymap/default.ini')

cfg_block_keys = keymap.get('config','cfg_block_keys',  fallback='')
btn_off = keymap.get('config','btn_off',  fallback='')
btn_analog1x_left = keymap.get('config','btn_analog1x_left',  fallback='')
btn_analog1x_right = keymap.get('config','btn_analog1x_right',  fallback='')
btn_analog1y_down = keymap.get('config','btn_analog1y_down',  fallback='')
btn_analog1y_up = keymap.get('config','btn_analog1y_up',  fallback='')
btn_analog2x_left = keymap.get('config','btn_analog2x_left',  fallback='')
btn_analog2x_right = keymap.get('config','btn_analog2x_right',  fallback='')
btn_analog2y_down = keymap.get('config','btn_analog2y_down',  fallback='')
btn_analog2y_up = keymap.get('config','btn_analog2y_up',  fallback='')
btn_dpad_left = keymap.get('config','btn_dpad_left',  fallback='')
btn_dpad_right = keymap.get('config','btn_dpad_right',  fallback='')
btn_dpad_down = keymap.get('config','btn_dpad_down',  fallback='')
btn_dpad_up = keymap.get('config','btn_dpad_up',  fallback='')
btn_trigger_left = keymap.get('config','btn_trigger_left',  fallback='')
btn_trigger_right = keymap.get('config','btn_trigger_right',  fallback='')
btn_a = keymap.get('config','btn_a',  fallback='')
btn_b = keymap.get('config','btn_b',  fallback='')
btn_x = keymap.get('config','btn_x',  fallback='')
btn_y = keymap.get('config','btn_y',  fallback='')
btn_lb = keymap.get('config','btn_lb',  fallback='')
btn_rb = keymap.get('config','btn_rb',  fallback='')
btn_l3 = keymap.get('config','btn_l3',  fallback='')
btn_r3 = keymap.get('config','btn_r3',  fallback='')
btn_back = keymap.get('config','btn_back',  fallback='')
btn_start = keymap.get('config','btn_start',  fallback='')
btn_guide = keymap.get('config','btn_guide',  fallback='')

btn_stick_alternate_onoff = keymap.get('config','btn_stick_alternate_onoff',  fallback='')
#btn_stick_alternate_off = keymap.get('config','btn_stick_alternate_off',  fallback='')
btn_trigger_alternate_onoff = keymap.get('config','btn_trigger_alternate_onoff',  fallback='')
#btn_trigger_alternate_off = keymap.get('config','btn_trigger_alternate_off',  fallback='')

btn_trigger_left_low = keymap.get('config','btn_trigger_left_low',  fallback='')
btn_trigger_left_high = keymap.get('config','btn_trigger_left_high',  fallback='')
btn_trigger_right_low = keymap.get('config','btn_trigger_right_low',  fallback='')
btn_trigger_right_high = keymap.get('config','btn_trigger_right_high',  fallback='')
btn_trigger_left_reduce = keymap.get('config','btn_trigger_left_reduce',  fallback='')
btn_trigger_right_reduce = keymap.get('config','btn_trigger_right_reduce',  fallback='')



btn_analog1x_reset = keymap.get('config','btn_analog1x_reset',  fallback='')
btn_analog1y_reset = keymap.get('config','btn_analog1y_reset',  fallback='')
btn_analog2x_reset = keymap.get('config','btn_analog2x_reset',  fallback='')
btn_analog2y_reset = keymap.get('config','btn_analog2y_reset',  fallback='')



#btn_fixed_mouse_position_off = keymap.get('config','btn_fixed_mouse_position_off',  fallback='')
#btn_mouse_limit_off = keymap.get('config','btn_mouse_limit_off',  fallback='')

btn_analog1x_left_alt = keymap.get('config','btn_analog1x_left_alt',  fallback='')
btn_analog1x_right_alt = keymap.get('config','btn_analog1x_right_alt',  fallback='')
btn_analog1y_down_alt = keymap.get('config','btn_analog1y_down_alt',  fallback='')
btn_analog1y_up_alt = keymap.get('config','btn_analog1y_up_alt',  fallback='')
btn_analog2x_left_alt = keymap.get('config','btn_analog2x_left_alt',  fallback='')
btn_analog2x_right_alt = keymap.get('config','btn_analog2x_right_alt',  fallback='')
btn_analog2y_down_alt = keymap.get('config','btn_analog2y_down_alt',  fallback='')
btn_analog2y_up_alt = keymap.get('config','btn_analog2y_up_alt',  fallback='')

btn_analog1_autocenter_onoff = keymap.get('config','btn_analog1_autocenter_onoff',  fallback='')
btn_analog2_autocenter_onoff = keymap.get('config','btn_analog2_autocenter_onoff',  fallback='')
btn_trigger_left_autocenter_onoff = keymap.get('config','btn_trigger_left_autocenter_onoff',  fallback='')
btn_trigger_right_autocenter_onoff = keymap.get('config','btn_trigger_right_autocenter_onoff',  fallback='')
btn_fixed_mouse_position_onoff = keymap.get('config','btn_fixed_mouse_position_onoff',  fallback='')
btn_mouse_limit_onoff = keymap.get('config','btn_mouse_limit_onoff',  fallback='')
btn_modifier_switches_off = keymap.get('config','btn_modifier_switches_off',  fallback='')


btns = (btn_analog1x_left,
    btn_analog1x_right,
    btn_analog1y_down,
    btn_analog1y_up,
    btn_analog2x_left,
    btn_analog2x_right,
    btn_analog2y_down,
    btn_analog2y_up,
    btn_dpad_left,
    btn_dpad_right,
    btn_dpad_down,
    btn_dpad_up,
    btn_trigger_left,
    btn_trigger_right,
    btn_a,
    btn_b,
    btn_x,
    btn_y,
    btn_lb,
    btn_rb,
    btn_l3,
    btn_r3,
    btn_back,
    btn_start,
    btn_guide)
 
def blockkeyboard():
    for x in btns:
        keyboard.block_key(''+x+'')
        
def unblockkeyboard():
    for x in btns:
        keyboard.unblock_key(''+x+'')


def on_move(x, y):
    global gamepad
    #gamepad.left_trigger(value=x)
    gamepad.left_joystick(x_value=-10000, y_value=ly)
    gamepad.update()
    print(f'Mouse moved to ({x}, {y})')

# Collect events until released

'''
listener = mouse.Listener(
    on_move=on_move,
    #on_click=on_click,
    #on_scroll=on_scroll
    )
listener.start()
'''


rx = lx = ry = ly = lt = rt = caps = 0

lx_p = ly_p = False


def center_reduction(var_throttle,var_throttle_max,positive):

    center_percent_var = int(spin_center_percent.get())
    center_value_var = spin_center_value.get()
    
    
    #print(f'{var_throttle}|{center_percent_var}|{center_value_var}')
    
    var_center_reduction = 1.0
    if (center_percent_var != 0):
        center_internal_value = (var_throttle_max*center_percent_var)/100
        center_internal_value_neg = ((var_throttle_max*center_percent_var)/100)*-1
        if (var_throttle < center_internal_value and positive == True):
            var_center_reduction = center_value_var
        if (var_throttle > center_internal_value_neg and positive == False):
             var_center_reduction = center_value_var
    #print(f'{var_throttle}|{center_percent_var}|{center_internal_value}|{var_center_reduction}')
    return var_center_reduction
    
def mouse_click(btn):
    mouseleft_click = mousemiddle_click = mouseright_click = False
    if (win32api.GetAsyncKeyState(win32con.VK_LBUTTON) < 0 ):
        mouseleft_click = True
    if (win32api.GetAsyncKeyState(win32con.VK_MBUTTON) < 0 ):
        mousemiddle_click = True
    if (win32api.GetAsyncKeyState(win32con.VK_RBUTTON) < 0 ):
        mouseright_click = True
        
    mouseleft_cfg = combomouseleft.get() 
    mousemiddle_cfg = combomousemiddle.get() 
    mouseright_cfg = combomouseright.get() 
    
    if (mouseleft_click and mouseleft_cfg == btn):
        return True
    if (mousemiddle_click and mousemiddle_cfg == btn):
        return True
    if (mouseright_click and mouseright_cfg == btn):
        return True  
        
    return False
    
    

def detectkeyboard(list_pressed):
    global gamepad
    global keyboard
    global mouse
    global lt
    global rt
    global throttle
    global throttle
    global throttle_y
    global throttle_rx
    global throttle_ry
    global throttle_increase_rate
    global throttle_max
    global throttle_min
    global ind_stick_alternate
    global ind_trigger_alternate
    global start_f12
    
    global ind_fixed_mouse
    global ind_limit_mouse
    
    global use_autocenter_stick_left
    
    
    if gamepad is None:
        return
    
    list_pressed = [str(x) for x in list_pressed]
    
    
    '''
    if keyboard.is_pressed('F12'):
        print('Exiting gamepad1')
        start_f12 = 0
        toggle_emulation()
    '''    
    if '88' in list_pressed:
        print('Exiting gamepad-2')
        start_f12 = 0
        toggle_emulation()
        
    throttle_increase_time = int(spin_inc_time.get())
    throttle_decrease_time = int(spin_dec_time.get())
    
    trigger_increase_time_left = int(spin_inc_key_left.get())
    trigger_increase_time_right = int(spin_inc_key_right.get())
    trigger_decrease_time_left = int(spin_dec_key_left.get())
    trigger_decrease_time_right = int(spin_dec_key_right.get())
    
    stick_turbo = float(spin_stick_turbo.get())
    trigger_slow_left = float(spin_trigger_slow_left.get())
    trigger_slow_right = float(spin_trigger_slow_right.get())
    
    trigger_increase_rate_left  = calculate_rate(255, trigger_increase_time_left)
    trigger_increase_rate_right = calculate_rate(255, trigger_increase_time_right)
    
    trigger_decrease_rate_left  = calculate_rate(255, trigger_decrease_time_left)
    trigger_decrease_rate_right = calculate_rate(255, trigger_decrease_time_right)
    
    
    stick_alternative_speed = spin_stick_alternative_speed_var.get()
    
    
    
    
    #print('trigger_increase_rate:'+str(trigger_increase_rate))
    #print('trigger_decrease_rate:'+str(trigger_decrease_rate))
    
    
    throttle_increase_rate = calculate_rate(throttle_max, throttle_increase_time)
    throttle_decrease_rate = calculate_rate(throttle_max, throttle_decrease_time) * -1
    
    
    #if '58' in list_pressed:
    #   throttle_increase_rate = calculate_rate(throttle_max, throttle_increase_time) * 2
    
    #print(globals())
    
    #DEBUG KEYS
    #for k, v in list(locals().items()):
    #    print(f'[{k}] - [{v}]')

    
    if btn_analog1_autocenter_onoff in list_pressed and btn_modifier_switches_off in list_pressed:
        swtiches(lbl1_swtich,lbl1_var,'OFF')
        use_autocenter_stick_left.set(0)
    elif btn_analog1_autocenter_onoff in list_pressed:
        swtiches(lbl1_swtich,lbl1_var,'ON')
        use_autocenter_stick_left.set(1)
            
    if btn_analog2_autocenter_onoff in list_pressed and btn_modifier_switches_off in list_pressed:
        swtiches(lbl2_swtich,lbl2_var,'OFF')
        use_autocenter_stick_right.set(0)
    elif btn_analog2_autocenter_onoff in list_pressed:
        swtiches(lbl2_swtich,lbl2_var,'ON')
        use_autocenter_stick_right.set(1)
            
    # TRIGGERS 
    if btn_trigger_left_autocenter_onoff in list_pressed and btn_modifier_switches_off in list_pressed:
        swtiches(lbl3_swtich,lbl3_var,'OFF')
        use_autocenter_trigger_left.set(0)
    elif btn_trigger_left_autocenter_onoff in list_pressed:
        swtiches(lbl3_swtich,lbl3_var,'ON')
        use_autocenter_trigger_left.set(1)
            
    if btn_trigger_right_autocenter_onoff in list_pressed and btn_modifier_switches_off in list_pressed:
        swtiches(lbl4_swtich,lbl4_var,'OFF')
        use_autocenter_trigger_right.set(0)
    elif btn_trigger_right_autocenter_onoff in list_pressed:
        swtiches(lbl4_swtich,lbl4_var,'ON')
        use_autocenter_trigger_right.set(1)        
            
    
    # FIXED MOUSE ON OFF
    if 'ind_fixed_mouse' not in globals():
        ind_fixed_mouse = False
    if btn_fixed_mouse_position_onoff in list_pressed and btn_modifier_switches_off in list_pressed:
        ind_fixed_mouse = False
        swtiches(lbl5_swtich,lbl5_var,'OFF')
    elif btn_fixed_mouse_position_onoff in list_pressed:
        ind_fixed_mouse = True
        swtiches(lbl5_swtich,lbl5_var,'ON')
        
    #if btn_fixed_mouse_position_off in list_pressed:
    #    ind_fixed_mouse = False
        
        
    # LIMIT MOUSE  MOUSE ON OFF
    if 'ind_limit_mouse' not in globals():
        ind_limit_mouse = False
    if btn_mouse_limit_onoff in list_pressed and btn_modifier_switches_off in list_pressed:
        ind_limit_mouse = False
        swtiches(lbl6_swtich,lbl6_var,'OFF')
    elif btn_mouse_limit_onoff in list_pressed:
        ind_limit_mouse = True
        swtiches(lbl6_swtich,lbl6_var,'ON')
            
    #if btn_mouse_limit_off in list_pressed:
    #    ind_limit_mouse = False
    
    
    if 'ind_stick_alternate' not in globals():
        ind_stick_alternate = False
    if btn_stick_alternate_onoff in list_pressed and btn_modifier_switches_off in list_pressed:
        ind_stick_alternate = False
        swtiches(lbl7_swtich,lbl7_var,'OFF')
    elif btn_stick_alternate_onoff in list_pressed:
        ind_stick_alternate = True
        swtiches(lbl7_swtich,lbl7_var,'ON')
    if (ind_stick_alternate == True):
        throttle_increase_rate = calculate_rate(throttle_max, throttle_increase_time)  * float(stick_turbo)
        #throttle_increase_rate = calculate_rate(throttle_max, throttle_increase_time)  * 2
        
        
    if 'ind_trigger_alternate' not in globals():
        ind_trigger_alternate = False    
        
    if btn_trigger_alternate_onoff in list_pressed and btn_modifier_switches_off in list_pressed:
        ind_trigger_alternate = False
        swtiches(lbl8_swtich,lbl8_var,'OFF')
    elif btn_trigger_alternate_onoff in list_pressed:
        ind_trigger_alternate = True
        swtiches(lbl8_swtich,lbl8_var,'ON')
    if (ind_trigger_alternate == True):
        trigger_increase_rate_left =  calculate_rate(255, trigger_increase_time_left) * float(trigger_slow_left)
        trigger_increase_rate_right =  calculate_rate(255, trigger_increase_time_right) * float(trigger_slow_right)
        trigger_decrease_rate_left  = calculate_rate(255, trigger_decrease_time_left)  * float(trigger_slow_left)
        trigger_decrease_rate_right = calculate_rate(255, trigger_decrease_time_right) * float(trigger_slow_right)
        
        
  
    #print(f'ind:{ind_trigger_alternate} Throttle:{trigger_increase_rate_left}')
    #print(f'ind:{ind_stick_alternate} Throttle:{throttle_increase_rate}')
    
    mouseleft_click = mousemiddle_click = mouseright_click = False
    if (win32api.GetAsyncKeyState(win32con.VK_LBUTTON) < 0 ):
        mouseleft_click = True
    if (win32api.GetAsyncKeyState(win32con.VK_MBUTTON) < 0 ):
        mousemiddle_click = True
    if (win32api.GetAsyncKeyState(win32con.VK_RBUTTON) < 0 ):
        mouseright_click = True
        
    mouseleft_cfg = combomouseleft.get() 
    mousemiddle_cfg = combomousemiddle.get() 
    mouseright_cfg = combomouseright.get() 
    
    mousecenterposition = combomousecenterposition.get()
    x, y = win32api.GetCursorPos()
    
    if(mouse_click('Center Mouse') and mousecenterposition =='X+Y'):
        print('centrando X+Y')
        win32api.SetCursorPos((center_x, center_y))
    elif(mouse_click('Center Mouse') and mousecenterposition =='X'):
        print('centrando X+Y')
        win32api.SetCursorPos((center_x, y))
    elif(mouse_click('Center Mouse') and mousecenterposition =='Y'):
        print('centrando X+Y')
        win32api.SetCursorPos((x, center_y))
       
    if btn_a in list_pressed or mouse_click('A'):
        gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
    else:
        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
        
    if btn_b in list_pressed or mouse_click('B'):
        gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
    else:
        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
        
    if btn_x in list_pressed or mouse_click('X'):
        gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_X)
    else:
        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_X)

    if btn_y in list_pressed or mouse_click('Y'):
        gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)
    else:
        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)
        
    if btn_lb in list_pressed or mouse_click('LB'):
        gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER)
    else:
        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER)
        
    if btn_rb in list_pressed or mouse_click('RB'):
        gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER)
    else:
        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER)
        
    if btn_r3 in list_pressed or mouse_click('R3'):
        gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_THUMB)
    else:
        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_THUMB)
        
    if btn_l3 in list_pressed or mouse_click('L3'):
        gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB)
    else:
        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB)
        
    if btn_back in list_pressed or mouse_click('Back'):
        gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_BACK)
    else:
        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_BACK)
    
    if btn_start in list_pressed or mouse_click('Start'):
        gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_START)
    else:
        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_START)  
    
    if btn_guide in list_pressed or mouse_click('Guide'):
        gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_GUIDE)
    else:
        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_GUIDE)  
        
    # DPAD
    if btn_dpad_left in list_pressed:
        gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT)
    else:
        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT)
        
    if btn_dpad_right in list_pressed:
        gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT)
    else:
        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT)

    if btn_dpad_down in list_pressed:
        gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN)
    else:
        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN)
    
    if btn_dpad_up in list_pressed:
        gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP)
    else:
        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP)
    
    
    # LEFT TRIGGER    
    if btn_trigger_left_high in list_pressed:
        lt = 255 * float(spin_trigger_hold_high_left.get())
    elif btn_trigger_left_low in list_pressed:
        lt = 255 * float(spin_trigger_hold_low_left.get())
    elif mouseleft_click and mouseleft_cfg == 'Left Trigger':
        lt = lt + round(trigger_increase_rate_left)
    elif mousemiddle_click and mousemiddle_cfg == 'Left Trigger':
        lt = lt + round(trigger_increase_rate_left)
    elif mouseright_click and mouseright_cfg == 'Left Trigger':
        lt = lt + round(trigger_increase_rate_left)
    elif btn_trigger_left in list_pressed:
        lt = lt + round(trigger_increase_rate_left)
    elif (btn_trigger_left_reduce in list_pressed and use_autocenter_trigger_left.get() == 0): 
        lt = lt + round(trigger_decrease_rate_left)*-1
    elif (lt > 0 and use_autocenter_trigger_left.get() == 1): 
        lt = lt + round(trigger_decrease_rate_left)*-1
    #else:
    #    lt = 0
        
    if lt > 255:
        lt = 255
    elif lt < 0:
        lt = 0 
    comboside = combo.get()
    combowheelval = combowheel.get()
    if (comboside !='Left Trigger-X' and comboside !='Left Trigger-X' and combowheelval !='Left Trigger'):
        gamepad.left_trigger(value=round(lt))
        
    # RIGHT TRIGGER
    
 
    
    
    
    
    if btn_trigger_right_high in list_pressed:
        rt = 255 * float(spin_trigger_hold_high_right.get())
    elif btn_trigger_right_low in list_pressed:
        rt = 255 * float(spin_trigger_hold_low_right.get())
    elif mouseleft_click and mouseleft_cfg == 'Right Trigger':
        rt = rt + round(trigger_increase_rate_right)
    elif mousemiddle_click and mousemiddle_cfg == 'Right Trigger':
        rt = rt + round(trigger_increase_rate_right)
    elif mouseright_click and mouseright_cfg == 'Right Trigger':
        rt = rt + round(trigger_increase_rate_right)
    elif btn_trigger_right in list_pressed:
        rt = rt + round(trigger_increase_rate_right)
    elif (btn_trigger_right_reduce in list_pressed  and use_autocenter_trigger_right.get() == 0): 
        rt = rt + round(trigger_decrease_rate_right)*-1
    elif (rt > 0 and use_autocenter_trigger_right.get() == 1): 
        rt = rt + round(trigger_decrease_rate_right)*-1
    #else:
    #    rt = 0
        
    if rt > 255:
        rt = 255
    elif rt < 0:
        rt = 0 
    if (comboside !='Right Trigger-X' and comboside !='Right Trigger-Y' and combowheelval !='Right Trigger'):
        gamepad.right_trigger(value=round(rt))
        
        
    stick_limit_response_type = combo_stick_limit_response_type.get()    
    stick_alternative_limit_var = spin_stick_alternative_limit_var.get()

   
    if btn_analog1x_reset in list_pressed:
        throttle = int(combo_reset_left_x.get())
    elif btn_analog1x_left in list_pressed:
        if (throttle > 0 and use_autocenter_stick_left.get() == 1):
            throttle = throttle + round(throttle_decrease_rate *4)
        elif (throttle > 0):
            throttle = throttle + round(throttle_decrease_rate)
        else:
            multiply_center = center_reduction(throttle,throttle_max,False)
            throttle_increase_rate = float(throttle_increase_rate)*float(multiply_center)
            throttle = throttle + throttle_increase_rate  * -1
            
            
    elif btn_analog1x_right in list_pressed:
        if (throttle < 0  and use_autocenter_stick_left.get() == 1):
            throttle = throttle - round(throttle_decrease_rate *4)
        elif (throttle < 0):
            throttle = throttle - round(throttle_decrease_rate)
        else:
            multiply_center = center_reduction(throttle,throttle_max,True)
            throttle_increase_rate = float(throttle_increase_rate)*float(multiply_center)
            throttle = throttle + throttle_increase_rate  * +1
            
    ###########################
    # BLOCO ANALOG LEFT X ALTERNATIVE 
    ###########################
    elif btn_analog1x_left_alt in list_pressed and stick_limit_response_type == 'Default':
        if (throttle > 0 and use_autocenter_stick_left.get() == 1):
            throttle = throttle + round(throttle_decrease_rate *4)
        elif (throttle > 0):
            throttle = throttle + round(throttle_decrease_rate)
        else:
            multiply_center = center_reduction(throttle,throttle_max,False)
            throttle_increase_rate = float(throttle_increase_rate)*float(multiply_center)
            throttle_increase_rate = throttle_increase_rate*stick_alternative_speed
            throttle = throttle + throttle_increase_rate  * -1
            if throttle < (int32_max*-1-1)*stick_alternative_limit_var:
                throttle = (int32_max*-1-1)*stick_alternative_limit_var    
    elif btn_analog1x_right_alt in list_pressed and stick_limit_response_type == 'Default':
        if (throttle < 0  and use_autocenter_stick_left.get() == 1):
            throttle = throttle - round(throttle_decrease_rate *4)
        elif (throttle < 0):
            throttle = throttle - round(throttle_decrease_rate)
        else:
            multiply_center = center_reduction(throttle,throttle_max,True)
            throttle_increase_rate = float(throttle_increase_rate)*float(multiply_center)
            throttle_increase_rate = throttle_increase_rate*stick_alternative_speed
            throttle = throttle + throttle_increase_rate  * +1
            if throttle > throttle_max*stick_alternative_limit_var:
                throttle = throttle_max*stick_alternative_limit_var
    elif btn_analog1x_left_alt in list_pressed and stick_limit_response_type == 'Direct':
        throttle = (int32_max*-1-1)*stick_alternative_limit_var
    elif btn_analog1x_right_alt in list_pressed and stick_limit_response_type == 'Direct':
        throttle =  throttle_max*stick_alternative_limit_var
    ###########################
    # END BLOCO ANALOG LEFT X ALTERNATIVE 
    ###########################
    
    elif (throttle < 0 and use_autocenter_stick_left.get() == 1): 
        throttle = throttle - round(throttle_decrease_rate *2)
        if(throttle >= round(throttle_decrease_rate *2)*+1):
            throttle =0
            
    elif (throttle > 0 and use_autocenter_stick_left.get() == 1): 
        throttle = throttle + round(throttle_decrease_rate *2)
        if(throttle <= round(throttle_decrease_rate *2)):
            throttle =0
            
    if throttle > throttle_max:
        throttle = throttle_max
    elif throttle < (int32_max*-1-1):
        throttle = (int32_max*-1-1) 
        
     
    # TRATAMENTO Y
    if btn_analog1y_reset in list_pressed:
        throttle_y = int(combo_reset_left_y.get())
    elif btn_analog1y_down in list_pressed:
        #gamepad.left_joystick(x_value=-32768, y_value=ly)
        if (throttle_y > 0 and use_autocenter_stick_left.get() == 1):
            throttle_y = throttle_y + round(throttle_decrease_rate *4)
        elif (throttle_y > 0):
            throttle_y = throttle_y + round(throttle_decrease_rate)
        else:
            multiply_center = center_reduction(throttle,throttle_max,False)
            throttle_increase_rate = float(throttle_increase_rate)*float(multiply_center)
            throttle_y = throttle_y + throttle_increase_rate  * -1
            
    elif btn_analog1y_up in list_pressed:
        if (throttle_y < 0 and use_autocenter_stick_left.get() == 1):
            throttle_y = throttle_y - round(throttle_decrease_rate *4)
        elif (throttle_y < 0):
            throttle_y = throttle_y - round(throttle_decrease_rate)
        else:
            multiply_center = center_reduction(throttle,throttle_max,True)
            throttle_increase_rate = float(throttle_increase_rate)*float(multiply_center)
            throttle_y = throttle_y + throttle_increase_rate  * +1
    
    ###########################
    # BLOCO ANALOG LEFT Y ALTERNATIVE 
    ###########################
    elif btn_analog1y_down_alt in list_pressed and stick_limit_response_type == 'Default':
        if (throttle_y > 0 and use_autocenter_stick_left.get() == 1):
            throttle_y = throttle_y + round(throttle_decrease_rate *4)
        elif (throttle_y > 0):
            throttle_y = throttle_y + round(throttle_decrease_rate)
        else:
            multiply_center = center_reduction(throttle,throttle_max,False)
            throttle_increase_rate = float(throttle_increase_rate)*float(multiply_center)
            throttle_increase_rate = throttle_increase_rate*stick_alternative_speed
            throttle_y = throttle_y + throttle_increase_rate  * -1
            if throttle_y < (int32_max*-1-1)*stick_alternative_limit_var:
                throttle_y = (int32_max*-1-1)*stick_alternative_limit_var     
    elif btn_analog1y_up_alt in list_pressed and stick_limit_response_type == 'Default':
        if (throttle_y < 0 and use_autocenter_stick_left.get() == 1):
            throttle_y = throttle_y - round(throttle_decrease_rate *4)
        elif (throttle_y < 0):
            throttle_y = throttle_y - round(throttle_decrease_rate)
        else:
            multiply_center = center_reduction(throttle,throttle_max,True)
            throttle_increase_rate = float(throttle_increase_rate)*float(multiply_center)
            throttle_increase_rate = throttle_increase_rate*stick_alternative_speed
            throttle_y = throttle_y + throttle_increase_rate  * +1
            if throttle_y > throttle_max*stick_alternative_limit_var:
                throttle_y = throttle_max*stick_alternative_limit_var
    elif btn_analog1y_down_alt in list_pressed and stick_limit_response_type == 'Direct':
        throttle_y = (int32_max*-1-1)*stick_alternative_limit_var
    elif btn_analog1y_up_alt in list_pressed and stick_limit_response_type == 'Direct':
        throttle_y = throttle_max*stick_alternative_limit_var
    ###########################
    # END BLOCO ANALOG LEFT Y ALTERNATIVE 
    ###########################

   
    elif (throttle_y < 0 and use_autocenter_stick_left.get() == 1): 
        throttle_y = throttle_y - round(throttle_decrease_rate *2)
        if(throttle_y >= round(throttle_decrease_rate *2)*+1):
            throttle_y =0
            
    elif (throttle_y > 0 and use_autocenter_stick_left.get() == 1): 
        throttle_y = throttle_y + round(throttle_decrease_rate *2)
        if(throttle_y <= round(throttle_decrease_rate *2)):
            throttle_y =0
            
    if throttle_y > throttle_max:
        throttle_y = throttle_max
    elif throttle_y < (int32_max*-1-1):
        throttle_y = (int32_max*-1-1)     
        

    if (comboside !='Left Stick' and
        comboside !='Left Stick-X' and
        comboside !='Left Stick-Y'
        ):
        gamepad.left_joystick(x_value=int(throttle), y_value=int(throttle_y))
        
   
    
    # ANALOG R X
    if btn_analog2x_reset in list_pressed:
        throttle_rx = int(combo_reset_right_x.get())
    elif btn_analog2x_left in list_pressed:
        if (throttle_rx > 0 and use_autocenter_stick_right.get() == 1):
            throttle_rx = throttle_rx + round(throttle_decrease_rate *4)
        elif (throttle_rx > 0):
            throttle_rx = throttle_rx + round(throttle_decrease_rate)
        else:
            multiply_center = center_reduction(throttle,throttle_max,False)
            throttle_increase_rate = float(throttle_increase_rate)*float(multiply_center)
            throttle_rx = throttle_rx + throttle_increase_rate  * -1
            
    elif btn_analog2x_right in list_pressed:
        if (throttle_rx < 0 and use_autocenter_stick_right.get() == 1):
            throttle_rx = throttle_rx - round(throttle_decrease_rate *4)
        elif (throttle_rx < 0):
            throttle_rx = throttle_rx - round(throttle_decrease_rate)
        else:
            multiply_center = center_reduction(throttle,throttle_max,True)
            throttle_increase_rate = float(throttle_increase_rate)*float(multiply_center)
            throttle_rx = throttle_rx + throttle_increase_rate  * +1
    ###########################
    # BLOCO ANALOG RIGHT X ALTERNATIVE 
    ###########################
    elif btn_analog2x_left_alt in list_pressed and stick_limit_response_type == 'Default':
        if (throttle_rx > 0 and use_autocenter_stick_right.get() == 1):
            throttle_rx = throttle_rx + round(throttle_decrease_rate *4)
        elif (throttle_rx > 0):
            throttle_rx = throttle_rx + round(throttle_decrease_rate)
        else:
            multiply_center = center_reduction(throttle,throttle_max,False)
            throttle_increase_rate = float(throttle_increase_rate)*float(multiply_center)
            throttle_increase_rate = throttle_increase_rate*stick_alternative_speed
            throttle_rx = throttle_rx + throttle_increase_rate  * -1
            if throttle_rx < (int32_max*-1-1)*stick_alternative_limit_var:
                throttle_rx = (int32_max*-1-1)*stick_alternative_limit_var
            
    elif btn_analog2x_right_alt in list_pressed and stick_limit_response_type == 'Default':
        if (throttle_rx < 0 and use_autocenter_stick_right.get() == 1):
            throttle_rx = throttle_rx - round(throttle_decrease_rate *4)
        elif (throttle_rx < 0):
            throttle_rx = throttle_rx - round(throttle_decrease_rate)
        else:
            multiply_center = center_reduction(throttle,throttle_max,True)
            throttle_increase_rate = float(throttle_increase_rate)*float(multiply_center)
            throttle_increase_rate = throttle_increase_rate*stick_alternative_speed
            throttle_rx = throttle_rx + throttle_increase_rate  * +1
            if throttle_rx > throttle_max*stick_alternative_limit_var:
                throttle_rx = throttle_max*stick_alternative_limit_var
                
    elif btn_analog2x_left_alt in list_pressed and stick_limit_response_type == 'Direct':
        throttle_rx = (int32_max*-1-1)*stick_alternative_limit_var
    elif btn_analog2x_right_alt in list_pressed and stick_limit_response_type == 'Direct':
        throttle_rx = throttle_max*stick_alternative_limit_var
    ###########################
    # END BLOCO ANALOG RIGHT X ALTERNATIVE 
    ###########################
    
    elif (throttle_rx < 0 and use_autocenter_stick_right.get() == 1): 
        throttle_rx = throttle_rx - round(throttle_decrease_rate *2)
        if(throttle_rx >= round(throttle_decrease_rate *2)*+1):
            throttle_rx =0
            
    elif (throttle_rx > 0 and use_autocenter_stick_right.get() == 1): 
        throttle_rx = throttle_rx + round(throttle_decrease_rate *2)
        if(throttle_rx <= round(throttle_decrease_rate *2)):
            throttle_rx =0
            
    if throttle_rx > throttle_max:
        throttle_rx = throttle_max
    elif throttle_rx < (int32_max*-1-1):
        throttle_rx = (int32_max*-1-1) 
        
        
    # TRATAMENTO Y
    if btn_analog2y_reset in list_pressed:
        throttle_ry = int(combo_reset_right_y.get())
    elif btn_analog2y_down in list_pressed:
        #gamepad.left_joystick(x_value=-32768, y_value=ly)
        if (throttle_ry > 0 and use_autocenter_stick_right.get() == 1):
            throttle_ry = throttle_ry + round(throttle_decrease_rate *4)
        elif (throttle_ry > 0):
            throttle_ry = throttle_ry + round(throttle_decrease_rate)
        else:
            multiply_center = center_reduction(throttle,throttle_max,False)
            throttle_increase_rate = float(throttle_increase_rate)*float(multiply_center)
            throttle_ry = throttle_ry + throttle_increase_rate  * -1
            
    elif btn_analog2y_up in list_pressed:
        if (throttle_ry < 0 and use_autocenter_stick_right.get() == 1):
            throttle_ry = throttle_ry - round(throttle_decrease_rate *4)
        elif (throttle_ry < 0):
            throttle_ry = throttle_ry - round(throttle_decrease_rate)
        else:
            multiply_center = center_reduction(throttle,throttle_max,True)
            throttle_increase_rate = float(throttle_increase_rate)*float(multiply_center)
            throttle_ry = throttle_ry + throttle_increase_rate  * +1
    
    ###########################
    # BLOCO ANALOG RIGHT Y ALTERNATIVE 
    ###########################
    elif btn_analog2y_down_alt in list_pressed and stick_limit_response_type == 'Default':
        #gamepad.left_joystick(x_value=-32768, y_value=ly)
        if (throttle_ry > 0 and use_autocenter_stick_right.get() == 1):
            throttle_ry = throttle_ry + round(throttle_decrease_rate *4)
        elif (throttle_ry > 0):
            throttle_ry = throttle_ry + round(throttle_decrease_rate)
        else:
            multiply_center = center_reduction(throttle,throttle_max,False)
            throttle_increase_rate = float(throttle_increase_rate)*float(multiply_center)
            throttle_increase_rate = throttle_increase_rate*stick_alternative_speed
            throttle_ry = throttle_ry + throttle_increase_rate  * -1
            if throttle_ry < (int32_max*-1-1)*stick_alternative_limit_var:
                throttle_ry = (int32_max*-1-1)*stick_alternative_limit_var     
            
            
    elif btn_analog2y_up_alt in list_pressed and stick_limit_response_type == 'Default':
        if (throttle_ry < 0 and use_autocenter_stick_right.get() == 1):
            throttle_ry = throttle_ry - round(throttle_decrease_rate *4)
        elif (throttle_ry < 0):
            throttle_ry = throttle_ry - round(throttle_decrease_rate)
        else:
            multiply_center = center_reduction(throttle,throttle_max,True)
            throttle_increase_rate = float(throttle_increase_rate)*float(multiply_center)
            throttle_increase_rate = throttle_increase_rate*stick_alternative_speed
            throttle_ry = throttle_ry + throttle_increase_rate  * +1
            if throttle_ry > throttle_max*stick_alternative_limit_var:
                throttle_ry = throttle_max*stick_alternative_limit_var
            
    elif btn_analog2y_down_alt in list_pressed and stick_limit_response_type == 'Direct':
        throttle_ry = (int32_max*-1-1)*stick_alternative_limit_var
    elif btn_analog2y_up_alt in list_pressed and stick_limit_response_type == 'Direct':
        throttle_ry = throttle_max*stick_alternative_limit_var
     
    ###########################
    # END BLOCO ANALOG RIGHT Y ALTERNATIVE 
    ###########################
    
    
    elif (throttle_ry < 0 and use_autocenter_stick_right.get() == 1): 
        throttle_ry = throttle_ry - round(throttle_decrease_rate *2)
        if(throttle_ry >= round(throttle_decrease_rate *2)*+1):
            throttle_ry =0
            
    elif (throttle_ry > 0 and use_autocenter_stick_right.get() == 1): 
        throttle_ry = throttle_ry + round(throttle_decrease_rate *2)
        if(throttle_ry <= round(throttle_decrease_rate *2)):
            throttle_ry =0
            
    if throttle_ry > throttle_max:
        throttle_ry = throttle_max
    elif throttle_ry < (int32_max*-1-1):
        throttle_ry = (int32_max*-1-1)     
    comboside = combo.get()
    if (comboside !='Right Stick' and
        comboside !='Right Stick-X' and
        comboside !='Right Stick-Y'
        ):
        gamepad.right_joystick(x_value=int(throttle_rx), y_value=int(throttle_ry))


    
    #gamepad.update()
    #time.sleep(0.01)
    
 