# input_processing.py
# Steven (Han) Au, ENSF 692 P24

class Sensor:

    # Constructor to set default values
    def __init__(self):
        self.lightStatus = 'green'
        self.pedestrianStatus = 'no'
        self.vehicleStatus = 'no'
        self.programStatus = True

    # Updates the vision input status
    def update_status(self):
        print("Are changes detected in the vision input?")

        userInput = input("Select 1 for light, 2 for pedestrian, 3 for vehicle, or 0 to end the program >>> ")
        if(userInput == '0' or
           userInput == '1' or
           userInput == '2' or
           userInput == '3'):
            
            if(userInput == '0'):
                print("Exiting program...")
                self.programStatus = False

            if(userInput == '1'):
                self.update_light()
                print_message(self)

            if(userInput == '2'):
                self.update_pedestrian()
                print_message(self)

            if(userInput == '3'):
                self.update_vehicle()
                print_message(self)

        else:
            print("You must select 1, 2, 3, or 0.\n")
            

    # Gets input for updating the light color, also checks the input for validity
    def update_light(self):
        lightInput = input("Type in the new light status >>> ")
        if lightInput == 'red' or lightInput == 'yellow' or lightInput == 'green':
            self.lightStatus = lightInput
        else:
            print("Invalid Vision Change")

    # Gets input for updating the pedestrian status, also checks the input for validity
    def update_pedestrian(self):
        pedestrianInput = input("Type in the new pedestrian status >>> ")
        if pedestrianInput == 'yes' or pedestrianInput == 'no':
            self.pedestrianStatus = pedestrianInput
        else:
            print("Invalid Vision Change")
    # Gets input for updating the vehicle status, also checks the input for validity    
    def update_vehicle(self):
        vehicleInput = input("Type in the new vehicle status >>> ")
        if vehicleInput == 'yes' or vehicleInput == 'no':
            self.vehicleStatus = vehicleInput
        else:
            print("Invalid Vision Change")

    # checks scenario and prints the valid output
    def check_scenario(self):
        if self.lightStatus == 'red' or self.pedestrianStatus == 'yes' or self.vehicleStatus == 'yes':
            return "STOP"
        if self.lightStatus == 'green' and self.pedestrianStatus == 'no' and self.vehicleStatus == 'no':
            return "PROCEED"
        if self.lightStatus == 'yellow' and self.pedestrianStatus == 'no' and self.vehicleStatus == 'no':
            return "CAUTION"


def print_message(sensor):
    print("\n" + sensor.check_scenario())
    print("\nLight = " + sensor.lightStatus + 
          " , Pedestrian = " + sensor.pedestrianStatus +
          " , Vehicle = " + sensor.vehicleStatus + "\n")


def main():
    sensorClass = Sensor()
    print("\n***ENSF 692 Car Vision Detector Processing Program***\n")
    while sensorClass.programStatus:
        sensorClass.update_status()

# Conventional Python code for running main within a larger program
# No additional code should be included below this
if __name__ == '__main__':
    main()

