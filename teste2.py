'''
import tkinter as tk

root = tk.Tk()
root.geometry("300x200")

# Create a top frame
top_frame = tk.Frame(root, bg="lightblue", bd=2, relief="sunken")
top_frame.pack(side="top", fill="both", expand=True)

# Create a bottom frame
bottom_frame = tk.Frame(root, bg="lightgrey", bd=2, relief="raised")
bottom_frame.pack(side="bottom", fill="both", expand=True)

# Place widgets inside the frames
tk.Button(top_frame, text="Button in Top").pack(pady=10)
tk.Button(bottom_frame, text="Button in Bottom").pack(pady=10)

root.mainloop()
'''
import tkinter as tk
from tkinter import ttk, Canvas, messagebox
import win32api
import os, subprocess
import configparser

sys.dont_write_bytecode = True

config = configparser.ConfigParser()

# Global Settings
deadzone = 0.1  
x_sensitivity = 1.0
y_sensitivity = 1.0
is_running = False

width, height = win32api.GetSystemMetrics(0), win32api.GetSystemMetrics(1)
center_x = width // 2
center_y = height // 2


def update_keys():
    global btn_analog1x_left, \
        btn_analog1x_right, \
        btn_analog1y_down,  \
        btn_analog1y_up, \
        btn_analog2x_left, \
        btn_analog2x_right, \
        btn_analog2y_down, \
        btn_analog2y_up, \
        btn_dpad_left, \
        btn_dpad_right, \
        btn_dpad_down, \
        btn_dpad_up, \
        btn_trigger_left, \
        btn_trigger_right, \
        btn_a, \
        btn_b, \
        btn_x, \
        btn_y, \
        btn_lb, \
        btn_rb, \
        btn_l3, \
        btn_r3, \
        btn_back, \
        btn_start, \
        btn_guide, \
        btn_stick_alternate_onoff, \
        btn_trigger_alternate_onoff, \
        btn_trigger_left_low,\
        btn_trigger_left_high,\
        btn_trigger_right_low,\
        btn_trigger_right_high,\
        btn_trigger_left_reduce,\
        btn_trigger_right_reduce,\
        btn_analog1x_reset,\
        btn_analog1y_reset,\
        btn_analog2x_reset,\
        btn_analog2y_reset,\
        btn_analog1x_left_alt,btn_analog1x_right_alt,btn_analog1y_down_alt,btn_analog1y_up_alt,btn_analog2x_left_alt,btn_analog2x_right_alt,btn_analog2y_down_alt,btn_analog2y_up_alt,btn_analog1_autocenter_onoff,btn_analog2_autocenter_onoff,\
        btn_trigger_left_autocenter_onoff,\
        btn_trigger_right_autocenter_onoff,\
        btn_fixed_mouse_position_onoff,\
        btn_mouse_limit_onoff,\
        btn_modifier_switches_off

        
        
    keymap_file = combokey.get()
    if (not os.path.exists(f'keymap/{keymap_file}.ini') and not os.path.exists(f'keymap/default.ini')):
        messagebox.showwarning("Error", f"File {keymap_file}.ini and default.ini do not exist in keymap folder")
    else: 
        if (not os.path.exists(f'keymap/{keymap_file}.ini') and os.path.exists(f'keymap/default.ini')):
            keymap_file = 'default'
            
        keymap = configparser.ConfigParser()
        keymap.read(f'keymap/{keymap_file}.ini')

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
        
        
        

def load_profile():
    global deadzone_scale_var
    profile_name = profilecombo.get()
    
    if (profile_name == ''):
        messagebox.showwarning("Error", "Profile name cannot be empty")
    elif (not os.path.exists(f'profile/{profile_name}.ini')):
        messagebox.showwarning("Error", f"File {profile_name}.ini do not exist in profile folder")
    else:
        config.read(f'profile/{profile_name}.ini')
        gamepadtype_var = config.get('config','gamepadtype',  fallback='')
        keymap_var = config.get('config','keymap',  fallback='')
        mouse_var = config.get('config','mouse',  fallback='')
        mousewheel_var = config.get('config','mousewheel',  fallback='')
        use_integer_var = config.get('config','use_integer',  fallback='')
        mousefixed_var = config.get('config','mousefixed',  fallback='')
        mouse_x_position_var2 = config.get('config','mouse_x_position',  fallback='')
        mouse_y_position_var2 = config.get('config','mouse_y_position',  fallback='')
        
        
        deadzone_scale_var2 = config.get('config','deadzone_scale',  fallback='')
        x_sens_scale_var2 = config.get('config','x_sens_scale',  fallback='')
        y_sens_scale_var2 = config.get('config','y_sens_scale',  fallback='')
        spin_inc_wheel_var2 = config.get('config','spin_inc_wheel',  fallback='')
        spin_dec_wheel_var2 = config.get('config','spin_dec_wheel',  fallback='')
        spin_inc_time_var2 = config.get('config','spin_inc_time',  fallback='')
        spin_dec_time_var2 = config.get('config','spin_dec_time',  fallback='')
        
        spin_inc_key_var2_left = config.get('config','spin_inc_key_left',  fallback='')
        spin_inc_key_var2_right = config.get('config','spin_inc_key_right',  fallback='')
        spin_dec_key_var2_left = config.get('config','spin_dec_key_left',  fallback='')
        spin_dec_key_var2_right = config.get('config','spin_dec_key_right',  fallback='')
        spin_center_percent_var2 = config.get('config','spin_center_percent',  fallback='')
        spin_center_value_var2 = config.get('config','spin_center_value',  fallback='')
        #combo_center_type_var2 = config.get('config','combo_center_type',  fallback='')
        
        limitmouse_var2 = config.get('config','limitmouse',  fallback='')
        limit_mouse_x_position_var2 = config.get('config','limit_mouse_x_position',  fallback='')
        limit_mouse_y_position_var2 = config.get('config','limit_mouse_y_position',  fallback='')
        
        mouseleft_var2 = config.get('config',' mouseleft',  fallback='')
        mousemiddle_var2 = config.get('config','mousemiddle',  fallback='')
        mouseright_var2 = config.get('config','mouseright',  fallback='')
        trigger_hold_high_left_var2 = config.get('config','trigger_hold_high_left',  fallback='')
        trigger_hold_low_left_var2 = config.get('config','trigger_hold_low_left',  fallback='')
        trigger_slow_left_var2 = config.get('config','trigger_slow_left',  fallback='')
        trigger_hold_high_right_var2 = config.get('config','trigger_hold_high_right',  fallback='')
        trigger_hold_low_right_var2 = config.get('config','trigger_hold_low_right',  fallback='')
        trigger_slow_right_var2 = config.get('config','trigger_slow_right',  fallback='')
        stick_turbo_var2 = config.get('config','stick_turbo',  fallback='')
        
        use_autocenter_stick_left_var = config.get('config','use_autocenter_stick_left',  fallback='')
        use_autocenter_stick_right_var = config.get('config','use_autocenter_stick_right',  fallback='')
        use_autocenter_trigger_left_var = config.get('config','use_autocenter_trigger_left',  fallback='')
        use_autocenter_trigger_right_var = config.get('config','use_autocenter_trigger_right',  fallback='')
        
        combo_reset_left_x_var = config.get('config','reset_left_x',  fallback='')
        combo_reset_left_y_var = config.get('config','reset_left_y',  fallback='')
        combo_reset_right_x_var = config.get('config','reset_right_x',  fallback='')
        combo_reset_right_y_var = config.get('config','reset_right_y',  fallback='')
       
        hide_window_var = config.get('config','hide_window',  fallback='')
        polling_time_var = config.get('config','polling_time',  fallback='')
        
        mousecenterposition_var = config.get('config','mousecenterposition',  fallback='')
        
        stick_alternative_limit_var = config.get('config','stick_alternative_limit',  fallback='')
        stick_limit_response_type_var = config.get('config','stick_limit_response_type',  fallback='')
        stick_alternative_speed_var = config.get('config','stick_alternative_speed',  fallback='')
        
        
       
        
        if(gamepadtype_var): combotype.set(gamepadtype_var)
        if(keymap_var): combokey.set(keymap_var)
        if(mouse_var): combo.set(mouse_var)
        if(mousewheel_var): combowheel.set(mousewheel_var)
        if(use_integer_var): use_integer.set(use_integer_var)
        if(mousefixed_var): combomousefixed.set(mousefixed_var)
        if(mouse_x_position_var2): spin_mouse_x_position_var.set(mouse_x_position_var2)
        if(mouse_y_position_var2): spin_mouse_y_position_var.set(mouse_y_position_var2)
        
        
        
        if(deadzone_scale_var2): deadzone_scale_var.set(deadzone_scale_var2)
        if(x_sens_scale_var2): x_sens_scale_var.set(x_sens_scale_var2)
        if(y_sens_scale_var2): y_sens_scale_var.set(y_sens_scale_var2)
        if(spin_inc_wheel_var2): spin_inc_wheel_var.set(spin_inc_wheel_var2)
        if(spin_dec_wheel_var2): spin_dec_wheel_var.set(spin_dec_wheel_var2)
        if(spin_inc_time_var2): spin_inc_time_var.set(spin_inc_time_var2)
        if(spin_dec_time_var2): spin_dec_time_var.set(spin_dec_time_var2)
        
       
        
        
        if(spin_inc_key_var2_left): spin_inc_key_var_left.set(spin_inc_key_var2_left)
        if(spin_inc_key_var2_right): spin_inc_key_var_right.set(spin_inc_key_var2_right)
        if(spin_dec_key_var2_left): spin_dec_key_var_left.set(spin_dec_key_var2_left)
        if(spin_dec_key_var2_right): spin_dec_key_var_right.set(spin_dec_key_var2_right)
        if(spin_center_percent_var2): spin_center_percent_var.set(spin_center_percent_var2)
        if(spin_center_value_var2): spin_center_value_var.set(spin_center_value_var2)
        #if(combo_center_type_var2): combo_center_type.set(combo_center_type_var2)
        
        
        if(limitmouse_var2): combomouselimit.set(limitmouse_var2)
        if(limit_mouse_x_position_var2): spin_limit_mouse_x_position_var.set(limit_mouse_x_position_var2)
        if(limit_mouse_y_position_var2): spin_limit_mouse_y_position_var.set(limit_mouse_y_position_var2)
     
        #NEW 06-05
        if(mouseleft_var2): combomouseleft.set(mouseleft_var2)
        if(mousemiddle_var2): combomousemiddle.set(mousemiddle_var2)
        if(mouseright_var2): combomouseright.set(mouseright_var2)
        if(trigger_hold_high_left_var2): spin_trigger_hold_high_left_var.set(trigger_hold_high_left_var2)
        if(trigger_hold_low_left_var2): spin_trigger_hold_low_left_var.set(trigger_hold_low_left_var2)
        if(trigger_slow_left_var2): spin_trigger_slow_left_var.set(trigger_slow_left_var2)
        if(trigger_hold_high_right_var2): spin_trigger_hold_high_right_var.set(trigger_hold_high_right_var2)
        if(trigger_hold_low_right_var2): spin_trigger_hold_low_right_var.set(trigger_hold_low_right_var2)
        if(trigger_slow_right_var2): spin_trigger_slow_right_var.set(trigger_slow_right_var2)
        if(stick_turbo_var2): spin_stick_turbo_var.set(stick_turbo_var2)
        
        
        if(use_autocenter_stick_left_var): use_autocenter_stick_left.set(use_autocenter_stick_left_var)
        if(use_autocenter_stick_right_var): use_autocenter_stick_right.set(use_autocenter_stick_right_var)
        if(use_autocenter_trigger_left_var): use_autocenter_trigger_left.set(use_autocenter_trigger_left_var)
        if(use_autocenter_trigger_right_var): use_autocenter_trigger_right.set(use_autocenter_trigger_right_var)
        

        if(combo_reset_left_x_var): combo_reset_left_x.set(combo_reset_left_x_var)
        if(combo_reset_left_y_var): combo_reset_left_y.set(combo_reset_left_y_var)
        if(combo_reset_right_x_var): combo_reset_right_x.set(combo_reset_right_x_var)
        if(combo_reset_right_y_var): combo_reset_right_y.set(combo_reset_right_y_var)
       
        if(hide_window_var): hide_window.set(hide_window_var)
        if(polling_time_var): spin_polling_time_var.set(polling_time_var)
        
        if(mousecenterposition_var): combomousecenterposition.set(mousecenterposition_var)
        
        if(stick_alternative_limit_var): spin_stick_alternative_limit_var.set(stick_alternative_limit_var)
        if(stick_limit_response_type_var): combo_stick_limit_response_type.set(stick_limit_response_type_var)
        if(stick_alternative_speed_var): spin_stick_alternative_speed_var.set(stick_alternative_speed_var)

        
        if (not os.path.exists(f'keymap/{keymap_var}.ini')):
            messagebox.showwarning("Error", f"Keymap File {keymap_var}.ini do not exist. The default file will be used.")
            combokey.set('default')
        
        messagebox.showinfo("OK", "Profile loaded")
    #print(deadzone)
    #print(x_sensitivity)
    
    
def save_profile():
    profile_name = profilecombo.get()
    
    if (profile_name == ''):
        messagebox.showwarning("Error", "Profile name cannot be empty")
    else:
        config['config'] = {}
        config['config']['gamepadtype'] = combotype.get()
        config['config']['keymap'] = combokey.get()
        config['config']['mouse'] = combo.get()
        config['config']['mousewheel'] = combowheel.get()
        config['config']['use_integer'] = str(use_integer.get())
        config['config']['mousefixed'] = combomousefixed.get()
        config['config']['mouse_x_position'] = str(spin_mouse_x_position_var.get())
        config['config']['mouse_y_position'] = str(spin_mouse_y_position_var.get())

        config['config']['deadzone_scale'] = str(deadzone_scale.get())
        config['config']['x_sens_scale'] = str(x_sens_scale.get())
        config['config']['y_sens_scale'] = str(y_sens_scale.get())
        config['config']['spin_inc_wheel'] = str(spin_inc_wheel.get())
        config['config']['spin_dec_wheel'] = str(spin_dec_wheel.get())
        config['config']['spin_inc_time'] = str(spin_inc_time.get())
        config['config']['spin_dec_time'] = str(spin_dec_time.get())
        
        
        
        config['config']['spin_inc_key_left'] = str(spin_inc_key_left.get())
        config['config']['spin_inc_key_right'] = str(spin_inc_key_right.get())
        config['config']['spin_dec_key_left'] = str(spin_dec_key_left.get())
        config['config']['spin_dec_key_right'] = str(spin_dec_key_right.get())
        config['config']['spin_center_percent'] = str(spin_center_percent.get())
        config['config']['spin_center_value'] = str(spin_center_value.get())
        #config['config']['combo_center_type'] = str(combo_center_type.get())
        
        
        config['config']['limitmouse'] = combomouselimit.get()
        config['config']['limit_mouse_x_position'] = str(spin_limit_mouse_x_position.get())
        config['config']['limit_mouse_y_position'] = str(spin_limit_mouse_y_position.get())
        
        
        #NEW 06-05
        #MOUSE BUTTONS
        config['config']['mouseleft'] = combomouseleft.get()
        config['config']['mousemiddle'] = combomousemiddle.get()
        config['config']['mouseright'] = combomouseright.get()
        
        config['config']['trigger_hold_high_left'] = str(spin_trigger_hold_high_left.get())
        config['config']['trigger_hold_low_left'] = str(spin_trigger_hold_low_left.get())
        config['config']['trigger_slow_left'] = str(spin_trigger_slow_left.get())
        
        config['config']['trigger_hold_high_right'] = str(spin_trigger_hold_high_right.get())
        config['config']['trigger_hold_low_right'] = str(spin_trigger_hold_low_right.get())
        config['config']['trigger_slow_right'] = str(spin_trigger_slow_right.get())
        
        
        config['config']['stick_turbo'] = str(spin_stick_turbo.get())
        
        
        config['config']['use_autocenter_stick_left'] = str(use_autocenter_stick_left.get())
        config['config']['use_autocenter_stick_right'] = str(use_autocenter_stick_right.get())
        config['config']['use_autocenter_trigger_left'] = str(use_autocenter_trigger_left.get())
        config['config']['use_autocenter_trigger_right'] = str(use_autocenter_trigger_right.get())
                
        
        config['config']['reset_left_x'] = str(combo_reset_left_x.get())
        config['config']['reset_left_y'] = str(combo_reset_left_y.get())
        config['config']['reset_right_x'] = str(combo_reset_right_x.get())
        config['config']['reset_right_y'] = str(combo_reset_right_y.get())
        
        config['config']['hide_window'] = str(hide_window.get())
        
        config['config']['polling_time'] = str(spin_polling_time.get())
        config['config']['mousecenterposition'] = str(combomousecenterposition.get())
        
        config['config']['stick_alternative_limit'] = str(spin_stick_alternative_limit_var.get())
        config['config']['stick_limit_response_type'] = str(combo_stick_limit_response_type.get())
        config['config']['stick_alternative_speed'] = str(spin_stick_alternative_speed_var.get())
        
        
        
        # Save the configuration to a file
        with open('profile/'+profile_name+'.ini', 'w') as configfile:
            config.write(configfile)
            
        messagebox.showinfo("OK", "Profile Saved")

def mouse_to_joystick(x, y):
    x_sensitivity = float(x_sens_scale.get()) / 100
    y_sensitivity = float(y_sens_scale.get()) / 100
    deadzone = float(deadzone_scale.get()) / 100
    
    x_offset = (x - center_x) * x_sensitivity
    y_offset = (y - center_y) * y_sensitivity  
 
    # Deadzone 
    if abs(x_offset) < deadzone * width / 10:
        x_offset = 0.0 
    if abs(y_offset) < deadzone * height / 10:
        y_offset = 0.0
 
    x_value = x_offset / (width / 10)
    y_value = y_offset / (height / 10)
 
    return max(-1, min(1, x_value)), max(-1, min(1, y_value))
 
# GUI Functions
def update_deadzone(value):
    global deadzone
    deadzone = float(value) / 100
 
def update_sensitivity_x(value):
    global x_sensitivity, y_sensitivity
    x_sensitivity = float(value) / 100
    
def update_sensitivity_y(value):
    global x_sensitivity, y_sensitivity
    y_sensitivity = float(value) / 100

def setcombo(event):
    value = event.widget.get()
    mousewheel = combowheel.get()
    if (value == 'Left Trigger-Y' or  value == 'Right Trigger-Y' or  value == 'Left Trigger-X' or  value == 'Right Trigger-X'):
        if mousewheel != 'Center Mouse':
            combowheel.current(0)
     
    mouseleft = combomouseleft.get() 
    if(((value == 'Left Trigger-Y' or value == 'Left Trigger-X') and mouseleft == 'Left Trigger') or
        ((value == 'Right Trigger-Y' or value == 'Right Trigger-X')  and mouseleft == 'Right Trigger')):
        combomouseleft.current(0)
        
    mousemiddle = combomousemiddle.get() 
    if(((value == 'Left Trigger-Y' or value == 'Left Trigger-X') and mousemiddle == 'Left Trigger') or
        ((value == 'Right Trigger-Y' or value == 'Right Trigger-X')  and mousemiddle == 'Right Trigger')):
        combomousemiddle.current(0)
        
    mouseright = combomouseright.get() 
    if(((value == 'Left Trigger-Y' or value == 'Left Trigger-X') and mouseright == 'Left Trigger') or
        ((value == 'Right Trigger-Y' or value == 'Right Trigger-X')  and mouseright == 'Right Trigger')):
        combomouseright.current(0)
    
def setwheel(event):
    value = event.widget.get()
    
    mouseas = combo.get()
    
    if ((value == 'Left Trigger' and  (mouseas == 'Left Trigger-Y' or mouseas == 'Left Trigger-X')) or
        (value == 'Right Trigger' and  (mouseas == 'Right Trigger-Y' or mouseas == 'Right Trigger-X'))):
        combo.current(0)
    mouseleft = combomouseleft.get() 
    if((value == 'Left Trigger' and mouseleft == 'Left Trigger') or
        (value == 'Right Trigger' and mouseleft == 'Right Trigger')):
        combomouseleft.current(0)
        
    mousemiddle = combomousemiddle.get() 
    if((value == 'Left Trigger' and mousemiddle == 'Left Trigger') or
        (value == 'Right Trigger' and mousemiddle == 'Right Trigger')):
        combomousemiddle.current(0)
        
    mouseright = combomouseright.get() 
    if((value == 'Left Trigger' and mouseright == 'Left Trigger') or
        (value == 'Right Trigger' and mouseright == 'Right Trigger')):
        combomouseright.current(0)

def setbuttons_left(event):
    value = event.widget.get()
   
    mouseas = combo.get()
    mousewheel = combowheel.get()
        
    if ((value == 'Left Trigger' and  (mouseas == 'Left Trigger-Y' or mouseas == 'Left Trigger-X')) or
        (value == 'Right Trigger' and  (mouseas == 'Right Trigger-Y' or mouseas == 'Right Trigger-X'))):
        combo.current(0)
        
    if ((value == 'Left Trigger' and  mousewheel == 'Left Trigger') or
        (value == 'Right Trigger' and  mousewheel == 'Right Trigger')):
        combowheel.current(0)
    
    mousemiddle = combomousemiddle.get() 
    if((value == 'Left Trigger' and mousemiddle == 'Left Trigger') or
        (value == 'Right Trigger' and mousemiddle == 'Right Trigger')):
        combomousemiddle.current(0)
        
    mouseright = combomouseright.get() 
    if((value == 'Left Trigger' and mouseright == 'Left Trigger') or
        (value == 'Right Trigger' and mouseright == 'Right Trigger')):
        combomouseright.current(0)
    

def setbuttons_middle(event):
    value = event.widget.get()
   
    mouseas = combo.get()
    mousewheel = combowheel.get()
    
    if ((value == 'Left Trigger' and  (mouseas == 'Left Trigger-Y' or mouseas == 'Left Trigger-X')) or
        (value == 'Right Trigger' and  (mouseas == 'Right Trigger-Y' or mouseas == 'Right Trigger-X'))):
        combo.current(0)
        
    if ((value == 'Left Trigger' and  mousewheel == 'Left Trigger') or
        (value == 'Right Trigger' and  mousewheel == 'Right Trigger')):
        combowheel.current(0)
        
    mouseleft = combomouseleft.get() 
    if((value == 'Left Trigger' and mouseleft == 'Left Trigger') or
        (value == 'Right Trigger' and mouseleft == 'Right Trigger')):
        combomouseleft.current(0)
        
    mouseright = combomouseright.get() 
    if((value == 'Left Trigger' and mouseright == 'Left Trigger') or
        (value == 'Right Trigger' and mouseright == 'Right Trigger')):
        combomouseright.current(0)
    
  

    
def setbuttons_right(event):
    value = event.widget.get()
   
    mouseas = combo.get()
    mousewheel = combowheel.get()
    
    if ((value == 'Left Trigger' and  (mouseas == 'Left Trigger-Y' or mouseas == 'Left Trigger-X')) or
        (value == 'Right Trigger' and  (mouseas == 'Right Trigger-Y' or mouseas == 'Right Trigger-X'))):
        combo.current(0)
        
    if ((value == 'Left Trigger' and  mousewheel == 'Left Trigger') or
        (value == 'Right Trigger' and  mousewheel == 'Right Trigger')):
        combowheel.current(0)
        
    mouseleft = combomouseleft.get() 
    if((value == 'Left Trigger' and mouseleft == 'Left Trigger') or
        (value == 'Right Trigger' and mouseleft == 'Right Trigger')):
        combomouseleft.current(0)
        
    mousemiddle = combomousemiddle.get() 
    if((value == 'Left Trigger' and mousemiddle == 'Left Trigger') or
        (value == 'Right Trigger' and mousemiddle == 'Right Trigger')):
        combomousemiddle.current(0)

        
    
 
def toggle_emulation():
    global is_running
    global monitor_process
    global root
    global gamepad
    is_running = not is_running
    if is_running:
        #if (hide_window.get() == 1):
        #    messagebox.showwarning("Caution", f"The window will be hidden.\nTo restore and stop the Gamepad, use the F12 key.")
        
        #start_button.config(text="Stop")
        #root.destroy()
        #main_loop()
        update_keys()
        #blockkeyboard()
        thread1 = threading.Thread(target=main_loop, daemon=True)
        thread1.start()
        start_button.config(text="Stop Gamepad (F12)")
        calibrate_button.config(state="disabled")
        monitor_button.config(state="normal")
        combo.config(state="disabled")
        combokey.config(state="disabled")
        combotype.config(state="disabled")
        combowheel.config(state="disabled")
        combomousecenterposition.config(state="disabled")
        combomousefixed.config(state="disabled")
        combomouseleft.config(state="disabled")
        combomousemiddle.config(state="disabled")
        combomouseright.config(state="disabled")
        combomouselimit.config(state="disabled")
        check_hide_window.config(state="disabled")
        spin_polling_time.config(state="disabled")
        profilecombo.config(state="disabled")
        load_button.config(state="disabled")
        save_button.config(state="disabled")

        
        check_int.config(state="disabled")
        if (hide_window.get() == 1):
            root.withdraw()
    else:
        #unblockkeyboard()   
        #del gamepad
        #del thread1
        try:
            monitor_process.terminate()
        except:
            print("Not possible to close JOY subprocess")
            
        start_button.config(text="Start Gamepad (F12)")
        calibrate_button.config(state="normal")
        monitor_button.config(state="disabled")
        combotype.config(state="readonly")
        combo.config(state="readonly")
        combokey.config(state="readonly")
        combowheel.config(state="readonly")
        combomouseleft.config(state="readonly")
        combomousemiddle.config(state="readonly")
        combomouseright.config(state="readonly")
        combomousecenterposition.config(state="readonly")
        combomousefixed.config(state="readonly")
        combomouselimit.config(state="readonly")
        check_int.config(state="normal")
        check_hide_window.config(state="normal")
        spin_polling_time.config(state="normal")
        profilecombo.config(state="normal")
        load_button.config(state="normal")
        save_button.config(state="normal")
        if (hide_window.get() == 1):
            root.deiconify()
            root.update()

def monitor_emulation():
    global monitor_process
    #os.startfile("pygame-joystick-test.py")
    #p1 = subprocess.call('python pygame-joystick-test.py')
    executable_path = sys.executable
    #print(executable_path)
    monitor_process = subprocess.Popen(executable_path+" pygame-joystick-test.py")
    #os.system("pygame-joystick-test.py")
    monitor_button.config(state="disabled")
    '''
    while monitor_process.poll() is None:
        print("Process is still running...")
        time.sleep(0.5)
    '''
        
        

def swtiches(lbl,lblvar,txt):
    if (txt == 'ON'):
        lbl.config(bg="green") 
        lbl.config(fg="yellow") 
        lblvar.set(txt)
    else:
        lbl.config(bg="red") 
        lbl.config(fg="white") 
        lblvar.set(txt)
   
def calibrate_emulation():
    global is_running
    is_running = not is_running
    if is_running:
        #swtiches(lbl1_swtich,lbl1_var,'ON')
        #start_button.config(text="Stop")
        #root.destroy()
        #calibrate_loop()
        thread1 = threading.Thread(target=calibrate_loop,daemon=True)
        thread1.start()
        calibrate_button.config(text="Stop Calibration")
        start_button.config(state="disabled")
        combo.config(state="disabled")
        combokey.config(state="disabled")
        combomousefixed.config(state="disabled")
        combotype.config(state="disabled")
        combowheel.config(state="disabled")
        check_int.config(state="disabled")
        combomouseleft.config(state="disabled")
        combomousemiddle.config(state="disabled")
        combomouseright.config(state="disabled")
        combomouselimit.config(state="disabled")
    else:
        #swtiches(lbl1_swtich,lbl1_var,'OFF')
        calibrate_button.config(text="Start Calibration")
        start_button.config(state="normal")
        combo.config(state="readonly")
        combokey.config(state="readonly")
        combomousefixed.config(state="readonly")
        combotype.config(state="readonly")
        combowheel.config(state="readonly")
        check_int.config(state="normal")
        combomouseleft.config(state="readonly")
        combomousemiddle.config(state="readonly")
        combomouseright.config(state="readonly")
        combomousefixed.config(state="readonly")
        combomouselimit.config(state="readonly")


start_f12 = 0

def on_f12(event):
    global start_f12
    #print(f"Key released: {event.keysym}")
    #if (event.keysym =='F12' and start_f12 ==0):
    if (start_f12 ==0):
        start_f12 = 1
        toggle_emulation()
    else:
        start_f12 = 0

def start_gui():
    global start_button
    global calibrate_button
    global tabControl
    global combo
    global combowheel
    global combokey
    global combotype
    global profilecombo
    global combomousefixed
    global use_integer
    global check_int
    global spin_mouse_x_position_var
    global spin_mouse_y_position_var
    global deadzone_scale
    global deadzone_scale_var
    global x_sens_scale
    global x_sens_scale_var
    global y_sens_scale
    global y_sens_scale_var
    global spin_inc_wheel
    global spin_inc_wheel_var
    global spin_dec_wheel
    global spin_dec_wheel_var
    global spin_inc_time
    global spin_inc_time_var
    global spin_dec_time
    global spin_dec_time_var
    global spin_dec_time_var
    
    global spin_inc_key_left
    global spin_inc_key_right
    global spin_inc_key_var_left
    global spin_inc_key_var_right
    global spin_dec_key_left
    global spin_dec_key_right
    global spin_dec_key_var_left
    global spin_dec_key_var_right
    global spin_center_percent
    global spin_center_percent_var
    global spin_center_value
    global spin_center_value_var
    global combo_center_type
    global combomouselimit
    global spin_limit_mouse_x_position
    global spin_limit_mouse_y_position
    global spin_limit_mouse_x_position_var
    global spin_limit_mouse_y_position_var
    
    global combomouseleft
    global combomousemiddle
    global combomouseright
    
    global spin_trigger_hold_high_left
    global spin_trigger_hold_low_left
    global spin_trigger_slow_left
    
    global spin_trigger_hold_high_left_var
    global spin_trigger_hold_low_left_var
    global spin_trigger_slow_left_var
    
    global spin_trigger_hold_high_right
    global spin_trigger_hold_low_right
    global spin_trigger_slow_right
    
    global spin_trigger_hold_high_right_var
    global spin_trigger_hold_low_right_var
    global spin_trigger_slow_right_var

    global spin_stick_turbo
    global spin_stick_turbo_var
    
    global use_autocenter_stick_left
    global use_autocenter_stick_right
    global use_autocenter_trigger_left
    global use_autocenter_trigger_right
    
    global combo_reset_left_x
    global combo_reset_left_y
    global combo_reset_right_x
    global combo_reset_right_y
    
    global hide_window
    global check_hide_window
    global spin_polling_time_var
    global spin_polling_time
    
    global combomousecenterposition
    global monitor_button
    
    global spin_stick_alternative_limit_var
    global combo_stick_limit_response_type
    global spin_stick_alternative_speed_var
    
    global lbl0_var, lbl0_swtich
    global lbl01_var, lbl01_swtich
    global lbl1_var, lbl1_swtich
    global lbl2_var, lbl2_swtich
    global lbl3_var, lbl3_swtich
    global lbl4_var, lbl4_swtich
    global lbl5_var, lbl5_swtich
    global lbl6_var, lbl6_swtich
    global lbl7_var, lbl7_swtich
    global lbl8_var, lbl8_swtich
    
    global load_button, save_button

    
    
    filelista_profile = []
    for file in os.scandir('profile/'):
        if(file.is_file()):
            file_name, file_extension = os.path.splitext(file.name)
            if (file_extension == '.ini'):
                filelista_profile.append(file_name)
    #print(filelista_profile)


    filelista_keys = []
    for file in os.scandir('keymap/'):
        if(file.is_file()):
            file_name, file_extension = os.path.splitext(file.name)
            if (file_extension == '.ini'):
                filelista_keys.append(file_name)
    #print(filelista_keys)

    if (not os.path.exists(f'keymap/default.ini')):
        messagebox.showwarning("Error", f"Default keymap file [default.ini] do not exist in keymap folder")
        sys.exit()

    
    root = tk.Tk()
    root.title("KBM2Gamepad Emulator")
    root.geometry("800x600")
    root.resizable(False, False)
    
    root.bind('<F12>', on_f12)
    #root.bind("<KeyRelease>", on_f12)
    
    tabControl = ttk.Notebook(root)
    tab1 = ttk.Frame(tabControl)
    tab2 = ttk.Frame(tabControl)
    tab3 = ttk.Frame(tabControl)
    tab4 = ttk.Frame(tabControl)
    tab5 = ttk.Frame(tabControl)

    tabControl.add(tab1, text ='General')
    tabControl.add(tab2, text ='Mouse Config')
    tabControl.add(tab3, text ='Analog Sticks')
    tabControl.add(tab4, text ='Triggers')
    tabControl.add(tab5, text ='Keymap')
    tabControl.pack(expand = 1, fill ="both")
    
    
    ##########################################
    # CONTENT FOR TAB ONE
    ##########################################
    tkrow =0
    top_frame = tk.LabelFrame(tab1, text="General Config:")
    top_frame.pack(side="top", pady='10')
    
    tkrow= tkrow + 1
    tk.Label(top_frame, text="Gamepad Type:").grid(row=tkrow, column=0,sticky="w",padx=20)
    options = ["Xbox 360",\
    #"DS4 (PS4)",\
    #"Virtual Joystick (Vjoy)"
    ]
    combotype = ttk.Combobox(top_frame, values=options, state="readonly")
    combotype.current(0)
    combotype.grid(row=tkrow, column=1,  padx=3, pady=3, sticky="w")

    tkrow= tkrow + 1
    tk.Label(top_frame, text="Keymap file:").grid(row=tkrow, column=0,sticky="w",padx=20)
    combokey = ttk.Combobox(top_frame, values=filelista_keys, width=30, state="readonly")
    #combokey.current(0)
    combokey.set('default')
    combokey.grid(row=tkrow, column=1,  padx=3, pady=3, sticky="w")

    tkrow= tkrow + 1
    tk.Label(top_frame, text="Mouse as:").grid(row=tkrow, column=0,sticky="w",padx=20)
    # MOVE MOUSE POSIÇÂO: ctypes.windll.user32.SetCursorPos(0, 0)
    options = ["None",\
        "Left Stick","Left Stick-X","Left Stick-Y",\
        "Right Stick","Right Stick-X","Right Stick-Y",\
        "----------",\
        "Left Trigger-Y", "Right Trigger-Y","Left Trigger-X", "Right Trigger-X",\
        "----------",\
        "Left Stick-X + Left Trigger-Y",\
        "Left Stick-X + Left Trigger-Y-Full",\
        "Left Stick-X + Right Trigger-Y",\
        "Left Stick-X + Right Trigger-Y-Full",\
        ]
    combo = ttk.Combobox(top_frame, values=options, width=30, state="readonly")
    combo.bind('<<ComboboxSelected>>', setcombo)
    combo.current(0)
    combo.grid(row=tkrow, column=1,  padx=3, pady=3, sticky="w")

    tkrow= tkrow + 1
    tk.Label(top_frame, text="Mouse Wheel as:").grid(row=tkrow, column=0,sticky="w",padx=20)
    options = ["None", "Center Mouse","Left Trigger", "Right Trigger"]
    combowheel = ttk.Combobox(top_frame, values=options, state="readonly")
    combowheel.current(1)
    combowheel.grid(row=tkrow, column=1,  padx=3, pady=3, sticky="w")
    combowheel.bind('<<ComboboxSelected>>', setwheel)
    
    tkrow= tkrow + 1
    canvas = Canvas(top_frame, width=500, height=5)
    canvas.grid(row=tkrow, column=0,columnspan=3)
    y = 3
    canvas.create_line(0, y, 500, y)
    
    tkrow= tkrow + 1
    tk.Label(top_frame, text="Mouse Buttons:").grid(row=tkrow, column=0, sticky="w",padx=20)
    options = ["None", \
        "Left Trigger", "Right Trigger",\
        "----------",\
        "Center Mouse",
        "----------",\
        #"Left Stick","Left Stick-X","Left Stick-Y", \
        #"Right Stick","Right Stick-X","Right Stick-Y", \
        "A","B","X","Y","LB","RB","L3","R3","Start","Back","Guide"
    ]
    #LEFT
    tk.Label(top_frame, text="Left:").grid(row=tkrow, column=1,sticky="w")
    combomouseleft = ttk.Combobox(top_frame, values=options, state="readonly")
    combomouseleft.current(0)
    combomouseleft.grid(row=tkrow, column=1,  padx=50, pady=3, sticky="w")
    combomouseleft.bind('<<ComboboxSelected>>', setbuttons_left)
    
    #MIDDLE
    tkrow= tkrow + 1
    tk.Label(top_frame, text="Middle:").grid(row=tkrow, column=1,sticky="w")
    combomousemiddle = ttk.Combobox(top_frame, values=options, state="readonly")
    combomousemiddle.current(0)
    combomousemiddle.grid(row=tkrow, column=1,  padx=50, pady=3, sticky="w")
    combomousemiddle.bind('<<ComboboxSelected>>', setbuttons_middle)
    
    #RIGHT
    tkrow= tkrow + 1
    tk.Label(top_frame, text="Right:").grid(row=tkrow, column=1,sticky="w")
    combomouseright = ttk.Combobox(top_frame, values=options, state="readonly")
    combomouseright.current(0)
    combomouseright.grid(row=tkrow, column=1,  padx=50, pady=3, sticky="w")
    combomouseright.bind('<<ComboboxSelected>>', setbuttons_right)
    
    
    tkrow= tkrow + 1
    canvas = Canvas(top_frame, width=500, height=5)
    canvas.grid(row=tkrow, column=0,columnspan=3)
    y = 3
    canvas.create_line(0, y, 500, y)
    
    tkrow= tkrow + 1
    hide_window = tk.IntVar()
    tk.Label(top_frame, text="Auto Hide GUI:").grid(row=tkrow, column=0, sticky="w",padx=20)
    check_hide_window = tk.Checkbutton(top_frame, text="Yes - To restore the window use F12 key", variable=hide_window, onvalue=1, offvalue=0)
    check_hide_window.grid(row=tkrow, column=1,sticky="w")
    hide_window.set(0)
    
    
    spin_polling_time_var = tk.DoubleVar(value=0.01)
    tkrow= tkrow + 1
    tk.Label(top_frame, text="Process Polling time:").grid(row=tkrow, column=0,sticky="w",padx=20)
    spin_polling_time = tk.Spinbox(top_frame, from_=0.00, to=10, increment=0.01, format="%.2f", width=12, wrap=True,state="readonly",textvariable=spin_polling_time_var)
    spin_polling_time.grid(row=tkrow, column=1, padx=3, sticky="w")
    
    
    
    
    
    tkrow= 0  
    #bottom_frame = tk.LabelFrame(tab1, text="Actions:",width=500,height=65)
    #bottom_frame.pack(side="top", pady='10')
    bottom_frame = tk.LabelFrame(root, text="Actions:",width=500,height=65,bg="lightgrey")
    bottom_frame.place(x=150, y=390)
    
    bottom_frame.pack_propagate(False)
    
    tkrow= tkrow + 1
    start_button = tk.Button(bottom_frame, text="Start Gamepad (F12)", command=toggle_emulation)
    start_button.pack(side='left',padx=10, pady=10)
    
    monitor_button = tk.Button(bottom_frame, text="Start Monitoring", command=monitor_emulation)
    monitor_button.pack(side='left',padx=10, pady=10)
    monitor_button.config(state="disabled")

    calibrate_button = tk.Button(bottom_frame, text="Start Calibration", command=calibrate_emulation)
    calibrate_button.pack(side='left',padx=10, pady=10)
    tk.Label(bottom_frame, text="*Console output").pack(side='left',padx=10, pady=10)

    tkrow= 0
    bottom_frame2 = tk.LabelFrame(tab1, text="Save / Load:",width=500,height=65)
    bottom_frame2.pack(side="top")
    
    bottom_frame2.pack_propagate(False)

    tkrow= tkrow + 1
    tk.Label(bottom_frame2, text="Profile:").pack(side="left", padx=5, pady='10')
    profilecombo = ttk.Combobox(bottom_frame2, values=filelista_profile,width=30)
    #combo.bind('<<ComboboxSelected>>', setcombo)
    profilecombo.current(0)
    #profilecombo.grid(row=tkrow, column=1,  padx=3, pady=3, sticky="w")
    profilecombo.pack(side="left", padx=5, pady='3')

    load_button = tk.Button(bottom_frame2, text="Load", command=load_profile)
    load_button.pack(side="left", padx=5, pady='10')

    save_button = tk.Button(bottom_frame2, text="Save", command=save_profile)
    save_button.pack(side="left", padx=5, pady='10')
    
    bottom_frame2 = tk.LabelFrame(root, text="Switches button monitoring:",width=500,height=75)
    bottom_frame2.place(x=15, y=460)
    
   
    
    tkrow= 0
    tk.Label(bottom_frame2, text="Keyboard\nSuppress").grid(row=tkrow, column=0, sticky="w",)
    tk.Label(bottom_frame2, text="Key-TO-Joy\nMuted").grid(row=tkrow, column=1, sticky="w",)
    tk.Label(bottom_frame2, text="Analog Left\nAuto center").grid(row=tkrow, column=2, sticky="w",)
    tk.Label(bottom_frame2, text="Analog Right\nAuto center").grid(row=tkrow, column=3, sticky="w")
    tk.Label(bottom_frame2, text="Trigger Left\nAuto center").grid(row=tkrow, column=4, sticky="w")
    tk.Label(bottom_frame2, text="Trigger Right\nAuto center").grid(row=tkrow, column=5, sticky="w")
    tk.Label(bottom_frame2, text="Fixed mouse\nPosition").grid(row=tkrow, column=6, sticky="w")
    tk.Label(bottom_frame2, text="Limit mouse\nMovement").grid(row=tkrow, column=7, sticky="w")
    tk.Label(bottom_frame2, text="Analog Alternative\nSpeed - Switch").grid(row=tkrow, column=8, sticky="w")
    tk.Label(bottom_frame2, text="Trigger Alternative\nSpeed - Switch").grid(row=tkrow, column=9, sticky="w")
    
    tkrow= tkrow + 1
    
    # swtiches(lbl1_swtich,lbl1_var,'ON')
    
    lbl0_var = tk.StringVar(value="ON")
    lbl0_swtich = tk.Label(bottom_frame2, textvariable=lbl0_var,bg="green", fg="yellow", font=("Arial", 15))
    lbl0_swtich.grid(row=tkrow, column=0, sticky="n")
    
    lbl01_var = tk.StringVar(value="OFF")
    lbl01_swtich = tk.Label(bottom_frame2, textvariable=lbl01_var,bg="red", fg="white", font=("Arial", 15))
    lbl01_swtich.grid(row=tkrow, column=1, sticky="n")
    
    
    lbl1_var = tk.StringVar(value="ON")
    lbl1_swtich = tk.Label(bottom_frame2, textvariable=lbl1_var,bg="green", fg="yellow", font=("Arial", 15))
    lbl1_swtich.grid(row=tkrow, column=2, sticky="n")
    
    lbl2_var = tk.StringVar(value="ON")
    lbl2_swtich = tk.Label(bottom_frame2, textvariable=lbl2_var,bg="green", fg="yellow", font=("Arial", 15))
    lbl2_swtich.grid(row=tkrow, column=3, sticky="n")
    
    lbl3_var = tk.StringVar(value="ON")
    lbl3_swtich = tk.Label(bottom_frame2, textvariable=lbl3_var,bg="green", fg="yellow", font=("Arial", 15))
    lbl3_swtich.grid(row=tkrow, column=4, sticky="n")
    
    lbl4_var = tk.StringVar(value="ON")
    lbl4_swtich = tk.Label(bottom_frame2, textvariable=lbl4_var,bg="green", fg="yellow", font=("Arial", 15))
    lbl4_swtich.grid(row=tkrow, column=5, sticky="n")
    
    lbl5_var = tk.StringVar(value="OFF")
    lbl5_swtich = tk.Label(bottom_frame2, textvariable=lbl5_var,bg="red", fg="white", font=("Arial", 15))
    lbl5_swtich.grid(row=tkrow, column=6, sticky="n")
    
    lbl6_var = tk.StringVar(value="OFF")
    lbl6_swtich = tk.Label(bottom_frame2, textvariable=lbl6_var,bg="red", fg="white", font=("Arial", 15))
    lbl6_swtich.grid(row=tkrow, column=7, sticky="n")
    
    lbl7_var = tk.StringVar(value="OFF")
    lbl7_swtich = tk.Label(bottom_frame2, textvariable=lbl7_var,bg="red", fg="white", font=("Arial", 15))
    lbl7_swtich.grid(row=tkrow, column=8, sticky="n")
    
    lbl8_var = tk.StringVar(value="OFF")
    lbl8_swtich = tk.Label(bottom_frame2, textvariable=lbl8_var,bg="red", fg="white", font=("Arial", 15))
    lbl8_swtich.grid(row=tkrow, column=9, sticky="n")


    ##########################################
    # CONTENT FOR TAB TWO
    ##########################################
    tkrow= 0
    left_frame = tk.LabelFrame(tab2, text="Mouse Sensitivity:")
    left_frame.pack(side="top", pady='10')
   
  
    tkrow= tkrow + 1
    tk.Label(left_frame, text="Deadzone:").grid(row=tkrow, column=0)
    #deadzone_scale = tk.Scale(left_frame, from_=0, to=25, orient=tk.HORIZONTAL, length=500, resolution=0.01, command=update_deadzone)
    deadzone_scale_var = tk.DoubleVar(value=2.5)
    deadzone_scale = tk.Scale(left_frame, from_=0, to=25, orient=tk.HORIZONTAL, length=500, resolution=0.01,variable=deadzone_scale_var)
    #deadzone_scale.set(2.5)
    deadzone_scale.grid(row=tkrow, column=1,pady=2)

    tkrow= tkrow + 1
    tk.Label(left_frame, text="X Sensitivity").grid(row=tkrow, column=0)
    #x_sens_scale = tk.Scale(left_frame, from_=0, to=100, orient=tk.HORIZONTAL,length=500, resolution=0.01, command=update_sensitivity_x)
    x_sens_scale_var = tk.DoubleVar(value=23.5)
    x_sens_scale = tk.Scale(left_frame, from_=0, to=100, orient=tk.HORIZONTAL,length=500, resolution=0.01,variable=x_sens_scale_var)
    #x_sens_scale.set(x_sensitivity * 23.5)
    x_sens_scale.grid(row=tkrow, column=1,pady=2)

    tkrow= tkrow + 1
    tk.Label(left_frame, text="Y Sensitivity:").grid(row=tkrow, column=0)
    #y_sens_scale = tk.Scale(left_frame, from_=0, to=100, orient=tk.HORIZONTAL,length=500, resolution=0.01, command=update_sensitivity_y)
    y_sens_scale_var = tk.DoubleVar(value=23.5)
    y_sens_scale = tk.Scale(left_frame, from_=0, to=100, orient=tk.HORIZONTAL,length=500, resolution=0.01,variable=y_sens_scale_var)
    #y_sens_scale.set(y_sensitivity * 23.5)
    y_sens_scale.grid(row=tkrow, column=1,pady=2)
    
    left_frame2 = tk.LabelFrame(tab2, text="Mouse Configs:")
    left_frame2.pack(side="top", pady='10')
    
    tkrow= 0
    use_integer = tk.IntVar()
    tk.Label(left_frame2, text="Use X/Y as Integer:").grid(row=tkrow, column=0, sticky="w",padx=20)
    check_int = tk.Checkbutton(left_frame2, text="Use Integer for mouse position", variable=use_integer, onvalue=1, offvalue=0)
    check_int.grid(row=tkrow, column=1,sticky="w")
    use_integer.set(1)
    
    tkrow= tkrow + 1
    tk.Label(left_frame2, text="[BTN] Center Mouse Position:").grid(row=tkrow, column=0, sticky="w",padx=20)
    options = ["X+Y", "X", "Y"]
    combomousecenterposition = ttk.Combobox(left_frame2, values=options,width=7, state="readonly")
    combomousecenterposition.current(1)
    combomousecenterposition.grid(row=tkrow, column=1,  padx=3, pady=3, sticky="w")

    tkrow= tkrow + 1
    tk.Label(left_frame2, text="[BTN] Fixed Mouse Position:").grid(row=tkrow, column=0, sticky="w",padx=20)
    options = ["None", "X", "Y","X+Y"]
    combomousefixed = ttk.Combobox(left_frame2, values=options,width=7, state="readonly")
    combomousefixed.current(2)
    combomousefixed.grid(row=tkrow, column=1,  padx=3, pady=3, sticky="w")
    #combomousefixed.bind('<<ComboboxSelected>>', setwheel)
    
    tk.Label(left_frame2, text="X:").grid(row=tkrow, column=1, padx=70,sticky="w")
    tk.Label(left_frame2, text="Y:").grid(row=tkrow, column=1, padx=140,sticky="w")
    spin_mouse_x_position_var = tk.IntVar(value=0)
    spin_mouse_y_position_var = tk.IntVar(value=0)
    spin_mouse_x_position = tk.Spinbox(left_frame2, from_=0, to=3000, width=5, increment=10, wrap=True, state="readonly",textvariable=spin_mouse_x_position_var)
    spin_mouse_x_position.grid(row=tkrow, column=1, padx=90, pady=3, sticky="w")
    spin_mouse_y_position = tk.Spinbox(left_frame2, from_=0, to=3000,width=5, increment=10, wrap=True,state="readonly",textvariable=spin_mouse_y_position_var)
    spin_mouse_y_position.grid(row=tkrow, column=1, padx=160, pady=3, sticky="w")
    
    tkrow= tkrow + 1
    tk.Label(left_frame2, text="[BTN] Limit Mouse Movement:").grid(row=tkrow, column=0, sticky="w",padx=20)
    options = ["None", "X", "Y","X+Y"]
    combomouselimit = ttk.Combobox(left_frame2, values=options,width=7, state="readonly")
    combomouselimit.current(1)
    combomouselimit.grid(row=tkrow, column=1,  padx=3, pady=3, sticky="w")
    tk.Label(left_frame2, text="X:").grid(row=tkrow, column=1, padx=70,sticky="w")
    tk.Label(left_frame2, text="Y:").grid(row=tkrow, column=1, padx=140,sticky="w")
    spin_limit_mouse_x_position_var = tk.IntVar(value=80)
    spin_limit_mouse_y_position_var = tk.IntVar(value=0)
    spin_limit_mouse_x_position = tk.Spinbox(left_frame2, from_=0, to=3000, width=5, increment=10, wrap=True, state="readonly",textvariable=spin_limit_mouse_x_position_var)
    spin_limit_mouse_x_position.grid(row=tkrow, column=1, padx=90, pady=3, sticky="w")
    spin_limit_mouse_y_position = tk.Spinbox(left_frame2, from_=0, to=3000,width=5, increment=10, wrap=True,state="readonly",textvariable=spin_limit_mouse_y_position_var)
    spin_limit_mouse_y_position.grid(row=tkrow, column=1, padx=160, pady=3, sticky="w")


    ##########################################
    # CONTENT FOR TAB THREE
    ##########################################
    tkrow= 0
    
    
    left_frame3 = tk.LabelFrame(tab3, text="Left Stick:",width=150,height=150)
    left_frame3.place(x=100, y=10)
    
    tkrow= tkrow + 1
    use_autocenter_stick_left = tk.IntVar()
    #tk.Label(left_frame3, text="AutoCenter Analog Left:").grid(row=tkrow, column=0, sticky="w")
    #check_autocenter_stick_left = tk.Checkbutton(left_frame3, text="Yes", variable=use_autocenter_stick_left, onvalue=1, offvalue=0)
    #check_autocenter_stick_left.grid(row=tkrow, column=1,sticky="w")
    use_autocenter_stick_left.set(1)
    
    tkrow= tkrow + 1
    tk.Label(left_frame3, text="Reset X Position:").grid(row=tkrow, column=0, sticky="w")
    options = ["0", "-32768", "32767"]
    combo_reset_left_x = ttk.Combobox(left_frame3, values=options,width=7, state="readonly")
    combo_reset_left_x.current(0)
    combo_reset_left_x.grid(row=tkrow, column=1,  padx=1,pady=1, sticky="w")
    
    tkrow= tkrow + 1
    tk.Label(left_frame3, text="Reset Y Position:").grid(row=tkrow, column=0, sticky="w")
    combo_reset_left_y = ttk.Combobox(left_frame3, values=options,width=7, state="readonly")
    combo_reset_left_y.current(0)
    combo_reset_left_y.grid(row=tkrow, column=1,  padx=1, pady=1, sticky="w")
    
    

    right_frame3 = tk.LabelFrame(tab3, text="Right Stick:",width=150,height=150)
    right_frame3.place(x=540, y=10)
        
    tkrow= 0
    use_autocenter_stick_right = tk.IntVar()
    #tk.Label(right_frame3, text="AutoCenter Analog Right:").grid(row=tkrow, column=0, sticky="w")
    #check_autocenter_stick_right = tk.Checkbutton(right_frame3, text="Yes", variable=use_autocenter_stick_right, onvalue=1, offvalue=0)
    #check_autocenter_stick_right.grid(row=tkrow, column=1,sticky="w")
    use_autocenter_stick_right.set(1)
    
    tkrow= tkrow + 1
    tk.Label(right_frame3, text="Reset X Position:").grid(row=tkrow, column=0, sticky="w")
    combo_reset_right_x = ttk.Combobox(right_frame3, values=options,width=7, state="readonly")
    combo_reset_right_x.current(0)
    combo_reset_right_x.grid(row=tkrow, column=1,  padx=1,pady=1, sticky="w")
    
    tkrow= tkrow + 1
    tk.Label(right_frame3, text="Reset Y Position:").grid(row=tkrow, column=0, sticky="w")
    combo_reset_right_y = ttk.Combobox(right_frame3, values=options,width=7, state="readonly")
    combo_reset_right_y.current(0)
    combo_reset_right_y.grid(row=tkrow, column=1,  padx=1,pady=1, sticky="w")
    
    
    
    center_frame3 = tk.LabelFrame(tab3, text="Values for reset Analog buttons:",width=600,height=120)
    tkrow= 0
    center_frame3.pack(side="top", pady='10')
    #center_frame3.grid_propagate(False)
    msg1 = "[0]  - X: Center Y: Center"
    msg2 = "[-32768] - X: Left Y: Bottom"
    msg3 = "[32767]  - X: Right Y: Top"
    tkrow= tkrow + 1
    tk.Label(center_frame3, text=msg1).grid(row=tkrow, column=0,sticky="w")
    tkrow= tkrow + 1
    tk.Label(center_frame3, text=msg2).grid(row=tkrow, column=0,sticky="w")
    tkrow= tkrow + 1
    tk.Label(center_frame3, text=msg3).grid(row=tkrow, column=0,sticky="w")

    
    
    right_frame = tk.LabelFrame(tab3, text="Advanced Config:",width=600,height=200)
    right_frame.place(x=100, y=100)

 
    #center_frame.place(x=100, y=100)
    right_frame.grid_propagate(False)
    
    tkrow= 0
    spin_inc_time_var = tk.IntVar(value=160)
    tkrow= tkrow + 1
    tk.Label(right_frame, text="Increase time:").grid(row=tkrow, column=0,sticky="w")
    spin_inc_time = tk.Spinbox(right_frame, from_=0, to=1000, increment=10, width=12, wrap=True,state="readonly",textvariable=spin_inc_time_var)
    spin_inc_time.grid(row=tkrow, column=1, padx=3, sticky="w")

    spin_dec_time_var = tk.IntVar(value=80)
    tkrow= tkrow + 1
    tk.Label(right_frame, text="Decrease time:").grid(row=tkrow, column=0,sticky="w")
    spin_dec_time = tk.Spinbox(right_frame, from_=0, to=1000, increment=10, width=12, wrap=True,state="readonly",textvariable=spin_dec_time_var)
    spin_dec_time.grid(row=tkrow, column=1, padx=3, sticky="w")

    '''
    spin_inc_key_var = tk.IntVar(value=250)
    tkrow= tkrow + 1
    tk.Label(right_frame, text="[Keyboard Trigger] Increase time:").grid(row=tkrow, column=0,sticky="w")
    spin_inc_key = tk.Spinbox(right_frame, from_=0, to=1000, increment=10, width=12, wrap=True,state="readonly",textvariable=spin_inc_key_var)
    spin_inc_key.grid(row=tkrow, column=1, padx=3, sticky="w")

    spin_dec_key_var = tk.IntVar(value=160)
    tkrow= tkrow + 1
    tk.Label(right_frame, text="[Keyboard Trigger] Decrease time:").grid(row=tkrow, column=0,sticky="w")
    spin_dec_key = tk.Spinbox(right_frame, from_=0, to=1000, increment=10, width=12, wrap=True,state="readonly",textvariable=spin_dec_key_var)
    spin_dec_key.grid(row=tkrow, column=1, padx=3, sticky="w")
    '''
     
    spin_center_percent_var = tk.IntVar(value=40)
    tkrow= tkrow + 1
    tk.Label(right_frame, text="Center sensivity %:").grid(row=tkrow, column=0,sticky="w")
    spin_center_percent = tk.Spinbox(right_frame, from_=0, to=100, increment=10, width=12, wrap=True,state="readonly",textvariable=spin_center_percent_var)
    spin_center_percent.grid(row=tkrow, column=1, padx=3, sticky="w")
    
    spin_center_value_var = tk.DoubleVar(value=0.8)
    tkrow= tkrow + 1
    tk.Label(right_frame, text="Center reduction %:").grid(row=tkrow, column=0,sticky="w")
    spin_center_value = tk.Spinbox(right_frame, from_=0.0, to=1.0, increment=0.1, width=12, wrap=True,state="readonly",textvariable=spin_center_value_var)
    spin_center_value.grid(row=tkrow, column=1, padx=3, sticky="w")
    
    
    spin_stick_turbo_var = tk.DoubleVar(value=2.0)
    tkrow= tkrow + 1
    tk.Label(right_frame, text="Alternative Speed %:").grid(row=tkrow, column=0,sticky="w")
    spin_stick_turbo = tk.Spinbox(right_frame, from_=0.00, to=10.00, increment=0.5, width=12, wrap=True,state="readonly",textvariable=spin_stick_turbo_var)
    spin_stick_turbo.grid(row=tkrow, column=1, padx=3, sticky="w")
    
    
    spin_stick_alternative_limit_var = tk.DoubleVar(value=0.60)
    tkrow= tkrow + 1
    tk.Label(right_frame, text="Alternative Limit Buttons %:").grid(row=tkrow, column=0,sticky="w")
    spin_stick_alternative_limit = tk.Spinbox(right_frame, from_=0.02, to=0.98, increment=0.01, width=12, wrap=True,state="readonly",textvariable=spin_stick_alternative_limit_var)
    spin_stick_alternative_limit.grid(row=tkrow, column=1, padx=3, sticky="w")
    
    tkrow= tkrow + 1
    tk.Label(right_frame, text="Alternative reponse limit type:").grid(row=tkrow, column=0, sticky="w")
    options = ["Default", "Direct"]
    combo_stick_limit_response_type = ttk.Combobox(right_frame, values=options,width=11, state="readonly")
    combo_stick_limit_response_type.current(0)
    combo_stick_limit_response_type.grid(row=tkrow, column=1,  padx=3, pady=3, sticky="w")
    
    spin_stick_alternative_speed_var = tk.DoubleVar(value=1.00)
    tkrow= tkrow + 1
    tk.Label(right_frame, text="Alternative Limit Speed %:").grid(row=tkrow, column=0,sticky="w")
    spin_stick_alternative_speed = tk.Spinbox(right_frame, from_=0.02, to=10.0, increment=0.01, width=12, wrap=True,state="readonly",textvariable=spin_stick_alternative_speed_var)
    spin_stick_alternative_speed.grid(row=tkrow, column=1, padx=3, sticky="w")
  
    
    ##########################################
    # CONTENT FOR TAB FOUR
    ##########################################
    
    left_frame4 = tk.LabelFrame(tab4, text="Left Trigger:",width=150,height=210)
    left_frame4.place(x=100, y=10)
    
    spin_inc_key_var_left = tk.IntVar(value=160)
    tkrow= tkrow + 1
    tk.Label(left_frame4, text="Increase time:").grid(row=tkrow, column=0,sticky="w")
    spin_inc_key_left = tk.Spinbox(left_frame4, from_=0, to=1000, increment=10, width=12, wrap=True,state="readonly",textvariable=spin_inc_key_var_left)
    spin_inc_key_left.grid(row=tkrow, column=1, padx=3, sticky="w")

    spin_dec_key_var_left = tk.IntVar(value=80)
    tkrow= tkrow + 1
    tk.Label(left_frame4, text="Decrease time:").grid(row=tkrow, column=0,sticky="w")
    spin_dec_key_left = tk.Spinbox(left_frame4, from_=0, to=1000, increment=10, width=12, wrap=True,state="readonly",textvariable=spin_dec_key_var_left)
    spin_dec_key_left.grid(row=tkrow, column=1, padx=3, sticky="w")
    
    spin_trigger_hold_high_left_var = tk.IntVar(value=0.7)
    tkrow= tkrow + 1
    tk.Label(left_frame4, text="[Trigger] Hold High %:").grid(row=tkrow, column=0,sticky="w")
    spin_trigger_hold_high_left = tk.Spinbox(left_frame4, from_=0.00, to=1.00, increment=0.05, width=12, wrap=True,state="readonly",textvariable=spin_trigger_hold_high_left_var)
    spin_trigger_hold_high_left.grid(row=tkrow, column=1, padx=3, sticky="w")
    
    spin_trigger_hold_low_left_var = tk.IntVar(value=0.35)
    tkrow= tkrow + 1
    tk.Label(left_frame4, text="[Trigger] Hold Low %:").grid(row=tkrow, column=0,sticky="w")
    spin_trigger_hold_low_left = tk.Spinbox(left_frame4, from_=0.00, to=1.00, increment=0.05, width=12, wrap=True,state="readonly",textvariable=spin_trigger_hold_low_left_var)
    spin_trigger_hold_low_left.grid(row=tkrow, column=1, padx=3, sticky="w")
    
    spin_trigger_slow_left_var = tk.IntVar(value=3.0)
    tkrow= tkrow + 1
    tk.Label(left_frame4, text="[Trigger] Alternative Speed %:").grid(row=tkrow, column=0,sticky="w")
    spin_trigger_slow_left = tk.Spinbox(left_frame4, from_=0.00, to=10.0, increment=0.1, width=12, wrap=True,state="readonly",textvariable=spin_trigger_slow_left_var)
    spin_trigger_slow_left.grid(row=tkrow, column=1, padx=3, sticky="w")
    
    tkrow= tkrow + 1
    use_autocenter_trigger_left = tk.IntVar()
    #tk.Label(left_frame4, text="[Trigger] AutoCenter/Reset Trigger:").grid(row=tkrow, column=0, sticky="w")
    #check_autocenter_trigger_left = tk.Checkbutton(left_frame4, text="Yes", variable=use_autocenter_trigger_left, onvalue=1, offvalue=0)
    #check_autocenter_trigger_left.grid(row=tkrow, column=1,sticky="w")
    use_autocenter_trigger_left.set(1)
    
    
    # RIGHT TRIGGER
    right_frame4 = tk.LabelFrame(tab4, text="Right Trigger:",width=150,height=210)
    right_frame4.place(x=438, y=10)
    
    spin_inc_key_var_right = tk.IntVar(value=250)
    tkrow= 0
    tk.Label(right_frame4, text="Increase time:").grid(row=tkrow, column=0,sticky="w")
    spin_inc_key_right = tk.Spinbox(right_frame4, from_=0, to=1000, increment=10, width=12, wrap=True,state="readonly",textvariable=spin_inc_key_var_right)
    spin_inc_key_right.grid(row=tkrow, column=1, padx=3, sticky="w")

    spin_dec_key_var_right = tk.IntVar(value=160)
    tkrow= tkrow + 1
    tk.Label(right_frame4, text="Decrease time:").grid(row=tkrow, column=0,sticky="w")
    spin_dec_key_right = tk.Spinbox(right_frame4, from_=0, to=1000, increment=10, width=12, wrap=True,state="readonly",textvariable=spin_dec_key_var_right)
    spin_dec_key_right.grid(row=tkrow, column=1, padx=3, sticky="w")

    spin_trigger_hold_high_right_var = tk.IntVar(value=0.7)
    tkrow= tkrow + 1
    tk.Label(right_frame4, text="[Trigger] Hold High:").grid(row=tkrow, column=0,sticky="w")
    spin_trigger_hold_high_right = tk.Spinbox(right_frame4, from_=0.00, to=1.00, increment=0.05, width=12, wrap=True,state="readonly",textvariable=spin_trigger_hold_high_right_var)
    spin_trigger_hold_high_right.grid(row=tkrow, column=1, padx=3, sticky="w")
    
    spin_trigger_hold_low_right_var = tk.IntVar(value=0.35)
    tkrow= tkrow + 1
    tk.Label(right_frame4, text="[Trigger] Hold Low:").grid(row=tkrow, column=0,sticky="w")
    spin_trigger_hold_low_right = tk.Spinbox(right_frame4, from_=0.00, to=1.00, increment=0.05, width=12, wrap=True,state="readonly",textvariable=spin_trigger_hold_low_right_var)
    spin_trigger_hold_low_right.grid(row=tkrow, column=1, padx=3, sticky="w")
    
    spin_trigger_slow_right_var = tk.IntVar(value=1.5)
    tkrow= tkrow + 1
    tk.Label(right_frame4, text="[Trigger] Alternative Speed %:").grid(row=tkrow, column=0,sticky="w")
    spin_trigger_slow_right = tk.Spinbox(right_frame4, from_=0.00, to=10.0, increment=0.1, width=12, wrap=True,state="readonly",textvariable=spin_trigger_slow_right_var)
    spin_trigger_slow_right.grid(row=tkrow, column=1, padx=3, sticky="w")
    
    tkrow= tkrow + 1
    use_autocenter_trigger_right = tk.IntVar()
    #tk.Label(right_frame4, text="[Trigger] AutoCenter/Reset Trigger:").grid(row=tkrow, column=0, sticky="w")
    #check_autocenter_trigger_right = tk.Checkbutton(right_frame4, text="Yes", variable=use_autocenter_trigger_right, onvalue=1, offvalue=0)
    #check_autocenter_trigger_right.grid(row=tkrow, column=1,sticky="w")
    use_autocenter_trigger_right.set(1)
    
    
    
    
    
  
    # CENTER FRAME
    center_frame = tk.LabelFrame(tab4, text="Wheel to Trigger:",width=600,height=100)
    center_frame.place(x=100, y=150)
    
    center_frame.grid_propagate(False)
    
    tkrow =0
    spin_inc_wheel_var = tk.IntVar(value=15)
    tkrow= tkrow + 1
    tk.Label(center_frame, text="[Trigger Wheel] Increase value:").grid(row=tkrow, column=0,sticky="w")
    spin_inc_wheel = tk.Spinbox(center_frame, from_=0, to=100, increment=1, width=12, wrap=True,state="readonly",textvariable=spin_inc_wheel_var)
    spin_inc_wheel.grid(row=tkrow, column=1, padx=3, pady=2, sticky="w")

    spin_dec_wheel_var = tk.IntVar(value=15)
    tkrow= tkrow + 1
    tk.Label(center_frame, text="[Trigger Wheel] Decrease value:").grid(row=tkrow, column=0,sticky="w")
    spin_dec_wheel = tk.Spinbox(center_frame, from_=0, to=100, increment=1, width=12, wrap=True,state="readonly",textvariable=spin_dec_wheel_var)
    spin_dec_wheel.grid(row=tkrow, column=1, padx=3, sticky="w")
    
    
    
    
    
 
    ##########################################
    # CONTENT FOR TAB FIVE
    ##########################################
    
    center_frame = tk.LabelFrame(tab5, text="Keymap:",width=600,height=200)
    center_frame.pack()
    #tk.Label(center_frame, text="Use generate.py on keymap folder").pack()
    tk.Button(center_frame, text="Execute generate.py", command=run_generate).pack()


    return root
    
    
def run_generate():
    os.startfile("keymap\\generate.bat")