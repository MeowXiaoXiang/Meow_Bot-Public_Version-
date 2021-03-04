import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json

with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

class Common(Cog_Extension):
    #ping
    @commands.command(name= 'ping', aliases=['延遲' , '機器人延遲' , 'delay'], brief="common", description="顯示機器人的延遲")
    async def ping(self, ctx):
        embed=discord.Embed(description=f"⌛ Ping：{round(self.bot.latency*1000)} 毫秒 (ms)",color=0xffae00)
        await ctx.send(embed=embed)
    #查詢user資訊
    @commands.command(name= 'user', aliases=['使用者資訊' , '用戶資訊'], brief="common", description="查詢你自己的資訊和所在頻道的資訊")
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
    @commands.command(name= 'sayd', aliases=['說' , '機器人說'], brief="common", description=f"使機器人說話 使用方法：{jdata['command_prefix']}sayd [訊息] ")
    async def sayd(self,ctx,*,value:str=str()):
          await ctx.message.delete()
          if value != str():
              await ctx.send(value)
 
    #近戰有塞急進猛突12x下的暴擊機率計算器
    @commands.command(name='ccc', aliases=['急進猛突' , '急進' , '極盡'], brief="warframe", description=f"計算塞急進猛突後暴率 使用方法：{jdata['command_prefix']}ccc [基礎近戰暴率] [連擊數] [額外暴率加成]")
    async def ccc(self,ctx,*,num='CCC'):
      try:
        i1, i2, i3 = num.split(' ')
        if int(i2) <= 13:
          sum= float(i1) * ( 100 + 60 * ( float(i2) - 1 ) + float(i3) )  / 100
          #總暴率=基礎暴率× (1 + 急進猛突的加成 × (連擊倍率-1)+其他暴擊加成)
          await ctx.send('近戰總爆擊機率：' + str(sum) + '%')
        else:
          await ctx.send('連擊最高只有到13x啦！')
      except:
        await ctx.send(jdata['command_prefix']+'ccc [基礎近戰暴率 連擊數 額外暴率加成]')
    #----------------------------------
    #近戰有塞創口潰爛12x下的觸發機率計算器    
    @commands.command(name= 'wws', aliases=['創口潰爛' , '創口'], brief="warframe", description=f"計算塞創口潰爛後觸發 使用方法：{jdata['command_prefix']}wws [基礎近戰觸發] [連擊數] [額外觸發加成]")
    async def wws(self,ctx,*,num='WWS'):
      try:
        i1, i2, i3 = num.split(' ')
        if int(i2) <= 13:
          sum= float(i1) * ( 100 + 40 * ( float(i2) - 1 ) + float(i3) )  / 100
          #總觸發=基礎觸發× (1 + 觸發加成 × (連擊倍率-1)+其他觸發加成)
          await ctx.send('近戰總觸發機率：' + str(sum) + '%')
        else:
          await ctx.send('連擊最高只有到13x啦！')
      except:
        await ctx.send(jdata['command_prefix']+'wws [基礎近戰觸發 連擊數 額外觸發加成]')

    #環形裝置
    @commands.command(name='toroid',aliases=['環形裝置'], brief="warframe", description='顯示環形裝置出處')
    async def toroid(self,ctx):
      await ctx.send('```維加環形裝置→太空站          & 微蟎蛛型機\n告達環形裝置→昇華實驗室      & 賽托蛛型機(瓦內蜘蛛)\n索拉環形裝置→潤盈寺          & 凱塔蛛型機\n聖油環形裝置→利潤收割者圓蛛\n天藍環形裝置→剝削者圓蛛```')

    
    @commands.command(name= 'avatar', aliases=['頭貼' , '頭像'], brief="common", description=f"此功能可以顯示目標用戶的頭像全圖 用法為：{jdata['command_prefix']}avatar [用戶ID] 要開啟'外觀->開發者模式'然後對用戶滑鼠右鍵複製ID")
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
    bot.add_cog(Common(bot))