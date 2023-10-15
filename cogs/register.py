import disnake
from disnake.ext import commands
import sqlite3

conn = sqlite3.connect(database='C:\\coding\\python\\kl\\kl_disnake_tools_bot\\utils\\sqlite3\\dbs\\users.db')

class RegisterCog(commands.Cog):
    def __init__(self,bot) -> None:
        self.bot = bot


    @commands.slash_command()
    async def register(inter: disnake.ApplicationCommandInteraction):
        cursor = conn.cursor()
        data = (inter.author.id,inter.author.name,0,0)
        sql_query = """--sql
            INSERT INTO users (user_id,username,user_xp,user_currency) VALUES (?,?,?,?)
"""
        cursor.execute(sql_query,data)
        conn.commit()
        embed = disnake.Embed(
            title='Successful',
            description=f"""
                User id: {inter.author.id}
                Username: {inter.author.name}
                User's Currency: 0
                User's XP: 0
            """,
            colour=disnake.Colour.random(),
        )

        await inter.response.send_message(embed=embed)