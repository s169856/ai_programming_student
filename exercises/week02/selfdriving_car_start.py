"""
Oefening 1: Self-Driving Car (Model-based Reflex Agent)
========================================================
Implementeer een agent die zijn voorligger volgt.
"""


class LidarSensorInput:
    def __init__(self, distance=0.0):
        self.DistanceTo = distance


class Brake:
    def __str__(self):
        return "BRAKE"


class Nothing:
    def __str__(self):
        return "NOTHING"


class SelfDrivingCar:
    def __init__(self):
        # TODO: interne state — welke variabele heb je nodig?
        self.last_distance = 0

    def process(self, sensor_input: LidarSensorInput):
        # TODO: bereken relatieve snelheid en tijd tot botsing; 
        #       rem als tijd < 5 seconden
        current_distance  = sensor_input.DistanceTo

        if self.last_distance is None:
            self.last_distance = current_distance
            return Nothing()

        speed = self.last_distance - current_distance
    
        if speed != 0:
            time = current_distance / speed

        self.last_distance = current_distance

        if time < 5:
            return Brake()
        else:
            return Nothing()


if __name__ == "__main__":
    sensor = LidarSensorInput(10)
    agent = SelfDrivingCar()

    for afstand in [10, 15, 13, 10, 8, 6, 4, 3]:
        sensor.DistanceTo = afstand
        action = agent.process(sensor)
        print(f"Afstand: {afstand}m -> {action}")