import os
import discord
from discord.ext import commands
from webserver import keep_alive as keep_alive

ClientToken = os.environ['MyClientToken']

intents = discord.Intents.default()
intents.members = True
MyClient = commands.Bot(command_prefix='!', self_bot=True, intents=intents)
MyClient.remove_command(help)

@MyClient.event
async def on_ready():
  print(MyClient.user.name)
  await MyClient.change_presence(activity=discord.Activity(type=3, name="You Smarty Pants      oooooooooooooooooooo"), status=discord.Status.online)



@MyClient.event
async def on_message(message):
    if message.author!=MyClient.user:
        async for message in message.channel.history(limit=1):
          user = MyClient.get_user(851116367053717545)
          if "Direct" in str(message.channel):
            await user.send(f"""
            **DM {message.author}:** {message.content}""")
          else:
            await user.send(f"""**{message.guild}**
            **{message.channel}**
            **{message.author}:** *{message.content}*""")
    

keep_alive()
MyClient.run(ClientToken, bot=False)
