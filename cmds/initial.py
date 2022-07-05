import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json
with open('setting.json', mode='r',encoding='utf8') as jfile:
    jdata=json.load(jfile)

class Initial(Cog_Extension):

    @commands.command()
    async def ping(self,ctx):
        await ctx.send(f'現在延遲 {round(self.bot.latency*1000)} (ms)')

    @commands.command()
    async def 自我介紹(self,ctx):
        pic=discord.File(jdata["profile_pic"])
        await ctx.send(jdata["profile"])
        await ctx.send(file=pic)

    #@commands.command()
    #async def hi(self,ctx):
    #    await ctx.send('hi\n')
    

def setup(bot):
    bot.add_cog(Initial(bot))
