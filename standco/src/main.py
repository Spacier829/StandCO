from connection_manager import ConnectionManager
from relay_manager import RelayManager

if __name__ == '__main__':
    config_pressure_relay = "../configs/config_pressure_relay.json"
    connection_manager = ConnectionManager(config_pressure_relay)
    connection_manager.connect_to_sensors()
    relay_manager = RelayManager(connection_manager.clients)

    while True:
        relay_manager.read_discrete_inputs()
        result = relay_manager.get_relay_states()
        for i in range(len(result)):
            test = result[i]
            print(test["name"] + " " + str(test["state"]))
        a = 123
