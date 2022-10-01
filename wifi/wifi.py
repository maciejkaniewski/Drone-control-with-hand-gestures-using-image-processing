import subprocess

DRONE_WIFI_NETWORK_NAME = 'TELLO-F11F4E'


class WiFi:
    """
    Class that handles events related to the Wi-Fi network.
    """

    def __init__(self):
        """
        Constructs Wi-Fi object.
        """

        self.is_there_active_connection = False
        self.available_networks = []
        self.signal_strength = 0

    def find_available_networks(self) -> None:
        """
        Finds available Wi-Fi networks
        """

        process = subprocess.run(['nmcli', '-t', '-f', 'SSID,SECURITY,SIGNAL', 'dev', 'wifi'], stdout=subprocess.PIPE)
        if process.returncode == 0:
            self.available_networks = process.stdout.decode('utf-8').strip().split('\n')
        else:
            self.available_networks = []

    def is_wifi_available(self, ssid: str) -> bool:
        """
        Checks if a Wi-Fi network with the given name is available.

        :param ssid: name of the Wi-Fi network (Service Set Identifier)
        :return: True if Wi-Fi is available
        """

        return ssid in [x.split(':')[0] for x in self.available_networks]

    def connect_to(self, ssid: str, password: str) -> bool:
        """
        Connects to the Wi-Fi network with the given name.

        :param ssid: name of the Wi-Fi network (Service Set Identifier)
        :param password: password for the Wi-Fi network
        :return: True if successfully connected
        """

        if not self.is_wifi_available(ssid):
            return False
        subprocess.call(['nmcli', 'd', 'wifi', 'connect', ssid, 'password', password])
        return self.is_connected_to(ssid)

    @staticmethod
    def current_connection() -> str:
        """
        Checks which Wi-Fi network is currently connected.

        :return: Current network name
        """
        process = subprocess.run(['nmcli', '-t', '-f', 'ACTIVE,SSID', 'dev', 'wifi'], stdout=subprocess.PIPE)
        if process.returncode == 0:
            return [i for i in process.stdout.decode('utf-8').strip().split('\n')
                    if i.startswith('yes')][0].split(":")[1]
        else:
            return ''

    def is_connected_to(self, ssid: str) -> bool:
        """
        Checks if there is a connection to the Wi-Fi network with the given name.

        :param ssid: name of the Wi-Fi network (Service Set Identifier)
        :return: True if connected to the Wi-Fi with the given name;
        """

        return self.current_connection() == ssid

    def check_signal_strength(self) -> int:
        """
        Checks the signal strength of the currently connected Wi-Fi network.

        :return: signal strength
        """
        process = subprocess.run(['nmcli', '-f', 'IN-USE,SECURITY,SIGNAL', 'dev', 'wifi'], stdout=subprocess.PIPE)
        if process.returncode == 0:
            self.signal_strength = (int(
                [i for i in process.stdout.decode('utf-8').strip().split('\n') if i.startswith('*')][0].split(
                    '       ')[2]))
            return self.signal_strength
