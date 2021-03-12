import os
from discord.ext import commands

class Cog_Extension(commands.Cog):
       def __init__(self,bot):
            if not os.path.exists('log'):
                print(' * The logs folder is not exists.\n * Creating logs folder...')
                os.mkdir('log')
                print(' * Starting Bot...')
            self.bot = bot
