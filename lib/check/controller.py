from asyncsnmplib.mib.mib_index import MIB_INDEX
from libprobe.asset import Asset
from libprobe.check import Check
from libprobe.exceptions import CheckException
from ..snmpclient import get_snmp_client
from ..snmpquery import snmpquery

QUERIES = (
    (MIB_INDEX['MERAKI-CLOUD-CONTROLLER-MIB']['merakiObjects'], False),
    (MIB_INDEX['MERAKI-CLOUD-CONTROLLER-MIB']['organization'], False),
)


class CheckController(Check):
    key = 'controller'

    @staticmethod
    async def run(asset: Asset, local_config: dict, config: dict) -> dict:

        snmp = get_snmp_client(asset, local_config, config)
        state = await snmpquery(snmp, QUERIES)

        if not any(state.values()):
            raise CheckException('no data found')

        # we merge everything into single item
        # this is safe because we query only scalar objects
        item = {
            k: v
            for items in state.values()
            for item in items
            for k, v in item.items()
        }
        item['name'] = 'controller'
        return {
            'controller': [item]
        }
