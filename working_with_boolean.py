# Demonstration of Boolean
# True and False (Initial Caps) are keyword values
# Don't confuse them with TRUE and FALSE which are constants
# that have to have a value assigned to them.

light_switch = True
if light_switch: # Using a boolean in a conditional statement
    print (f"The light switch is ON")
else:
    print (f"The light switch is OFF")

light_switch = False
if light_switch: # light_switch is True
    print(f"The light switch is ON")
else:  # light_switch is FALSE
    print(f"The light switch is OFF")
