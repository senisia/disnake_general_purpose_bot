import asyncio
from urllib import response
import disnake
from disnake.ext import commands
from utils.games.coinflip import coinflip

class GameCog(commands.Cog):
    def __init__(self,bot) -> None:
        self.bot = bot

    @commands.slash_command()
    async def coinflip(self, inter: disnake.ApplicationCommandInteraction, coinflip_choice = None):
        result = coinflip(coinflip_choice=coinflip_choice)
        await inter.response.send_message("The coin spins  <a:bitcoinflipping:1161358606680195092>")

        await asyncio.sleep(2)

        if coinflip_choice and result is True:
            await inter.followup.send("You have won!")

        elif coinflip_choice and result is False:
            await inter.followup.send("You have lost!")

        elif coinflip_choice is None:
            await inter.followup.send("Enter a valid choice, example usage: /coinflip coinflip_choice:heads")
        
    