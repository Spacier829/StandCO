import time


class RelayManager:

    def __init__(self, clients):
        self.relay_states = []
        self.clients = clients
        for client in clients:
            for relay in client["sensors"]:
                self.relay_states.append({
                    "name": relay["name"],
                    "address": relay["address"],
                    "state": None})

    def read_discrete_inputs(self):
        read_bytes_count = 8
        start_time = time.time()
        for client_data in self.clients:
            # Здесь нужно установить счетчик, который будет помогать ставить состояние по адресу
            client = client_data["client"]
            slave_id = client_data["slave"]
            try:
                result = client.read_discrete_inputs(0, read_bytes_count, slave_id)
                if result and not result.isError():
                    for i in range(len(result.bits)):
                        for s in self.relay_states:
                            # Здесь нужно добавить проверку индекса либо адреса для установки всех значений состояний
                            state = result.bits[i]
                            if s["address"] == i:
                                s["state"] = state
                                break
                else:
                    print(f"Ошибка чтения")
            except Exception as e:
                print(f"Ошибка при опросе {e}")
        end_time = time.time()
        elapsed_time = end_time - start_time
        a = 123

    def get_relay_states(self):
        return self.sensors_states
