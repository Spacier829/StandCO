import json

from pymodbus.client import ModbusTcpClient


class ConnectionManager:
    def __init__(self):
        self.clients = []
        self.sensors = []
        self.load_config(path="config.json")

    def load_config(self, path):
        with open(path, "r") as file:
            config = json.load(file)
        for device in config["devices"]:
            client = ModbusTcpClient(host=device["ip"], port=device["port"])
            if client.connect():
                print(f"Connected to {device['ip']}:{device['port']}")
                self.clients.append({"client": client, "sensors": device["sensors"]})
            else:
                print(f"Failed to connect to {device['ip']}:{device['port']}")

    def read_sensors(self):
        states = []
        for device in self.clients:
            client = device["client"]
            for sensor in device["sensors"]:
                try:
                    result = client.read_discrete_inputs(sensor["address"], 1)
                    if result.isError():
                        states.append(False)
                    else:
                        states.append(True)
                except Exception as e:
                    print(f"Error reading sensor {sensor['name']}: {e}")
                    states.append(False)

    def close(self):
        for client in self.clients:
            client.close()


