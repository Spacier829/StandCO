from standco.src.managers.connection_manager import ConnectionManager


class ConnectionUtil:
    def __init__(self):
        config_pressure_relays = "../configs/relays_config_test.json"
        config_pressure_sensors = "../configs/sensors_config_test.json"

        self.connection_manager_relays = ConnectionManager(config_pressure_relays)

        self.connection_manager_sensors = ConnectionManager(config_pressure_sensors)
        self.connection_manager_relays.connect()
        self.connection_manager_sensors.connect()

    def get_relays_connections(self):
        return self.connection_manager_relays

    def get_sensors_connections(self):
        return self.connection_manager_sensors

    def close(self):
        self.connection_manager_relays.close()
        self.connection_manager_sensors.close()
