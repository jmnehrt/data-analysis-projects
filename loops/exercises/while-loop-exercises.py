# Define three variables for the LaunchCode shuttle - one for the starting fuel level, another for the number of astronauts aboard, and the third for the altitude the shuttle reaches.
starting_fuel_level = 0 #to initialize a variable that will be changed by input or by the code's iteration, assign it a value of zero to begin. at this pount, it's jsut to estbalish that this variable exists so the code can refer to it later
astronauts_on_board = 0
shuttle_altitude = 0 




# Exercise #1: Construct while loops to do the following:
  # a. Query the user for the starting fuel level. Validate that the user enters a positive, integer value greater than 5000 but less than 30000. 

# while starting_fuel_level <= 5000 or starting_fuel_level > 30000: #the condition in the first line of the loop is what keeps it running
#    starting_fuel_level = int(input('Enter the starting fuel level: ')) #input but changed the string to an integer
   

# b. Use a second loop to query the user for the number of astronauts (up to a maximum of 7). Validate the entry.
# while astronauts_on_board <= 0 or astronauts_on_board >= 8: #the condition in the first line of the loop is what keeps it running
#   astronauts_on_board = int(input('Enter the number of astronauts on board: ')) #input but changed the string to an integer
   
  

# c. Use a final loop to monitor the fuel status and the altitude of the shuttle. Each iteration, decrease the fuel level by 100 units for each astronaut aboard. Also, increase the altitude by 50 kilometers.
while shuttle_altitude >= 0:
    



# Exercise #2: Print the result with the phrase, The shuttle gained an altitude of ___ km and has ___ kg of fuel left. Fill in the blanks with the altitude and fuel level values.

# If the altitude is 2000 km or higher, add “Orbit achieved!” Otherwise add, “Failed to reach orbit.”
