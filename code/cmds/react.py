import discord
import random
import json
from discord.ext import commands
from core.classes import Cog_Extension

with open('setting.json', mode='r',encoding='utf8') as jfile:
    jdata=json.load(jfile)

class React(Cog_Extension):

    @commands.command()
    async def 傳圖片(self,ctx):
        random_pic=random.choice(jdata["pic"])
        pic=discord.File(random_pic)
        await ctx.send(file=pic)

    @commands.command()
    async def 爛笑話(self,ctx):
        fun_line=random.choice(jdata["fun"])
        await ctx.send(fun_line)

    #@commands.command()
    #async def web(ctx):
    #    random_pic=random.choice(jdata["url_pic"])
    #    pic=discord.File(random_pic)
    #    await ctx.send(random_pic)

def setup(bot):
    bot.add_cog(React(bot))