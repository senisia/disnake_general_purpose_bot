import disnake
from disnake.ext import commands
from utils.sqlite3.queries import increase_currency, check_user_id_exists

class LevelCog(commands.Cog):
    def __init__(self,bot) -> None:
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message: disnake.Message):
        user_id = message.author.id
        if check_user_id_exists(id=user_id):
            increase_currency(id=user_id)