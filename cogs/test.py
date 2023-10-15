import disnake
from disnake.ext import commands

class TestCog(commands.Cog):
    def __init__(self,bot) -> None:
        self.bot = bot


    @commands.command()
    async def test(self,ctx: commands.Context):
        ctx.send("test")
    