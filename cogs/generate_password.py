import disnake
from disnake.ext import commands
from utils.gen_pass import gen_pass


class GeneratePasswordCog(commands.Cog):
    def __init__(self,bot) -> None:
        self.bot = bot

    @commands.slash_command()
    async def generate_password(inter: disnake.ApplicationCommandInteraction,password_length: int):
        result = gen_pass(password_length=password_length)
        embed = disnake.Embed(title='Your password:', description=result, color=disnake.Colour.random())
        await inter.response.send_message(embed=embed, ephemeral=True)