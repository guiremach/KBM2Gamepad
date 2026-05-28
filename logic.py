threadExecutionInterval = 5

def calculate_rate(max, time):
    if time > 0:
        return max / (time / threadExecutionInterval)
    else:
        return max
# These were +1 and -1 in source material.
# You MUST use +/- 2 for My Summer Car or axis may spontaneously invert
int32_max = (2 ** 14) - 2
int32_min = (( 2 ** 14) * -1) + 2

int32_max = 32767
int32_min = 0

# =============================================================================================
# //////////////////////////////////////// SETTINGS ///////////////////////////////////////////
# =============================================================================================
# Mouse settings
# =============================================================================================
# Higher SCR = Smoother/Slower Response | Lower SCR = Harder/Quicker Response
# With the game's built in steering settings, there's no need to change the scr value
# SCR's effects can be felt better with arcade style racing games
global mouse_sensitivity, sensitivity_center_reduction
mouse_sensitivity = 15
sensitivity_center_reduction = 15
# =============================================================================================
# Steering settings
# =============================================================================================
global steering, steering_max, steering_min, steering_center_reduction	
# Init values, do not change
steering = 0.0
rz = 0
steering_max = float(int32_max)
steering_min = float(int32_min)
steering_center_reduction = 1.0
# =============================================================================================
# Throttle, Break, and Control Keys:
# =============================================================================================
global throttle_key, throttle_key_sec, throttle_key_ter, brake_key, throttle_key_hold, reset_key
global space_reset_enabled, low_mode_enabled, steering_key_pause
#throttle_key = Key.A
#throttle_key_sec = Key.D2
#brake_key = Key.S
#throttle_key_hold = Key.D3
#reset_key = Key.D4
#steering_key_pause = Key.D5
#Change "True" to "False" to disable Space Bar as reset and low mode respecitvely
space_reset_enabled = True
low_mode_enabled = True
# =============================================================================================
# Throttle settings
# =============================================================================================
# Set throttle behaviour with the increase and decrease time (ms)
# the actual increase and decrease rates are calculated automatically
throttle_increase_time = 160
throttle_decrease_time = 80

#throttle_increase_time = 660
#throttle_decrease_time = 800

# global declarations
global throttle, throttle_max, throttle_min, throttle_increase_rate, throttle_decrease_rate
global throttle_sec, throttle_low
global throttle_sec_set, throttle_hold_set, throttle_inc_mod, throttle_dec_mod, throttle_low_set
global braking_sec
#initialization values. Do not change.
throttle_max = int32_max
throttle_min = int32_min
throttle_increase_rate = calculate_rate(throttle_max, throttle_increase_time)
throttle_decrease_rate = calculate_rate(throttle_max, throttle_decrease_time) * -1
throttle_sec_set = False
throttle_hold_set = False
throttle_low_set = False	
throttle = throttle_rx = throttle_min
throttle_y = throttle_ry = throttle_min
#additional setup parameters
# _sec and _low modifiers are used to lower maximum values
# _mod values are for alternate attack and release rates
throttle_sec = 0.63 * int32_max
throttle_low = 0.4 * int32_max
throttle_inc_mod = 0.25
throttle_dec_mod = 0.15	
# =============================================================================================
# Braking settings
# =============================================================================================
# Set throttle behaviour with the increase and decrease time (ms)
# the actual increase and decrease rates are calculated automatically
braking_increase_time = 60
braking_decrease_time = 100
# Init values, do not change
global braking, braking_max, braking_min, braking_increase_rate
global braking_decrease_rate, braking_sec
braking_sec = 0.5 * int32_max
braking_max = int32_max
braking_min = int32_min
braking = braking_min
braking_increase_rate = calculate_rate(braking_max, braking_increase_time)
braking_decrease_rate = calculate_rate(braking_max, braking_decrease_time) * -1  