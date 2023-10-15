import disnake
import io
from disnake.ext import commands
from utils.image_manipulation import create_profile_image
from utils.sqlite3.queries import get_user_xp_by_id

class ProfileCog(commands.Cog):
    def __init__(self,bot) -> None:
        self.bot = bot
    
    @commands.slash_command(name="profile")
    async def profile(inter: disnake.ApplicationCommandInteraction):
        total_xp = get_user_xp_by_id(id=inter.author.id)
        if total_xp is None:
            await inter.response.send_message("You have to register first!")
        image_bytes = create_profile_image(url=inter.author.avatar._url, username=inter.author.name, total_xp=total_xp)
        image_stream = io.BytesIO()
        image_bytes.save(image_stream, format='PNG')
        image_stream.seek(0)
        image_file = disnake.File(image_stream, filename=f"{inter.author.name}.png")
        await inter.response.send_message(file=image_file)