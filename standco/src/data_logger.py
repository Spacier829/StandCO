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
