from connection_manager import ConnectionManager
from sensor_manager import SensorManager

if __name__ == '__main__':
    connection_manager = ConnectionManager()
    connection_manager.connect_to_sensors()
    sensor_manager = SensorManager(connection_manager.clients)

    while True:
        sensor_manager.read_discrete_inputs()
        result = sensor_manager.get_sensors_states()
        print(result)
    a = 123
