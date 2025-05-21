import logging
from ..icmp import async_merakicontroller2
from libprobe.asset import Asset
from libprobe.exceptions import CheckException, NoCountException


async def check_merakicontroller(
        asset: Asset,
        asset_config: dict,
        config: dict) -> dict:
    ...
