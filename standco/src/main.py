from PyQt6 import QtWidgets
import sys
from standco.src.gui.stand_gui import Stand_Gui
from standco.src.managers.connection_manager import ConnectionManager
from standco.src.managers.relay_manager import RelayManager
from standco.src.managers.sensor_manager import SensorManager
from logger.data_logger import DataLogger

if __name__ == '__main__':
    # config_pressure_relays = "../configs/config_pressure_relays_test.json"
    # config_pressure_sensors = "../configs/config_pressure_sensors_test.json"
    # connection_manager_relay = ConnectionManager(config_pressure_relays)
    # connection_manager_relay.connect_to_sensors()
    # relay_manager = RelayManager(connection_manager_relay.clients)
    # relay_manager.read_states()
    # b = relay_manager.get_relay_states()
    app = QtWidgets.QApplication(sys.argv)
    win = Stand_Gui()
    win.show()
    sys.exit(app.exec())
