class RelayManager:

    def __init__(self, clients):
        self.relay_states = []
        self.clients = []
        for client in clients:
            if client["is_connected"]:
                self.clients.append(client)
                for relay in client["sensors"]:
                    self.relay_states.append({
                        "name": relay["name"],
                        "address": relay["address"],
                        "state": False})

    def read_states(self):
        read_byte_count = 8
        for client_data in self.clients:
            client = client_data["client"]
            slave_id = client_data["slave"]
            try:
                results = client.read_discrete_inputs(0, read_byte_count, slave=slave_id)
                if results and not results.isError():
                    states = results.bits[:read_byte_count]
                    for i, relay in enumerate(client_data["sensors"]):
                        if i < len(states):
                            state = bool(states[i])
                            for s in self.relay_states:
                                if s["name"] == relay["name"]:
                                    s["state"] = state
                                    break
                else:
                    print(f"Ошибка чтения")
            except Exception as e:
                raise Exception(f"Ошибка при опросе {e}")

    def get_relay_states(self):
        return self.relay_states
