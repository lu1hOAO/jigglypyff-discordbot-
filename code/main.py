import discord
from discord.ext import commands
import json
import random

with open('setting.json', mode='r',encoding='utf8') as jfile:
    jdata=json.load(jfile)

bot=commands.Bot(command_prefix='嘿胖丁 ')

@bot.event
async def on_ready():
    print(">> Bot is online <<")

@bot.event
async def on_member_join(member):
    channel=bot.get_channel(int(jdata['Welcome_channel']))
    await channel.send(f'{member}join!')

@bot.event
async def on_member_remove(member):
    channel=bot.get_channel(int(jdata['Leave_channel']))
    await channel.send(f'{member}leave!')

@bot.command()
async def ping(ctx):
    await ctx.send(f'現在延遲 {round(bot.latency*1000)} (ms)')

@bot.command()
async def 傳圖片(ctx):
    random_pic=random.choice(jdata["pic"])
    pic=discord.File(random_pic)
    await ctx.send(file=pic)

@bot.command()
async def 講笑話(ctx):
    random_pic=random.choice(jdata["pic"])
    pic=discord.File(random_pic)
    await ctx.send(file=pic)

@bot.command()
async def web(ctx):
    random_pic=random.choice(jdata["url_pic"])
    pic=discord.File(random_pic)
    await ctx.send(random_pic)




@bot.command()
async def 自我介紹(ctx):
    pic=discord.File(jdata["profile_pic"])
    await ctx.send('哈囉我是胖丁\n想要使用指令時請打上嘿胖丁 (嘿胖丁完之後要空一格喔)')
    await ctx.send('以下是目前指令\n ping： 目前延遲\n 傳圖片：我會傳圖片\n\n\n指令還在增加中喔！')
    await ctx.send(file=pic)

bot.run(jdata['TOKEN'])

