import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json
with open('setting.json', mode='r',encoding='utf8') as jfile:
    jdata=json.load(jfile)

class Event(Cog_Extension):
    @commands.Cog.listener()
    async def on_member_join(self,member):
        channel=self.bot.get_channel(int(jdata['Welcome_channel']))
        await channel.send(f'{member} join!')

    @commands.Cog.listener()
    async def on_member_remove(self,member):
        channel=self.bot.get_channel(int(jdata['Leave_channel']))
        await channel.send(f'{member} leave!')

    @commands.Cog.listener()
    async def on_message(self,msg):
        if msg.content.endswith('胖丁') and msg.author !=self.bot.user:
            await msg.channel.send('需要我幫忙嗎？可以使用自我介紹')
        if "嘿胖丁　"in msg.content and msg.author !=self.bot.user:
            await msg.channel.send('你好像用到全形空白鍵囉，按一下 shift+space 換回半形才能啟動我的指令喔!')

def setup(bot):
    bot.add_cog(Event(bot))