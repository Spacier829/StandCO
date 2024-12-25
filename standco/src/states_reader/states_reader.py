from standco.src.managers.connection_manager import ConnectionManager
from standco.src.managers.relay_manager import RelayManager
from standco.src.managers.sensor_manager import SensorManager
from loggers.data_logger import DataLogger


class StatesReader:
    def __init__(self):
        config_pressure_relays = "../configs/config_pressure_relays_test.json"
        config_pressure_sensors = "../configs/config_pressure_sensors_test.json"

        self.connection_manager_relays = ConnectionManager(config_pressure_relays)

        self.connection_manager_sensors = ConnectionManager(config_pressure_sensors)
        self.connection_manager_relays.connect()
        self.connection_manager_sensors.connect()

        self.relays_manager = RelayManager(self.connection_manager_relays.clients)
        self.sensors_manager = SensorManager(self.connection_manager_sensors.clients)

        self.logger = DataLogger()

    def read(self):
        self.relays_manager.read_states()
        result_relays = self.relays_manager.get_relay_states()

        self.sensors_manager.read_values()
        result_sensors = self.sensors_manager.get_sensor_values()
        if not self.logger.file_initialized:
            self.logger.initialize_file(result_relays, result_sensors)

        self.logger.log_data(result_relays, result_sensors)
        return result_relays, result_sensors

    def close_util(self):
        self.connection_manager_sensors.close()
        self.connection_manager_relays.close()
