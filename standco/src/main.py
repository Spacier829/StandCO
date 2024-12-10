from time import sleep

from connection_manager import ConnectionManager
from relay_manager import RelayManager
from sensor_manager import SensorManager

if __name__ == '__main__':
    # config_pressure_relay = "../configs/config_pressure_relay.json"
    config_pressure_sensor = "../configs/config_pressure_sensor.json"
    # connection_manager_relay = ConnectionManager(config_pressure_relay)
    connection_manager_sensors = ConnectionManager(config_pressure_sensor)
    # connection_manager_relay.connect_to_sensors()
    connection_manager_sensors.connect_to_sensors()
    # relay_manager = RelayManager(connection_manager_relay.clients)
    sensors_manager = SensorManager(connection_manager_sensors.clients)
    while True:
        # relay_manager.read_states()
        # result = relay_manager.get_relay_states()
        # for i in range(len(result)):
        #     test = result[i]
        #     print(test["name"] + " " + str(test["state"]))
        sensors_manager.read_values()
        result = sensors_manager.get_sensor_values()
        for i in range(len(result)):
            test = result[i]
            print(test["name"] + " " + str(test["pressure"]) + " " + str(test["temperature"]))
            sleep(1)
