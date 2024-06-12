from abc import ABC, abstractmethod
import random

class GreenhouseConsole(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def checkStatus(self):
        pass

    @abstractmethod
    def exit(self):
        pass

class GreenhouseStart(GreenhouseConsole):
    def __init__(self):
        self.status = False

    def start(self):
        print("The greenhouse console has started")
        self.status = True

    def checkStatus(self):
        return self.status
    
    def exit(self):
        print("Exiting the greenhouse console.")
        self.status = False

class Temperature(GreenhouseConsole):
    def __init__(self):
        self.temperature = random.randint(80, 110)
        print(f"The current temperature is {self.temperature} degrees Fahrenheit.")

    def check_temperature(self):
        print(f"The current temperature is {self.temperature} degrees Fahrenheit.")

    def fan_on(self):
        self.temperature -= 5
        print("Fan turned on. Cooling down.")
        self.check_temperature()
    
    def heater_on(self):
        self.temperature += 5
        print("Heater turned on. Warming up.")
        self.check_temperature()

    def start(self):
        print("Temperature control started.")
    
    def checkStatus(self):
        print(f"Temperature control status: {self.temperature}")
        return self.temperature
    
    def exit(self):
        print("Temperature control stopped.")
        self.temperature = None

# Testing the classes
greenhouse_console = GreenhouseStart()
greenhouse_console.start()
print(greenhouse_console.checkStatus())
greenhouse_console.exit()

temperature_control = Temperature()
temperature_control.start()
temperature_control.check_temperature()
temperature_control.fan_on()
temperature_control.heater_on()
temperature_control.exit()