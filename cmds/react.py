import discord
import random
import json
from discord.ext import commands
from core.classes import Cog_Extension
import requests

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
        embed.set_footer(text="by jiggly_puff")
        await ctx.send(embed=embed)

    @commands.command()
    async def 查天氣(self,ctx,*,city:str):
        url = "https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001"
        city=city
        params = {
            "Authorization": jdata["Authorization"],
            "locationName": city
        }
        response = requests.get(url, params=params)

        if response.status_code == 200:
            data = json.loads(response.text)
            location = data["records"]["location"][0]["locationName"]
            weather_elements = data["records"]["location"][0]["weatherElement"]
            weather_state = weather_elements[0]["time"][0]["parameter"]["parameterName"]
            rain_prob = weather_elements[1]["time"][0]["parameter"]["parameterName"]
            min_tem = weather_elements[2]["time"][0]["parameter"]["parameterName"]
            comfort = weather_elements[3]["time"][0]["parameter"]["parameterName"]
            max_tem = weather_elements[4]["time"][0]["parameter"]["parameterName"]
            embed=discord.Embed(title="天氣資訊", url="https://www.cwb.gov.tw/V8/C/", description="今日天氣",color=0xff4284)
            embed.add_field(name="城市", value=location, inline=True)
            embed.add_field(name="天氣概況", value=weather_state, inline=True)
            embed.add_field(name="降雨機率", value=rain_prob, inline=True)
            embed.add_field(name="最低溫", value=min_tem, inline=True)
            embed.add_field(name="最高溫", value=max_tem, inline=True)
            embed.add_field(name="體感", value=comfort, inline=True)
            embed.set_footer(text="by jiggly_puff")
            await ctx.send(embed=embed)
            await ctx.send("不管天氣如何都要注意行車安全喔")
            
            
            

    #@commands.command()
    #async def sayd(self,ctx,*,msg):
    #    await ctx.message.delete()
    #    await ctx.send(msg)

    #@commands.command()
    #async def clean(self,ctx,num:int):
    #    await ctx.channel.purge(limit=num+1)
    



    #@commands.command()
    #async def web(ctx):
    #    random_pic=random.choice(jdata["url_pic"])
    #    pic=discord.File(random_pic)
    #    await ctx.send(random_pic)

def setup(bot):
    bot.add_cog(React(bot))