import signal

from standco.src.managers.connection_manager import ConnectionManager
from standco.src.managers.relay_manager import RelayManager
from standco.src.managers.sensor_manager import SensorManager
from loggers.data_logger import DataLogger
from time import sleep


class StatesReader:
    def __init__(self):
        config_pressure_relays = "../configs/config_pressure_relays.json"
        config_pressure_sensors = "../configs/config_pressure_sensors.json"

        self.connection_manager_relays = ConnectionManager(config_pressure_relays)

        self.connection_manager_sensors = ConnectionManager(config_pressure_sensors)
        self.connection_manager_relays.connect_to_sensors()
        self.connection_manager_sensors.connect_to_sensors()

        self.relays_manager = RelayManager(self.connection_manager_relays.clients)
        self.sensors_manager = SensorManager(self.connection_manager_sensors.clients)

        self.logger = DataLogger()

        self.is_running = True

        signal.signal(signal.SIGINT, self.signal_handler)

    def signal_handler(self, sig, frame):
        print("Остановка программы")
        self.is_running = False

    def read(self):
        self.relays_manager.read_states()
        result_relays = self.relays_manager.get_relay_states()

        self.sensors_manager.read_values()
        result_sensors = self.sensors_manager.get_sensor_values()
        return result_relays, result_sensors

    def print_states(self):
        while self.is_running:
            try:
                relays_states, sensors_values = self.read()
                if not self.logger.file_initialized:
                    self.logger.initialize_file(relays_states, sensors_values)

                self.logger.log_data(relays_states, sensors_values)

                for relay in relays_states:
                    print(f"{relay['name']}: {relay['state']}")
                for sensor in sensors_values:
                    print(f"{sensor['name']}: P={sensor['pressure']:.4f}, T={sensor['temperature']:.4f}")
                sleep(1)
            except Exception as e:
                print(f"Ошибка:{e}")
                break
