class SensorManager:

    def __init__(self, clients):
        self.sensors_states = []
        self.clients = clients
        for client in clients:
            for sensor in client["sensors"]:
                self.sensors_states.append({
                    "name": sensor["name"],
                    "state": None})

    def read_discrete_inputs(self):
        read_bytes_count = 1
        for client_data in self.clients:
            client = client_data["client"]
            slave_id = client_data["slave"]
            for sensor in client_data["sensors"]:
                try:
                    address = sensor["address"]
                    result = client.read_discrete_inputs(address, read_bytes_count, slave=slave_id)
                    if result and not result.isError():
                        state = bool(result.bits[0])
                        for s in self.sensors_states:
                            if s["name"] == sensor["name"]:
                                s["state"] = state
                    else:
                        print(f"Ошибка чтения {sensor['name']} ({address})")
                except Exception as e:
                    print(f"Ошибка при опросе {sensor['name']} ({address}): {e}")

    def get_sensors_states(self):
        return self.sensors_states
