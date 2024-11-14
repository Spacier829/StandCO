import json
from pymodbus.client import ModbusTcpClient

with open('config.json', 'r') as config_file:
    config = json.load(config_file)

clients = []

def connect_to_sensors():
    for sensor in config['sensors']:
        client = ModbusTcpClient(host=sensor['ip'], port=sensor['port'])
        if client.connect():
            print(f"Connected to {sensor['ip']}:{sensor['port']}")
            clients.append(client)
        else:
            print(f"Failed to connect to {sensor['ip']}:{sensor['port']}")

connect_to_sensors()
