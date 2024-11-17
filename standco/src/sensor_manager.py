class SensorManager:
    def __init__(self, devices):
        self.sensors = []
        for device in devices:
            for sensor in device["sensors"]:
                self.sensors.append({
                    "name": sensor["name"],
                    "address": sensor["address"],
                    "state": False})

    def update_sensors_states(self, states):
        for sensor, state in zip(self.sensors, states):
            sensor["state"] = state

    def get_sensors_states(self):
        return self.sensors