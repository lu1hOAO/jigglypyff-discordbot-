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
        await ctx.send("恭喜獲得我的照片一張\n")
        await ctx.send(file=pic)

    @commands.command()
    async def 爛笑話(self,ctx):
        fun_line=random.choice(jdata["fun"])
        await ctx.send(fun_line)

    @commands.command()
    async def 吃什麼(self,ctx):
        embed=discord.Embed(title="要吃什麼", description="肚子大小事胖丁幫你決定", color=0xff4284)
        food=random.choice(jdata["food"])
        food_url=jdata[food]
        embed.set_thumbnail(url=food_url)
        embed.add_field(name="今天就吃", value=food, inline=False)
        embed.set_footer(text="by juggly_puff")
        await ctx.send(embed=embed)

    #@commands.command()
    #async def web(ctx):
    #    random_pic=random.choice(jdata["url_pic"])
    #    pic=discord.File(random_pic)
    #    await ctx.send(random_pic)

def setup(bot):
    bot.add_cog(React(bot))