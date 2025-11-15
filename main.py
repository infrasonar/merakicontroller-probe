from libprobe.probe import Probe
from lib.check.controller import CheckController
from lib.check.device import CheckDevice
from lib.check.interface import CheckInterface
from lib.check.network import CheckNetwork
from lib.check.ssid import CheckSsid
from lib.check.vlan import CheckVlan
from lib.version import __version__ as version


if __name__ == '__main__':
    checks = (
        CheckController,
        CheckDevice,
        CheckInterface,
        CheckNetwork,
        CheckSsid,
        CheckVlan,
    )

    probe = Probe("merakicontroller", version, checks)

    probe.start()
