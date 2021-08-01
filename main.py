import os
import discord
from discord.ext import commands
from webserver import keep_alive as keep_alive
from bot import bot

Token = os.environ['Token']


@bot.event
async def on_ready():
  print(bot.user.name)

  await bot.change_presence(activity=discord.Activity(type=3, name="You Smarty Pants      oooooooooooooooooooo"), status=discord.Status.online)

@bot.event
async def on_command_error(ctx, error):
  pass

keep_alive()
bot.run(Token, bot=False)