import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json

with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

class common(Cog_Extension):
    tag = "common"
    #ping
    @commands.command(name= 'ping', aliases=['延遲' , '機器人延遲' , 'delay'], brief="顯示機器人的延遲", description="顯示機器人連線至Discord的延遲")
    async def ping(self, ctx):
      latency = round(self.bot.latency*1000)
      red = max(0,min(int(255*(latency-50)/1000),255))
      green = 255-red
      color = discord.Colour.from_rgb(r=red,g=green,b=0)
      embed = discord.Embed(title="當前機器人的延遲",description=f'⌛ Ping：{round(self.bot.latency*1000)} 毫秒 (ms)',color=color)
      await ctx.send(embed=embed)
    #查詢user資訊
    @commands.command(name= 'user', aliases=['使用者資訊' , '用戶資訊'], brief="顯示使用者資訊", description="查詢你自己的資訊和所在頻道的資訊")
    async def user(self,ctx):
        arg = ctx.message.channel
        args = str(arg).split(' ')
        CMD = 'Direct Message with'
        CMDs = CMD.split(' ')
        msg = 'Author:'+str(ctx.message.author)+'\nAuthor ID:'+ str(ctx.message.author.id)+'\nChannel:'+str(ctx.message.channel)+'\nChannel ID:'+str(ctx.message.channel.id)
        if CMDs[0] == args[0] and CMDs[1] == args[1] and CMDs[2] == args[2]:
            print('私人訊息')
            await ctx.send(msg)
        else:
            print('群組訊息')
            msg = msg +'\nGuild.owner:'+str(ctx.guild.owner) +'\nGuild.owner_id:' +str(ctx.guild.owner_id)+'\nGuild.name:' +str(ctx.guild.name)
            await ctx.send(msg)
    #說
    @commands.command(name= 'sayd', aliases=['說' , '機器人說'], brief="復讀", description=f"讓機器人代替你說出msg的內容\n使用方法：{jdata['command_prefix']}sayd [訊息] ")
    async def sayd(self,ctx,*,value:str=str()):
          await ctx.message.delete()
          if value != str():
              await ctx.send(value)

    @commands.command(name= 'avatar', aliases=['頭貼' , '頭像'], brief="顯示目標的頭像", description=f"此功能可以顯示目標用戶的頭像全圖\n用法為：{jdata['command_prefix']}avatar [用戶ID] \n要開啟'外觀->開發者模式'然後對用戶滑鼠右鍵複製ID\n為了不打擾對方採用複製ID的方式")
    async def avatar(self,ctx,userid:str='0'):
      uid2 = userid.split('>')
      uid = int((uid2[0])[-18:])
      user = self.bot.get_user(int(uid))
      if user == None:
        await ctx.send('找不到指定用戶')
      else:
        asset = user.avatar_url
        await ctx.send(str(asset))
    
def setup(bot):
    bot.add_cog(common(bot))