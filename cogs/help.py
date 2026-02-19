import fluxer
from fluxer import Cog
from utils.send import send

class Help(Cog):
    def __init__(self, bot):
        super().__init__(bot)

    @Cog.command(name="help")
    async def help_command(self, ctx):
        embed = fluxer.Embed(
            title="Help",
            description="Here are the available commands:"
        )
        embed.add_field(
            name="n!help",
            value="Shows this message.",
            inline=False
        )

        await send(ctx, embed=embed)


async def setup(bot):
    await bot.add_cog(Help(bot))