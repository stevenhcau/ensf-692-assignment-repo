# input_processing.py
# YOUR NAME, ENSF 692 P24
# A terminal-based program for processing computer vision changes detected by a car.
# Detailed specifications are provided via the Assignment 2 README file.
# You must include the code provided below but you may delete the instructional comments.
# You may add your own additional classes, functions, variables, etc. as long as they do not contradict the requirements (i.e. no global variables, etc.). 
# You may import any modules from the standard Python library.
# Remember to include your name and comments.



# No global variables are permitted


# You do not need to provide additional commenting above this class, just the user-defined functions within the class
class Sensor:

    # Must include a constructor that uses default values
    # You do not need to provide commenting above the constructor
    def __init__(self):
        self.lightStatus = 'green'
        self.pedestrianStatus = 'no'
        self.vehicleStatus = 'no'

    # # Replace these comments with your function commenting
    def update_status(self): # You may decide how to implement the arguments for this function
        print("Are changes detected in the vision input?")

        userInput = input("Select 1 for light, 2 for pedestrian, 3 for vehicle, or 0 to end the program >>> ")

        if(userInput == '0'):
            self.programStatus = False

        if(userInput == '1'):
           self.update_light()

        if(userInput == '2'):
            self.update_pedestrian()

        if(userInput == '3'):
            self.update_vehicle()


    def update_light(self):
        lightInput = input("Type in the new light status >>> ")
        if lightInput == 'red' or lightInput == 'yellow' or lightInput == 'green':
            self.lightStatus = lightInput
        else:
            print("Error, please enter 'green', 'yellow', or 'red'")

    def update_pedestrian(self):
        pedestrianInput = input("Type in the new pedestrian status >>> ")
        if pedestrianInput == 'yes' or pedestrianInput == 'no':
            self.pedestrianStatus = pedestrianInput
        else:
            print("Error, please enter 'yes' or 'no'")
    
    def update_vehicle(self):
        vehicleInput = input("Type in the new vehicle status >>> ")
        if vehicleInput == 'yes' or vehicleInput == 'no':
            self.vehicleStatus = vehicleInput
        else:
            print("Error, please enter 'yes' or 'no'")

    # def update_obstacle(userInput):
        

# The sensor object should be passed to this function to print the action message and current status
# Replace these comments with your function commenting
# def print_message(sensor):
#     print()



# Complete the main function below
def main():
    sensorClass = Sensor()
    print("\n***ENSF 692 Car Vision Detector Processing Program***\n")
    sensorClass.update_status()
    print(sensorClass.lightStatus)
    




# Conventional Python code for running main within a larger program
# No additional code should be included below this
if __name__ == '__main__':
    main()

