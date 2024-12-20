from states_reader.states_reader import StatesReader
from managers.connection_manager import ConnectionManager
from managers.relay_manager import RelayManager
from managers.sensor_manager import SensorManager
from logger.data_logger import DataLogger

if __name__ == '__main__':
    states_reader = StatesReader()
    states_reader.print_states()
    config_pressure_relays = "../configs/config_pressure_relays.json"
    config_pressure_sensors = "../configs/config_pressure_sensors.json"
    # --------------- Обертка для конфиг файлов в считывании--------------------------
    try:
        relays_connection_manager_test = ConnectionManager(config_pressure_relays)
        relays_connection_manager_test.connect_to_sensors()
    except FileNotFoundError as exception:
        print(exception)
    # --------------------------------------------------------------------------------
    relays_manager_test = RelayManager(relays_connection_manager_test.clients)
    relays_manager_test.read_states()

