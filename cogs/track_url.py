import disnake
from disnake.ext import commands


class CurrentTrackUrlCog(commands.Cog):
    def __init__(self,bot) -> None:
        self.bot = bot


    @commands.slash_command()
    async def current_track_url(self,inter: disnake.ApplicationCommandInteraction):
        activity_data = inter.author.activities
        spotify_activity = None
        for activity in activity_data:
            if activity.type == disnake.ActivityType.listening:
                spotify_activity = activity

        if spotify_activity:
            spotify_track = spotify_activity.track_url
        elif not spotify_activity:
            spotify_track = "You are not listening to any music"

        await inter.response.send_message(spotify_track)