import disnake
from disnake.ext import commands

class GetAvatarCog(commands.Cog):
    def __init__(self,bot) -> None:
        self.bot = bot

    @commands.slash_command()
    async def get_avatar(inter: disnake.ApplicationCommandInteraction, member: disnake.Member = None):
        if member is None:
            member = inter.author
        
        embed = disnake.Embed(
            title = f"{member.name}'s avatar: ",
            color = member.accent_colour
        )

        embed.set_image(member.avatar)

        await inter.response.send_message(embed=embed)
        