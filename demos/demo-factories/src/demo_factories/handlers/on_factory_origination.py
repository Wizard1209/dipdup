from typing import cast

from demo_factories.types.registry.storage import RegistryStorage
from dipdup.context import HandlerContext
from dipdup.models import Origination


async def on_factory_origination(
    ctx: HandlerContext,
    registry_origination: Origination[RegistryStorage],
) -> None:
    originated_contract = cast(str, registry_origination.data.originated_contract_address)
    name = f'registry_dao_{originated_contract}'
    await ctx.add_contract(
        name=originated_contract,
        address=originated_contract,
        typename='registry',
    )
    await ctx.add_index(
        name=name,
        template='registry_dao',
        values={'contract': originated_contract},
    )
