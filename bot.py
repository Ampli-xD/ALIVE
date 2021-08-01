from discord.ext import commands

bot = commands.Bot(command_prefix='', self_bot=True)
bot.remove_command(help)