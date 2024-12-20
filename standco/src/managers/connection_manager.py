import json
from pymodbus.client import ModbusTcpClient


class ConnectionManager:
    def __init__(self, path):
        self.clients = []
        self.load_config(path)

    def load_config(self, path):
        with open(path, "r") as file:
            self.config = json.load(file)

    def connect_to_sensors(self):
        for device in self.config["devices"]:
            client = ModbusTcpClient(host=device["ip"], port=device["port"])
            if not client.connect():
                raise ConnectionError(f"Ошибка подключения к {device['ip']}:{device['port']}")
            self.clients.append({"client": client,
                                 "slave": device["slave"],
                                 "sensors": device["sensors"]})

    def close(self):
        for client in self.clients:
            client.close()
