from libprobe.probe import Probe
from lib.check.controller import check_controller
from lib.check.device import check_device
from lib.check.interface import check_interface
from lib.check.network import check_network
from lib.check.ssid import check_ssid
from lib.check.vlan import check_vlan
from lib.version import __version__ as version


if __name__ == '__main__':
    checks = {
        'controller': check_controller,
        'device': check_device,
        'interface': check_interface,
        'network': check_network,
        'ssid': check_ssid,
        'vlan': check_vlan,
    }

    probe = Probe("merakicontroller", version, checks)

    probe.start()
