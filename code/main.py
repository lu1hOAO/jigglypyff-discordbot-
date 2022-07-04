import discord
from discord.ext import commands
import json
import random
import os

with open('setting.json', mode='r',encoding='utf8') as jfile:
    jdata=json.load(jfile)

bot=commands.Bot(command_prefix='嘿胖丁 ')

@bot.event
async def on_ready():
    print(">> Bot is online <<")

@bot.event
async def on_member_join(member):
    channel=bot.get_channel(int(jdata['Welcome_channel']))
    await channel.send(f'{member} join!')

@bot.event
async def on_member_remove(member):
    channel=bot.get_channel(int(jdata['Leave_channel']))
    await channel.send(f'{member} leave!')

@bot.command()
async def load(ctx,extension):
    bot.load_extension(F'cmds.{extension}')
    await ctx.send(F'Loaded {extension} done!')


@bot.command()
async def unload(ctx,extension):
    bot.unload_extension(F'cmds.{extension}')
    await ctx.send(F'Un-Loaded {extension} done!')

@bot.command()
async def reload(ctx,extension):
    bot.reload_extension(F'cmds.{extension}')
    await ctx.send(F'Re-Loaded {extension} done!')



for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        bot.load_extension(f'cmds.{filename[:-3]}')

if __name__=="__main__":
    bot.run(jdata['TOKEN'])

