import json
import disnake
from disnake.ext import commands
from cogs.spotify import SpotifyCog
from cogs.generate_password import GeneratePasswordCog
from cogs.track_url import CurrentTrackUrlCog
from cogs.games import GameCog
from cogs.register import RegisterCog
from cogs.avatar import GetAvatarCog
from cogs.clear import ClearMessagesCog
from cogs.profile import ProfileCog
from cogs.levels import LevelCog
#from cogs.test import TestCog


with open('config.json', 'r+') as f:
    SECRETS = json.load(f)


PREFIX = SECRETS["PREFIX"]
TOKEN = SECRETS["TOKEN"]
INTENTS = disnake.Intents.all()

bot = commands.Bot(command_prefix=PREFIX,intents=INTENTS)

bot.add_cog(SpotifyCog(bot=bot))
bot.add_cog(GeneratePasswordCog(bot=bot))
bot.add_cog(CurrentTrackUrlCog(bot=bot))
bot.add_cog(GameCog(bot=bot))
bot.add_cog(RegisterCog(bot=bot))
bot.add_cog(GetAvatarCog(bot=bot))
bot.add_cog(ClearMessagesCog(bot=bot))
bot.add_cog(ProfileCog(bot=bot))
bot.add_cog(LevelCog(bot=bot))


if __name__ == "__main__":
    bot.run(TOKEN)