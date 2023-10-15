import disnake
from disnake.ext import commands

class ClearMessagesCog(commands.Cog):
    def __init__(self,bot) -> None:
        self.bot = bot

    @commands.slash_command()
    async def clear(inter: disnake.ApplicationCommandInteraction, amount: int):
        await inter.channel.purge(limit=amount)
        await inter.response.send_message(f"{amount} amount of messages have been deleted.")
    
    @commands.command()
    async def clear(ctx: commands.Context, amount: int):
        await ctx.channel.purge(limit=amount)
        await ctx.send(f"{amount} amount of messages have been deleted.")