import discord
from discord.ext import commands

bot=commands.Bot(command_prefix='嘿胖丁 ')

@bot.event
async def on_ready():
    print(">> Bot is online <<")

@bot.event
async def on_member_join(member):
    channel=bot.get_channel(993051908673638421)
    await channel.send(f'{member}join!')

@bot.event
async def on_member_remove(member):
    channel=bot.get_channel(993052029347971142)
    await channel.send(f'{member}leave!')

@bot.command()
async def ping(ctx):
    await ctx.send(f'現在延遲 {round(bot.latency*1000)} (ms)')

bot.run("OTkzMDM4NTE3MjM4MjU1NzM5.GWTc4g.WD1AKbwBKZ2AHVBqaKvzv-6AR5VcQGCnCGrT6c")

