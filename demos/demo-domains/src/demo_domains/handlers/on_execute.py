from demo_domains.handlers.on_storage_diff import on_storage_diff
from demo_domains.types.name_registry.parameter.execute import ExecuteParameter
from demo_domains.types.name_registry.storage import NameRegistryStorage
from dipdup.context import HandlerContext
from dipdup.models import Transaction


async def on_execute(
    ctx: HandlerContext,
    execute: Transaction[ExecuteParameter, NameRegistryStorage],
) -> None:
    storage = execute.storage
    await on_storage_diff(ctx, storage)
