from .embeds import Embeds


async def setup(bot):
    bot.add_cog(Embeds(bot))
