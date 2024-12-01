class RelayManager:

    def __init__(self, clients):
        self.relay_states = []
        self.clients = clients
        for client in clients:
            for relay in client["sensors"]:
                self.relay_states.append({
                    "name": relay["name"],
                    "address": relay["address"],
                    "state": False})

    def read_discrete_inputs(self):
        read_byte_count = 1
        for client_data in self.clients:
            client = client_data["client"]
            slave_id = client_data["slave"]
            for relay in client_data["sensors"]:
                try:
                    address = relay["address"]
                    result = client.read_discrete_inputs(address, read_byte_count, slave=slave_id)
                    if result and not result.isError():
                        state = bool(result.bits[0])
                        for s in self.relay_states:
                            if s["name"] == relay["name"]:
                                s["state"] = state
                                break
                    else:
                        print(f"Ошибка чтения")
                except Exception as e:
                    print(f"Ошибка при опросе {e}")

    def get_relay_states(self):
        return self.relay_states
