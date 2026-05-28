import keyboard



def key_on_off(ev):
    global keyh
    global muted_key
    global lbl0_var, lbl0_swtich
    global lbl0_swtich
    global root
    global lbl0_var, lbl01_swtich
    #print(ev.event_type)
    #print(ev.scan_code)
    scan_code = ev.scan_code
    if ev.is_keypad:
        scan_code = ev.scan_code+1000
    
    if (ev.event_type == 'down' and scan_code not in keyh.pressed):
        keyh.press(scan_code)
    elif (ev.event_type == 'up'):
        keyh.release(scan_code)
        

    if (scan_code == 15 and ev.event_type == 'down'):
        keyh.muted_joy = not keyh.muted_joy
        if keyh.muted_joy:
            print('Key TO Joy muted')
        else:
            print('Key TO Joy unmuted')
            
        
    if (scan_code == 41 and ev.event_type == 'down'):
        keyh.muted_key = not keyh.muted_key
        if keyh.muted_key:
            keyboard.unhook_all()
            keyboard.hook(key_on_off, suppress=True)
            print('Keyboard muted')
        else:
            keyboard.unhook_all()
            keyboard.hook(key_on_off, suppress=False)
            print('Keyboard unmuted')
    
class keyhook:
    #def __init__(self, btns):
    def __init__(self):
        self.pressed = []
        self.muted_joy = False
        self.muted_key = True
        #self.btns = btns
        #print(btns)
        #self.age = age
    def press(self, key):
        self.pressed.append(key)
        
    def release(self, key):
        if key in self.pressed:
            self.pressed.remove(key)
        
keyh = keyhook()   