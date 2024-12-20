import struct


class SensorManager:

    def __init__(self, clients):
        self.sensor_values = []
        self.clients = []
        for client in clients:
            if client["is_connected"]:
                self.clients.append(client)
                for sensor in client["sensors"]:
                    self.sensor_values.append({
                        "name": sensor["name"],
                        "pressure": 0.0,
                        "temperature": 0.0})

    def read_values(self):
        read_byte_count = 4
        for client_data in self.clients:
            client = client_data["client"]
            slave_id = client_data["slave"]
            for sensor in client_data["sensors"]:
                try:
                    result = client.read_input_registers(0, read_byte_count, slave=slave_id)
                    if result and not result.isError():
                        pressure = struct.unpack(">f", struct.pack(">HH", result.registers[1], result.registers[0]))[0]
                        temperature = struct.unpack(">f", struct.pack(">HH", result.registers[3], result.registers[2]))[
                            0]
                        for s in self.sensor_values:
                            if s["name"] == sensor["name"]:
                                s["pressure"] = pressure
                                s["temperature"] = temperature
                                break
                    else:
                        print(f"Ошибка чтения")
                except Exception as e:
                    print(f"Ошибка при опросе {e}")

    def get_sensor_values(self):
        return self.sensor_values
