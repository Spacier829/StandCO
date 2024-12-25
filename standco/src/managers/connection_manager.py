import json
from pymodbus.client import ModbusTcpClient


class ConnectionManager:
    def __init__(self, path):
        self.clients = []
        self.load_config(path)

    def load_config(self, path):
        try:
            with open(path, "r") as file:
                self.config = json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError(f"Ошибка открытия файла конфигурации.")

    def connect(self):
        for device in self.config["devices"]:
            client = ModbusTcpClient(host=device["ip"], port=device["port"])
            is_connected = False
            if client.connect():
                is_connected = True
            self.clients.append({"client": client,
                                 "slave": device["slave"],
                                 "sensors": device["sensors"],
                                 "is_connected": is_connected})

    def close(self):
        for client in self.clients:
            client.close()
