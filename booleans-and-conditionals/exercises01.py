# Assign the variables for exercise 1 here:
engine_indicator_light =  "red blinking"
space_suits_on = True
shuttle_cabin_ready = True
crew_status = space_suits_on and shuttle_cabin_ready
computer_status_code = 200
shuttle_speed = 15000



# BEFORE running the code, predict what will be printed to the console by the following statements:
# It will print "engines are off"

if engine_indicator_light == "green": #if returns True, then
  print("engines have started") #print this string
elif engine_indicator_light == "green blinking": #if the first condition returns false, check this
  print("engines are preparing to start") #print if elif returned True
else: #if both conditions returned False, 
  print("engines are off") #print this

  