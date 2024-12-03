from tabulate import tabulate
from datetime import datetime


class DataLogger:
    def __init__(self, relay_states, sensor_values):
        self.start_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        self.file_path = f"data_log_{self.start_time}.txt"
        self.relay_states = relay_states  # Данные реле
        self.sensor_values = sensor_values  # Данные датчиков

    def log_data(self, relay_states, sensor_values):
        # Заголовки таблицы
        relay_headers = [relay["name"] for relay in relay_states]
        sensor_headers = [f"{sensor['name']} (P)" for sensor in sensor_values] + \
                         [f"{sensor['name']} (T)" for sensor in sensor_values]
        self.headers = ["Time"] + relay_headers + sensor_headers

        # Значения для записи
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        relay_values = [int(relay["state"]) for relay in relay_states]
        sensor_values = [sensor["pressure"] for sensor in sensor_values] + \
                        [sensor["temperature"] for sensor in sensor_values]
        self.row = [timestamp] + relay_values + sensor_values

    def initialize_table(self):
        # Форматирование таблицы
        return tabulate([self.row], headers=self.headers, tablefmt="grid")

    def update_table(self):
        return tabulate([self.row], tablefmt="grid")

    def write_to_log(self, table_data):
        # Сохранение в файл
        with open(self.file_path, "a") as file:
            file.write(table_data + "\n\n")  # Разделяем записи пустой строкой
        print("Данные записаны в файл.")