import asyncio
import logging

from redbot.core import Config
from redbot.core.bot import Red
from redbot.core.i18n import Translator, cog_i18n

_ = Translator("Embeds", __file__)
log = logging.getLogger("red.niks-cogs.embeds")


@cog_i18n(_)
class EmbedsEvents:
    bot: Red
    config: Config
    ready: asyncio.Event

    async def red_delete_data_for_user(self, **kwargs):
        """Nothing to delete."""
        return
