import json
from pymodbus.client import ModbusTcpClient


class Connection:
    clients = []

    def connect_to_sensors(self):
        with open('config.json', 'r') as config_file:
            config = json.load(config_file)
        for sensor in config['sensors']:
            client = ModbusTcpClient(host=sensor['ip'], port=sensor['port'])
            if client.connect():
                print(f"Connected to {sensor['ip']}:{sensor['port']}")
                self.clients.append(client)
            else:
                print(f"Failed to connect to {sensor['ip']}:{sensor['port']}")
