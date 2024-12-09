import csv
from datetime import datetime


class DataLogger:
    def __init__(self):
        self.file_name = f"sensor_log_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.csv"
        self.file_initialized = False

    def initialize_file(self, relay_states, sensor_values):
        if not self.file_initialized:
            relay_headers = [relay["name"] for relay in relay_states]
            sensor_headers = [f"{sensor['name']} (P)" for sensor in sensor_values] + \
                             [f"{sensor['name']} (T)" for sensor in sensor_values]
            headers = ["Time"] + relay_headers + sensor_headers

            with open(self.file_name, mode="w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(headers)
            self.file_initialized = True

    def log_data(self, relay_states, sensor_values):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        relay_values = [int(relay["state"]) for relay in relay_states]
        sensor_values_flat = [sensor["pressure"] for sensor in sensor_values] + \
                             [sensor["temperature"] for sensor in sensor_values]
        row = [timestamp] + relay_values + sensor_values_flat

        with open(self.file_name, mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(row)



logger = SensorLogger()

while True:
    # Считываем данные с реле и датчиков
    relays_manager.read_states()
    result_relays = relays_manager.get_relay_states()

    sensors_manager.read_values()
    result_sensors = sensors_manager.get_sensor_values()

    # Инициализируем файл с заголовками (один раз)
    if not logger.file_initialized:
        logger.initialize_file(result_relays, result_sensors)

    # Логируем данные
    logger.log_data(result_relays, result_sensors)

    # Печать данных (для проверки)
    for relay in result_relays:
        print(f"{relay['name']}: {relay['state']}")
    for sensor in result_sensors:
        print(f"{sensor['name']}: Pressure={sensor['pressure']}, Temperature={sensor['temperature']}")

    sleep(1)
