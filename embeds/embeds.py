import logging

import discord
from redbot.core import checks, commands
from redbot.core.i18n import Translator, cog_i18n

from .events import EmbedsEvents

_ = Translator("Embeds", __file__)
log = logging.getLogger("red.niks-cogs.embeds")


GENERIC_FORBIDDEN = _(
    "I attempted to do something that Discord denied me permissions for."
    "\n"
    "> Your command failed to successfully complete."
)


@cog_i18n(_)
class Embeds(EmbedsEvents, commands.Cog):
    """A collection of embed utilities."""

    def __init__(self, bot):
        super().__init__()
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    @checks.mod_or_permissions(manage_messages=True)
    async def sendembed(self, ctx: commands.Context, title: str, text: str):
        """Send an embed to the current channel.

        The embed will contain a title `title` and body with `text`.
        All normal discord formatting will work inside the embed.
        Do not forget to put every argument into `" "`.
        If you want to attach a picture just add it to the message.

        Examples:
            `[p]sendembed "Title" "Text"`
            `[p]sendembed "📰 Super awesome news" "This is the body of the embed.\n> This is a quote."`
        """

        embed = discord.Embed(title=title, description=text, color=await ctx.embed_color())

        if ctx.message.attachments:
            embed.set_image(url=ctx.message.attachments[0].url)

        await ctx.send(embed=embed)
        try:
            await ctx.message.delete()
        except discord.Forbidden:
            await ctx.send(GENERIC_FORBIDDEN)
