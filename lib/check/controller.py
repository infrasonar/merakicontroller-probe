from asyncsnmplib.mib.mib_index import MIB_INDEX
from libprobe.asset import Asset
from libprobe.exceptions import CheckException
from ..snmpclient import get_snmp_client
from ..snmpquery import snmpquery

QUERIES = (
    (MIB_INDEX['MERAKI-CLOUD-CONTROLLER-MIB']['merakiObjects'], False),
    (MIB_INDEX['MERAKI-CLOUD-CONTROLLER-MIB']['organization'], False),
)


async def check_controller(
        asset: Asset,
        asset_config: dict,
        check_config: dict) -> dict:

    snmp = get_snmp_client(asset, asset_config, check_config)
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
