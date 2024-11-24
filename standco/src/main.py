from connection_manager import ConnectionManager
from relay_manager import RelayManager

if __name__ == '__main__':
    config_pressure_relay = "../configs/config_pressure_relay.json"
    connection_manager = ConnectionManager(config_pressure_relay)
    connection_manager.connect_to_sensors()
    sensor_manager = RelayManager(connection_manager.clients)

    while True:
        sensor_manager.read_discrete_inputs()
        result = sensor_manager.get_sensors_states()
        print(result)
    a = 123
