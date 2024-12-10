class SensorManager:

    def __init__(self, clients):
        self.sensor_values = []
        self.clients = clients
        for client in clients:
            for sensor in client["sensors"]:
                self.sensor_values.append({
                    "name": sensor["name"],
                    "pressure": 0.0,
                    "temperature": 0.0})

    def combine_to_float(self, high, low):
        combined = (low << 16) | high
        float_value = int.to_bytes(combined, length=4, byteorder='big', signed=False)
        return float.fromhex(float_value.hex())

    def read_values(self):
        read_byte_count = 4
        for client_data in self.clients:
            client = client_data["client"]
            slave_id = client_data["slave"]
            for sensor in client_data["sensors"]:
                try:
                    result = client.read_input_registers(0, read_byte_count, slave=slave_id)
                    if result and not result.isError():
                        pressure = self.combine_to_float(result.registers[0], result.registers[1])
                        temperature = self.combine_to_float(result.registers[2], result.registers[3])
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
