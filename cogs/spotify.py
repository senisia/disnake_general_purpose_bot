import disnake
from disnake.ext import commands


class SpotifyCog(commands.Cog):
    def __init__(self,bot) -> None:
        self.bot = bot


    @commands.slash_command()
    async def current_track(self, inter: disnake.ApplicationCommandInteraction):
        activity_data = inter.author.activities
        spotify_activity = None
        for activity in activity_data:
            if activity.type == disnake.ActivityType.listening:
                spotify_activity = activity
                break

        if spotify_activity:
            spotify_title = spotify_activity.title
            spotify_album = spotify_activity.album
            spotify_artist = spotify_activity.artist
            spotify_duration = spotify_activity.duration
            spotify_colour = spotify_activity.colour
            spotify_album_cover = spotify_activity.album_cover_url
            minutes = int(spotify_duration.total_seconds() // 60)
            seconds = int(spotify_duration.total_seconds() % 60)
            embed = disnake.Embed(
                title=f'Listening to {spotify_title} by {spotify_artist}', 
                description=f'Album: {spotify_album}\nDuration: {minutes}:{seconds}',
                colour=spotify_colour,
            )
            embed.set_image(url=spotify_album_cover)
        else:
            embed = disnake.Embed(
                title='Error',
                description='User is not listening to anything',       
            )

        await inter.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cogs(SpotifyCog(bot))