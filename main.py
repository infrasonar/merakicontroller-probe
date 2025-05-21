from libprobe.probe import Probe
from lib.check.merakicontroller import check_merakicontroller
from lib.version import __version__ as version


if __name__ == '__main__':
    checks = {
        'merakicontroller': check_merakicontroller
    }

    probe = Probe("merakicontroller", version, checks)

    probe.start()
